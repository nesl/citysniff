#include <sys_module.h>
#include <string.h>
#include <citysniff.h>

#define LED_DEBUG
#include <led_dbg.h>

#define SOUND_TID 0
#define OZONE_TID 1

#define ROOTNODE 4000

typedef struct sampler_state {
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
            if(sys_id() != ROOTNODE){
                if(sys_id()%2) {
                    sys_timer_start(SOUND_TID, 3048, TIMER_REPEAT);
                } else {
                    // every 30 minutes
                    //sys_timer_start(OZONE_TID, 1843200, TIMER_REPEAT);
                    sys_timer_start(OZONE_TID, 5000, TIMER_REPEAT);
                }
            }
            break;

        case MSG_TIMER_TIMEOUT: 
            {
                MsgParam *p = (MsgParam*)(msg->data);
                LED_DBG(LED_GREEN_ON);
                switch(p->byte) {
                    case SOUND_TID:
                        {
                            // microphone
                            sys_post_value(MIC_PID, MSG_MIC_GET_MEASUREMENT, 0, SOS_MSG_RELEASE);
                        }
                        break;

                    case OZONE_TID:
                        // ozone
                        sys_sensor_enable(OZONE_SID);
                        sys_sensor_get_data(OZONE_SID);

                        break;
                }
            }
            break;

        case MSG_MIC_DATA_READY:
            {
                msg_sound_t* m = (msg_sound_t*)sys_malloc(sizeof(msg_sound_t));
                memcpy((void*)&(m->measurement), (void*)msg->data, sizeof(uint32_t));
                LED_DBG(LED_GREEN_OFF);
                sys_post_net(s->spid, MSG_SOUND_DATA, sizeof(msg_sound_t), m, SOS_MSG_RELEASE, ROOTNODE);
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
                            msg_ozone_t* data_msg;

                            LED_DBG(LED_GREEN_OFF);
                            sys_sensor_disable(OZONE_SID);
                            data_msg = (msg_ozone_t*)sys_malloc(sizeof(msg_ozone_t));
                            data_msg->measurement = ((MsgParam*)msg->data)->word;

                            sys_post_net(s->spid,
                                    MSG_OZONE_DATA,
                                    sizeof(msg_ozone_t),
                                    data_msg,
                                    SOS_MSG_RELEASE,
                                    ROOTNODE);
                            break;
                        }
                    }
            }

        case MSG_SOUND_DATA:
            LED_DBG(LED_RED_TOGGLE);
            if(sys_id() == ROOTNODE){
                msg_sound_t* m = (msg_sound_t*)sys_malloc(sizeof(msg_sound_t));
                memcpy((void*)m, (void*)msg->data, sizeof(msg_sound_t));
                sys_post_uart(s->spid, MSG_SOUND_DATA, sizeof(msg_sound_t), m, SOS_MSG_RELEASE, BCAST_ADDRESS);
            }                        

           break;

        case MSG_OZONE_DATA:
           LED_DBG(LED_RED_TOGGLE);
           if(sys_id() == ROOTNODE){
                msg_ozone_t* m = (msg_ozone_t*)sys_malloc(sizeof(msg_ozone_t));
                memcpy((void*)m, (void*)msg->data, sizeof(msg_ozone_t));
                sys_post_uart(s->spid, MSG_OZONE_DATA, sizeof(msg_ozone_t), m, SOS_MSG_RELEASE, BCAST_ADDRESS);
            }                        


            break;

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

