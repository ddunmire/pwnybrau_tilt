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
python3 pwnybrau_tilt.py [--name <value>] [--output={STDOUT,LOG,HEC,MQTT}] [--output_config=<filename>] [--loglevel={INFO, WARN, DEBUG}] [--listentime={int}] [--hci <digit>]

optional parameters:
  * -h, --help          show this help message and exit
  * --output {STDOUT,LOG,HEC,MQTT}
                        Where to output measurements: (Default: STDOUT)
  * --output_config OUTPUT_CONFIG
                        Path and file name of the config file with our output
                        params. Used with LOG, MQTT and HEC
  * --loglevel LOGLEVEL   script logging level for messages (default: INFO)
                        INFO, DEBUG, WARN, WARNING, ERROR
  * --listentime LISTENTIME
                        How the script will run (in seconds) before exiting.
                        (default=-1 run forever)
  * --hci HCI           HCI adpater number for this device. Use hciconfig to
                        list devices and obtain number (X): hciX (default=0)
  * --name NAME         Sensor Name [Note: only used with MQTT to define the TOPIC Name.]

## Sample output from tilt log:
    timestamp=2019-10-22T10:21:34.790175, color=Black, temp=74, gravity=1.027, rssi=-60

## Global Prereqs:
1. python3 
2. libcap2-bin [optional] - for non root execution    


## Install pwnybrau_tilt:
1. copy pwnybrau_tilt into /opt/pwnybrau_tilt
2. from ddunmire/python-bleson project, copy the bleson folder into /opt/pwnybrau_tilt/bin


## Configuration - Pwnbrau Tilt splunk addon for Universal Forwarder (UF)
 
### Install Splunk and configure it to get data in (DGI)
1. Install Splunk Univeral Forwarder  \
     (https://docs.splunk.com/Documentation/Forwarder/8.0.0/Forwarder/Installanixuniversalforwarder)  
2. Follow the GDI steps from splunk developer service (SDS) to configure your certificate 
     (https://dev.splunk.com/scs/docs/add/ingest_forwarder)
3. 

### Configure UF to use pwnybrau_tilt     
1. create symbolic link so pwnybrau_tilt is app under splunk \
    ln -s /opt/pwnybrau_tilt /opt/splunkforwarder/etc/apps/pwnybrau_tilt
2. restart splunk

### Splunk Developer Services (SDS) - import pipeline and dashboards
The pipeline will process events sent to SDS and store them in the correct indexes.  The indexes can be searched via Splunk Investigate (SI).
1. login to SDS and access your tenant
2. TODO:  create pipelines and store in pwnybrau_tilt/pipelines :)  








## Special note:  pwnybrau running as non-root user
Bluetooth BLE on linux will require root access by default.  You can use the libcap2-bin package to grant python access. 

Assume user = splunk

1. install libcap2-bin package\
    sudo apt-get libcap2-bin
2. Allow python3 to have access to network using libcap2-bin package:\
    sudo setcap cap_net_raw,cap_net_admin+eip $(eval readlink -f `which python3`)
4.


