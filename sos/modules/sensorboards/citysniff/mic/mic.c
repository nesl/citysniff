#include <sys_module.h>
#include <signal.h>
#include <msp430/adc12.h>
#include <msp430/dma.h>
#include <bitsop.h>
#include <math.h>

#include "citysniff.h"

#define LED_DEBUG
#include <led_dbg.h>

#define SAMPLES 1020

enum {
    MIC_IDLE,
    MIC_BUSY,
};

typedef struct mic_state {
    sos_pid_t spid;
    uint16_t data[SAMPLES];
    uint8_t state;
} mic_state_t;

static int8_t mic_msg_handler(void *state, Message *msg);

int8_t mic_start(uint16_t* start, uint16_t length, enum adcRate rate);
void mic_stop( );

static const mod_header_t mod_header SOS_MODULE_HEADER = {
    .mod_id         = MIC_PID,
    .state_size     = sizeof(mic_state_t),
    .num_timers     = 0,
    .num_sub_func   = 0,
    .num_prov_func  = 0,
    .platform_type  = HW_TYPE /* or PLATFORM_ANY */,
    .processor_type = MCU_TYPE,
    .code_id        = ehtons(MIC_PID),
    .module_handler = mic_msg_handler,
};

static int8_t mic_msg_handler(void *state, Message *msg){
    
    mic_state_t* s = (mic_state_t*)state;

    switch(msg->type) {
        case MSG_INIT:
            P6DIR &=~(0x01); //input
            P6SEL |= 0x01; //ADC12 function
            SETBITHIGH(P5OUT, 0); // enable microphone
            s->spid = -1;
            s->state = MIC_IDLE;
            break;  
    
        case MSG_FINAL:
            mic_stop();  
            P6DIR |= 0x01;
            P6SEL &= ~(0x01);
            SETBITLOW(P5OUT, 0); 
            break;  

        case MSG_MIC_GET_MEASUREMENT:
            if(s->state == MIC_BUSY){
                sys_post_value(msg->sid, MSG_MIC_BUSY, 0, SOS_MSG_RELEASE);
            } else {
                s->spid = msg->sid;
                s->state = MIC_BUSY;
                if(mic_start(s->data, SAMPLES, EIGHT_KHZ) != SOS_OK){
                    sys_post_value(msg->sid, MSG_MIC_BUSY, 0, SOS_MSG_RELEASE);
                }
            }
            break;

        case MSG_MIC_DATA_READY:
            {
                uint32_t sum = 0;
                uint16_t avg;
                uint16_t i = 0;

                for(i=0; i<SAMPLES; i++){
                    sum += s->data[i];
                }

                avg = sum / SAMPLES;

                for(i=0; i<SAMPLES; i++){
                    sum += ((s->data[i]-avg)*(s->data[i]-avg));
                }

                s->state = MIC_IDLE;
                sys_post_value(s->spid, MSG_MIC_DATA_READY, sum, SOS_MSG_RELEASE);
                break;
            }
        default:
            return -EINVAL;
    }
    return SOS_OK;
}

interrupt (DACDMA_VECTOR) dac_dma_interrupt (){
    SYS_LED_DBG(LED_YELLOW_OFF);
    if((DMA0CTL & DMAIFG) == DMAIFG){
        mic_stop( );
        DMA0CTL &= ~DMAIFG;

        // Access your data here
        sys_post_value(MIC_PID, MSG_MIC_DATA_READY, 0, SOS_MSG_RELEASE);
    } else if ((DMA0CTL & DMAABORT) == DMAABORT){
        // DMA got aboarted.. try again next time
        DMA0CTL = 0;
        mic_stop();
        SYS_LED_DBG(LED_RED_TOGGLE);
    } else {
        // something went wrong. Stop the dma and adc and try again next time
        DMA0CTL = 0;
        mic_stop();
    }
}

int8_t mic_start(uint16_t* start, uint16_t length, enum adcRate rate){
  SYS_LED_DBG(LED_YELLOW_ON);
  
  if((DMA0CTL & DMAEN) == DMAEN){ //a DMA trasnfer is active
    SYS_LED_DBG(LED_RED_TOGGLE);
	// this shouldn't happen. Stop it and try again next time.
	mic_stop();
	DMA0CTL = 0;
    return -EINVAL; 
  }  
  //stop new ADC transfers (stop timerA)
  TACTL = TACLR;
  DMA0CTL = 0; //stop DMA transfers
  ADC12CTL0 &= ~(ENC); //disable converter
  //wait for pending conversions to finish
  //XXX not sure why, but the adc conversion is sometimes still going and and blocks here...
  //while((ADC12CTL1 & ADC12BUSY) != 0){LED_DBG(LED_RED_TOGGLE);}; 
  
  ADC12CTL0 = (ADC12ON+SHT0_0 +SHT1_0);    // Turn on ADC12
  ADC12CTL1 = (SHS_1 + ADC12SSEL_1 + CONSEQ_2); // User TimerA, and SMCLK          
  ADC12MCTL0 = (SREF_0 |INCH_0); // use ADC0 and Vcc as reference
  ADC12IFG =0; //clear any pending interrupts
  
  //configure TimerA
  TACCR0 = rate; // time when reset
  TACCR1 = rate/2; // time when set
  TACCTL1 = (OUTMOD_3); // use set/reset mode
  TACTL = (TASSEL_2);//clock source SMCLK
  
  //configure and start DMA
  //configure DMA channel
  DMACTL0 =  DMA0TSEL_6;
  DMACTL1 = 0;  
  //set DMA addresses
  DMA0DA = (unsigned int) start;
  DMA0SZ = length;
  DMA0SA = (unsigned int) &(ADC12MEM0);
  //set channel 0 properties
  DMA0CTL = ( DMADT_0 | DMAIE | DMASWDW |DMASRCINCR_0  |DMADSTINCR_3 |DMAEN); 
  
  //start TimerA (and the conversions)
  ADC12CTL0 |= ENC;  
  TACTL |= MC_1; //counts up to TACL0
  return SOS_OK;
}


void mic_stop( ){
  //stop pending DMAs 
  
  //stop ADC trigger (stop timerB)
  TACTL = TACLR;
 //stop ADC
  //while((ADC12CTL1 & 0x0001) != 0){}; //wait for pending conversions to complete
  ADC12CTL0 &= ~(ENC); //disable converter
  //turn the ADC off 
  ADC12CTL0 &= ~ADC12ON;  
}


#ifndef _MODULE_
mod_header_ptr mic_get_header()
{
    return sos_get_header_address(mod_header);
}
#endif

