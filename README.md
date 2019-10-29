# pwnybrau_read_tilt.py
pwnbrau.py script can be either a service or cmdlin tool.  It will listen for ibeacon messages from a Tilt hydrometer. 

Note:  All other ibeacons that are not from TILT hydrometers are dropped.
    UUID | Tilt Color 
    ---- | ---------- 
   a495bb **10** c5b14b44b5121370f02d74de | Red
   a495bb **20** c5b14b44b5121370f02d74de | Green    
   a495bb **30** c5b14b44b5121370f02d74de | Black
   a495bb **40** c5b14b44b5121370f02d74de | Purple
   a495bb **50** c5b14b44b5121370f02d74de | Orange
   a495bb **60** c5b14b44b5121370f02d74de | Blue
   a495bb **70** c5b14b44b5121370f02d74de | Yellow
   a495bb **80** c5b14b44b5121370f02d74de | Pink


## Syntax:
python3 pwnybrau_read_tilt.py [--logfile=<filename>] [--loglevel=(INFO, WARN, DEBUG)] [--listentime={int}]

optional parameters:
  * --logfile: path/file to output tilt measurements  [defaults to stdout if not included]
  * --loglevel: script logging level for messages [default = INFO]
  * --listentime: Time (in seconds) the script will wait for ibeacon events before exiting.  (default=-1 run forever)


## Sample output from tilt log:
    timestamp=2019-10-22T10:21:34.790175, color=Black, temp=74, gravity=1.027, rssi=-60

## Global Prereqs:
1. python3 
2. libcap2-bin [optional] - for non root execution    


## Install:
1. Copy: pwnybrau_tilt.tar to /opt
2. extract: tar -xvf pwnbrau_tilt.tar

## Configuration - Pwnbrau Tilt service



### Configuration - runas non-root
Assume user = splunk

1. install libcap2-bin package\
    sudo apt-get libcap2-bin
2. Allow python3 to have access to network using libcap2-bin package:\
    sudo setcap cap_net_raw,cap_net_admin+eip $(eval readlink -f `which python3`)
4.

## Configuration - Pwnbrau Tilt splunk addon for Universal Forwarder (UF)
This addon is designed to configure the UF to watch the /opt/pwnybrau/logs folder for 
