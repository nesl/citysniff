#include <sys_module.h>
#include <string.h>
#include <citysniff.h>

#define LED_DEBUG
#include <led_dbg.h>

#define SAMPLER_TID 0

typedef struct adc_sampler_state {
    uint8_t spid;
} sampler_state_t;

static int8_t sampler_msg_handler(void *state, Message *msg);

static const mod_header_t mod_header SOS_MODULE_HEADER = {
    .mod_id         = DFLT_APP_ID0,
    .state_size     = sizeof(sampler_state_t),
    .num_sub_func   = 0,
    .num_prov_func  = 0,
    .platform_type  = HW_TYPE /* or PLATFORM_ANY */,
    .processor_type = MCU_TYPE,
    .code_id        = ehtons(DFLT_APP_ID0),
    .module_handler = sampler_msg_handler,
};

static int8_t sampler_msg_handler(void *state, Message *msg){
    sampler_state_t* s = (sampler_state_t*)state;
    
    switch(msg->type) {
        case MSG_INIT:
            s->spid = msg->did;
            sys_timer_start(SAMPLER_TID, 3048, TIMER_REPEAT);
            break;

        case MSG_TIMER_TIMEOUT:
            LED_DBG(LED_GREEN_ON);
            // microphone
            //sys_post_value(MIC_PID, MSG_MIC_GET_MEASUREMENT, 0, SOS_MSG_RELEASE);
            // ozone
            sys_sensor_enable(OZONE_SID);
            sys_sensor_get_data(OZONE_SID);
            break;

        case MSG_MIC_DATA_READY:
            {
                uint32_t* data = sys_malloc(sizeof(uint32_t));
                memcpy((void*)data, (void*)msg->data, sizeof(uint32_t));
                LED_DBG(LED_GREEN_OFF);
                sys_post_uart(s->spid, MSG_MIC_DATA_READY, sizeof(uint32_t), data, SOS_MSG_RELEASE, BCAST_ADDRESS);
                break;
            }   

        case MSG_MIC_BUSY:
            LED_DBG(LED_GREEN_OFF);
            break;

        case MSG_DATA_READY:
            {
                switch (((MsgParam*)msg->data)->byte ){

                    case OZONE_SID:
                        {
                            MsgParam* data_msg;

                            LED_DBG(LED_GREEN_OFF);
                            sys_sensor_disable(OZONE_SID);
                            data_msg = (MsgParam*)sys_malloc(sizeof(MsgParam));
                            memcpy((void*)data_msg, (void*)msg->data, sizeof(MsgParam));

                            sys_post_uart(s->spid,
                                    MSG_DATA_READY,
                                    sizeof(MsgParam),
                                    data_msg,
                                    SOS_MSG_RELEASE,
                                    BCAST_ADDRESS);
                            break;
                        }
                    }
            }

        case MSG_FINAL:
            break;

        default:
            return -EINVAL;
    }
    return SOS_OK;
}

#ifndef _MODULE_
mod_header_ptr sampler_get_header()
{
    return sos_get_header_address(mod_header);
}
#endif

