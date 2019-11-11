#!/bin/sh

# Set up environment
# loglevels :CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
#
#
#
#
#
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
