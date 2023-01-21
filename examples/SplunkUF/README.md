#Splunk Universal Forwarder Scripted Input Example  
This example is designed to run on a raspberry pi connected with bluetooth.  

The UF will call a bash shell script to read a on a 10sec interval.  (see inputs.conf).  

The atlasTEMP.py and atlasPH.py scripts could be called directly, but this allow for admin to execute the script seperately to sample the output and be sure it is functioning correctly.


## Prerequisite
1. You have already installed Splunk Enterprise (somewhere)
1. You already have a Universal Forwarder running and connected to the splunk indexer(s)
1. Universal Forwarder has bluetooth enabled and can receive ibeacon messages.

## Installation
These instructions the splunk UF.  
1. copy SplunkUF example to $SPLUNK_HOME/etc/apps/pwnybrau_tilt
1. copy PWNYBRAU_TILT/src to $SPLUNK_HOME/etc/apps/pwnybrau_tilt/bin

    Note: You can test the shell script reads sensor and outputs to STDOUT.
    ```
    $ python3 pwnybrau_tilt.py  --output=STDOUT --hci=0 --listentime=5 
    ```

## Configuration
1. enable scripts by updating $SPLUNK_HOME/etc/apps/pwnybrau_tilt/local/inputs.conf
   - Set disabled = 0
1. [optional] You can change the granularity of polling or the name of the sensor by editing the scripts called by the scripted input located in this folder: $SPLUNK_HOME/etc/apps/pwnybrau_tilt/
Here are a few settings:
    - listentime : total time used to poll
    - sleeptime  : time between polls  
        >Note: total number of polls typically is listentime/ sleeptime - 1.  The -1 is a rule of thumb.  The code needs time to read the bus and output data and the longer listentime is, the more that delay adds up. 
    - hciAdapterNum     : hardware number (default = 0)
    - i2caddress : Atlas sensor address in i2cbus                 

1. restart UF
