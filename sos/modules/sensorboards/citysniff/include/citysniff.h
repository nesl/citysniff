#ifndef __CITYSNIFF_H__
#define __CITYSNIFF_H__

#include <message_types.h>

#define MIC_PID (APP_MOD_MIN_PID + 80)
#define OZONE_PID (APP_MOD_MIN_PID + 81)

#define MSG_MIC_BUSY (MOD_MSG_START + 80)
#define MSG_MIC_DATA_READY (MOD_MSG_START + 81)
#define MSG_MIC_GET_MEASUREMENT (MOD_MSG_START + 82)

enum {
    OZONE_SID = 1,
};

#define OZONE_HW_CH INCH_1


// MIC module declarations
#define CPU_CLOCK 1000000

enum adcRate {ONE_KHZ = ((CPU_CLOCK)/1000),
    TWO_KHZ = ((CPU_CLOCK)/2000),
    FOUR_KHZ = ((CPU_CLOCK)/4000),
    EIGHT_KHZ = ((CPU_CLOCK) / 8000),
};

#endif //__CITYSNIFF_H__
