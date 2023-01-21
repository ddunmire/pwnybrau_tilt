# pwnybrau_tilt.py
pwnbrau_tilt.py script can be either a service or cmdlin tool.  It will use your bluetooth wireless adapter to listen for ibeacon messages from a Tilt hydrometer.  

Note:  All other ibeacons that are not from TILT hydrometers are dropped.

Below is a list of TILT defined addresses along with their color.  Note the BOLD values map to color.
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

## Usage:
```
$ python3 pwnybrau_tilt.py [--name <value>] [--output={STDOUT,LOG,HEC,MQTT}] [--output_config=<filename>] [--loglevel={INFO, WARN, DEBUG}] [--listentime={int}] [--hci <digit>]

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
  * --name NAME         Sensor Name [Note: only used with MQTT to define 
                        TOPIC Name.]
```


## Sample output from tilt log:
    timestamp=2019-10-22T10:21:34.790175, color=Black, temp=74, gravity=1.027, rssi=-60

## Global Prereqs:
1. python3 
2. libcap2-bin [optional] - for non root execution
3. bluez [optional] - bluetooth cmdline tools


## Install pwnybrau_tilt:
1. copy pwnybrau_tilt into /opt/pwnybrau_tilt
2. from ddunmire/python-bleson project, copy the bleson folder into /opt/pwnybrau_tilt/bin


## Configuration - Pwnbrau Tilt splunk addon for Universal Forwarder (UF)
 
### Install Splunk and configure it to get data in (DGI)
1. Install Splunk Univeral Forwarder  \
     (https://docs.splunk.com/Documentation/Forwarder/8.0.0/Forwarder/Installanixuniversalforwarder)  
2. Configure your Universal Forwarder to connect ot your Splunk Indexers

### Configure UF to use pwnybrau_tilt     
1. create symbolic link so pwnybrau_tilt is app under splunk \
    ln -s /opt/pwnybrau_tilt /opt/splunkforwarder/etc/apps/pwnybrau_tilt
2. restart splunk

## Special note:  pwnybrau running as non-root user
Bluetooth BLE on linux will require root access by default.  You can use the libcap2-bin package to grant python access. 

Assume user = splunk

1. install libcap2-bin package\
    sudo apt-get libcap2-bin
2. Allow python3 to have access to network using libcap2-bin package:\
    sudo setcap cap_net_raw,cap_net_admin+eip $(eval readlink -f `which python3`)
4.

## Blue Tooth LE Beacon tool


### bluez package 
Bluetooth package for linux.  check out [filelist](https://packages.debian.org/buster/armhf/bluez/filelist) for all the stuffs.
```
hcitool - allow you to list local devices, listen and connect to devices   
    $ hcitool dev                <- List local bluetooth device(s) 
        output:
        Devices:
        hci0    DC:A6:32:37:13:4E

    $ hcitool lescan --duplicates
        output:
        LE Scan ...
        EA:0E:2D:1D:74:2F NuFACE Mini
        24:4B:03:36:20:00 [TV] Living room
        50:3D:89:6F:CB:19 SCHLAGE0001234
        ...

hciconfig - enable/disable and other stuffs.
    $ hciconfig lestates
        output: 
        hci0:   Type: Primary  Bus: UART
        BD Address: DC:A6:32:37:13:4E  ACL MTU: 1021:8  SCO MTU: 64:1
        UP RUNNING 
        RX bytes:2689048 acl:0 sco:0 events:80030 errors:0
        TX bytes:19834 acl:0 sco:0 commands:1116 errors:0

```

1. There are android and apple apps that let you listen in on beacons.  You would be amazed just how many there are around you!!!


## For mor information on Tilts beacons
1. Karl Urdevics did a good job decoding the Tilt's ibeacon message.  See https://kvurd.com/blog/tilt-hydrometer-ibeacon-data-format/

## Beneral beacon & bluetooth stuffs 
1. iBeacon - [wikipedia](https://en.wikipedia.org/wiki/IBeacon#Technical_details)
1. [How to Use Legacy Bluetooth LE Beacons](https://esf.eurotech.com/docs/how-to-user-bluetooth-le-beacons)

1. [How to Use Legacy Bluetooth LE Beacon Scanner](https://esf.eurotech.com/docs/how-to-use-bluetooth-le-beacon-scanner)