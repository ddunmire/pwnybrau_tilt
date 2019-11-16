#!/bin/sh

# pwnybrau_read_tilt_stdout.sh
# Simple shortcut script to be called by a splunk univeral forwarder
# BASH script calls python3 based script: pwnbrau_read_tilt.py
#    OUTPUT: JSON : timestamp, Specific gravity. Temperature (degF)
#    Sample output:  {"timestamp":"2019-11-11T15:35:07.046932+00:00","color":"Black","temp":74,"gravity":1.0390000343322754,"rssi":13}
#
export hciAdapterNum=0
export loglevel="ERROR"
export listentime=8

# execute sevice
if [ -z ${SPLUNK_HOME} ]; then
   DIRECTORY=$(cd `dirname $0` && pwd)
   echo $DIRECTORY
   python3 $DIRECTORY/pwnybrau_read_tilt.py --hci=$hciAdapterNum --listentime=$listentime --loglevel=$loglevel
else
   python3 $SPLUNK_HOME/etc/apps/pwnybrau_tilt/bin/pwnybrau_read_tilt.py --hcid=$hciAdapterNum --listentime=$listentime --loglevel=$loglevel
fi
