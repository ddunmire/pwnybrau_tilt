#!/bin/sh

# Set up environment
# loglevels :CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
#
#
#
#
#
#
export loglevel="ERROR"
export listentime=8 

# execute sevice
python3 $SPLUNK_HOME/etc/apps/pwnybrau_tilt/bin/pwnybrau_read_tilt.py --listentime=$listentime --loglevel=$loglevel
