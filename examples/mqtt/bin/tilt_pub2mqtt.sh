#!/bin/sh

# pwnybrau_read_tilt_stdout.sh
# Simple shortcut script to be called by a splunk univeral forwarder
# BASH script calls python3 based script: pwnbrau_read_tilt.py
#    OUTPUT: JSON : timestamp, Specific gravity. Temperature (degF)
#    Sample output:  {"timestamp":"2019-11-11T15:35:07.046932+00:00","color":"Black","temp":74,"gravity":1.0390000343322754,"rssi":13}
#
export output="MQTT"                                # output destination: STDOUT, MQTT, LOG or HEC
#export output="STDOUT"
export output_config="../local/publish_mosquitto.conf"   # output configuration file for defining endpoint
export listentime=-1                                 # total time to take measurements (note -1 = infinity)
export sleeptime=10                                  # time to wait between measurements

export hciAdapterNum=0
export loglevel="ERROR"


# Note --show_device_info         # print atlas device info


###########
## START 

# is python3 installed?
command -v python3 > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "Could not find python3.  Exiting..."
  exit 1
fi

# execute sevice
echo "python3 ../../../src/pwnybrau_tilt.py --debug --output=${output} --output_config=${output_config} --hci=$hciAdapterNum --listentime=$listentime --loglevel=$loglevel --output_config=\"${output_config}\" --listentime=${listentime} --sleeptime=${sleeptime}"

python3 ../../../src/pwnybrau_tilt.py --debug --output=${output} --output_config=${output_config} --listentime=${listentime} --sleeptime=${sleeptime}
