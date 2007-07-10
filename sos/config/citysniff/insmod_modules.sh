#!/bin/bash

BASEDIR=`pwd`/../../

# for now, mic does not work as module!
#cd ../../modules/sensorboards/citysniff/mic/
#make clean && make tmote
#sos_tool.exe --insmod mic.mlf
cd $BASEDIR/modules/sampler
make clean && make tmote
sos_tool.exe --insmod sampler.mlf
