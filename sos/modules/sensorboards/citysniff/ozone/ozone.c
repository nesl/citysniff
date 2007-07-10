/* -*- Mode: C; tab-width:2 -*- */
/* ex: set ts=2 shiftwidth=2 softtabstop=2 cindent: */

#include <sys_module.h>
#include <sensor.h>
#include <adc_api.h>
#include <bitsop.h>

#define LED_DEBUG
#include <led_dbg.h>

#include <citysniff.h>

#define OZONE_TID 0

typedef struct ozone_state {
	uint8_t state;
  uint8_t ozone_state;
} ozone_state_t;

enum {
  OZONE_IDLE,
  OZONE_READY,
  OZONE_HEATING,
  OZONE_BUSY,
};


// function registered with kernel sensor component
static int8_t ozone_control(func_cb_ptr cb, uint8_t cmd, void *data);
// data ready callback registered with adc driver
int8_t ozone_data_ready_cb(func_cb_ptr cb, uint8_t port, uint16_t value, uint8_t flags);

static int8_t ozone_msg_handler(void *state, Message *msg);

static const mod_header_t mod_header SOS_MODULE_HEADER = {
  mod_id : OZONE_PID,
  state_size : sizeof(ozone_state_t),
  num_sub_func : 0,
  num_prov_func : 2,
	platform_type : HW_TYPE,
	processor_type : MCU_TYPE,
	code_id : ehtons(OZONE_PID),
  module_handler : ozone_msg_handler,
	funct : {
		{ozone_control, "cCw2", OZONE_PID, SENSOR_CONTROL_FID},
		{ozone_data_ready_cb, "cCS3", OZONE_PID, SENSOR_DATA_READY_FID},
	},
};


/**
 * adc call back
 * not a one to one mapping so not SOS_CALL
 */
int8_t ozone_data_ready_cb(func_cb_ptr cb, uint8_t port, uint16_t value, uint8_t flags) {

	ozone_state_t *s = (ozone_state_t*)sys_get_state();
  
	// post data ready message here
	switch(port) {
		case OZONE_SID:
      if(s->ozone_state == OZONE_BUSY){
        // disable heating
        ADC12CTL0 = REF2_5V + REFON; // Internal 2.5V ref on
        DAC12_0CTL = DAC12IR + DAC12AMP_5 + DAC12ENC; // Internal ref gain 1
        DAC12_0DAT = 0x0;  // 0V
        if(sys_sensor_data_ready(OZONE_SID, value, flags) == SOS_OK){
          LED_DBG(LED_RED_OFF);
        }
        // report data
        s->ozone_state = OZONE_IDLE;
      } else {
        return -EINVAL;
      }

			break;
		default:
			return -EINVAL;
	}
	return SOS_OK;
}


static int8_t ozone_control(func_cb_ptr cb, uint8_t cmd, void* data) {\

	ozone_state_t *s = (ozone_state_t*)sys_get_state();
  
	//uint8_t ctx = *(uint8_t*)data;
	
	switch (cmd) {
		case SENSOR_GET_DATA_CMD:
      if(s->ozone_state == OZONE_READY){
        // start heating for 4 minutes
        s->ozone_state = OZONE_HEATING;
        sys_timer_start(OZONE_TID, 245760, TIMER_ONE_SHOT);
        //sys_timer_start(OZONE_TID, 2457, TIMER_ONE_SHOT);
        ADC12CTL0 = REF2_5V + REFON; // Internal 2.5V ref on
        DAC12_0CTL = DAC12IR + DAC12AMP_5 + DAC12ENC; // Internal ref gain 1
        DAC12_0DAT = 0x0A3D;  // 1.6V
        //DAC12_0DAT = 0x0666;  // 1.0V
        LED_DBG(LED_RED_ON);
      } else {
        return -EINVAL;
      }

      break;

		case SENSOR_ENABLE_CMD:
      if(s->ozone_state == OZONE_IDLE){
        LED_DBG(LED_YELLOW_TOGGLE);
        SETBITHIGH(P5OUT, 3);
        s->ozone_state = OZONE_READY;
      } else {
        return -EINVAL;
      }
			break;

		case SENSOR_DISABLE_CMD:
      SETBITLOW(P5OUT, 3);
      s->ozone_state = OZONE_IDLE;
			break;

		case SENSOR_CONFIG_CMD:
			// no configuation
			if (data != NULL) {
				sys_free(data);
			}
			break;

		default:
			return -EINVAL;
	}
	return SOS_OK;
}


int8_t ozone_msg_handler(void *state, Message *msg)
{
	
	ozone_state_t *s = (ozone_state_t*)state;
  
	switch (msg->type) {

		case MSG_INIT:
			// bind adc channel and register callback pointer
		  sys_adc_bind_port(OZONE_SID, OZONE_HW_CH, OZONE_PID,  SENSOR_DATA_READY_FID);
			// register with kernel sensor interface
			sys_sensor_register(OZONE_PID, OZONE_SID, SENSOR_CONTROL_FID, (void*)(&s->state));

      s->ozone_state = OZONE_IDLE;
      // make sure the sensor is off
      SETBITLOW(P5OUT, 3);

			break;

    case MSG_TIMER_TIMEOUT:
      if(s->ozone_state == OZONE_HEATING){
        s->ozone_state = OZONE_BUSY;
        // get ready to read ozone sensor
        return sys_adc_get_data(OZONE_SID, 0);
      } else {
        return -EINVAL;
      }
      break;

		case MSG_FINAL:
			//  unregister ADC port
			sys_adc_unbind_port(OZONE_PID, OZONE_SID);
			// unregister sensor, this will automatically also call SENSOLR_DISABLE_CMD
			sys_sensor_deregister(OZONE_PID, OZONE_SID);
			break;

		default:
			return -EINVAL;
			break;
	}
	return SOS_OK;
}


#ifndef _MODULE_
mod_header_ptr ozone_get_header() {
	return sos_get_header_address(mod_header);
}
#endif

