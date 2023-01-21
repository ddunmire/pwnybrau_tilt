#!/usr/bin/env python3

import atexit     #used for graceful exit of script (clean up bluetooth)
import argparse   #used to parse cmdline arguements to this script
import datetime   #used for timestamps
from time import sleep  #used to sleep thread
from bleson import get_provider, Observer                #Bluetooth BLE module
from bleson.logger import log, set_level, DEBUG, INFO    #Bluetooth BLE module: logging object
from bleson.core.hci.type_converters import hex_string   #Bluetooth BLE module: convert 
#from bleson.beacons.ibeacon import iBeacon_advertisement #Bluetooth BLE module: iBeacon advertisement

from ibeacon import iBeacon_advertisement               #Bluetooth BLE module: iBeacon advertisement
from pwnybrau_library.publisherfactory import PublisherFactory
from pwnybrau_library.publisher import Publisher

_TILTS = {
   'a495bb10c5b14b44b5121370f02d74de':'Red',
   'a495bb20c5b14b44b5121370f02d74de':'Green',    
   'a495bb30c5b14b44b5121370f02d74de':'Black',
   'a495bb40c5b14b44b5121370f02d74de':'Purple',
   'a495bb50c5b14b44b5121370f02d74de':'Orange',
   'a495bb60c5b14b44b5121370f02d74de':'Blue',
   'a495bb70c5b14b44b5121370f02d74de':'Yellow',
   'a495bb80c5b14b44b5121370f02d74de':'Pink',
}

_args = ""      #cmdline arguments
_observer = ""
_outputter:Publisher 
_sleepUntil = 0            # this is epoch time after which the next measurement can be processed.

# format json object
_readingtemplate='{{"timestamp":"{time}", "color":"{color}", "temp":{major}, "gravity":{minor}, "rssi":{rssi}}}'  

def exit_handler():
   ###### TODO: gracefull shutdown
   _observer.stop() 

# def get_logfile():
#    today=datetime.date.today()
#    logfile = args.logfile + "." + str(today.year) + "." + str(today.month) + "." + str(today.day) + ".log"
#    return logfile

def on_advertisement(advertisement):
    #Check to see if we are in a "sleep" cycle
    # TODO: figure out how to sleep the observer thread 
    global _sleepUntil
    now = datetime.datetime.now().timestamp()
    if _sleepUntil > now:
      return
    
    ibeacon = iBeacon_advertisement(advertisement)

    if ibeacon.is_ibeacon():
      #_uuid = ibeacon.uuid
      #_major = ibeacon.major
      #_minor = ibeacon.minor
      #_power = ibeacon.power
      #_rssi = ibeacon.rssi     #TODO: RSSI is not always negative number.  need to investigate bluetooth adapter.

      if ibeacon.uuid in _TILTS:
         msg=_readingtemplate.format(time=datetime.datetime.now(datetime.timezone.utc).isoformat(), \
                        color=_TILTS[ibeacon.uuid], major=ibeacon.major, minor=ibeacon.minor/1000, rssi=ibeacon.rssi)
         _outputter.publish(msg)

      # RESET sleep timer
      _sleepUntil = datetime.datetime.now().timestamp() + _args.sleeptime
         

def main():
   global _args, _outputter, _observer

   ###### Parse Arguements
   parser = argparse.ArgumentParser(description='pwnbrau.py will listen for ibeacon messages from a Tilt hydrometer and log them to file or stdout.')
   parser.add_argument("--output", type=str, default="STDOUT", choices=PublisherFactory.PublisherTypes, help="Where to output measurements: (Default: STDOUT)")
   parser.add_argument("--output_config", type=str, default="publish.conf", help="Path and file name of the config file with our output params.  Used with LOG, MQTT and HEC")
   #parser.add_argument("--logfile", default="stdout", help="path/file to output tilt measurements  [defaults to stdout if not included]")
   parser.add_argument("--loglevel", default="INFO", help="script logging level for messages (default: INFO) INFO, DEBUG, WARN, WARNING, ERROR")
   parser.add_argument("--listentime", type=float, default=-1, help="How the script will run (in seconds) before exiting.  (default=-1 run forever)")
   parser.add_argument("--sleeptime", type=float, default=1, help="How long to wait between measurement (in seconds) before exiting.  example: --sleeptime=.3 = 300ms (default=1s)")
   parser.add_argument("--hci", type=int, default=0, help="HCI adpater number for this device.  Use 'hciconfig' to list devices and obtain number.  SYNTAX: hciX where X is a number. (default=0)")
   parser.add_argument("--name", type=str, default="Tilt", help="Sensor Name. [Note: only used with MQTT to define the TOPIC Name.]")
   _args=parser.parse_args()

   # define outputter
   _outputter = PublisherFactory.factory(_args)
   level=set_level(_args.loglevel)

   ###### Define graceful exit
   atexit.register(exit_handler)

   ###### ibeacon adapter and observers
   adapter = get_provider().get_adapter(_args.hci)

   _observer = Observer(adapter)
   _observer.on_advertising_data = on_advertisement
   _observer.start()  # filter duplicates

   ###### Sleep this thread while the observer thread does its magic
   #listentime = _args.listentime
   if _args.listentime == -1:
      ###### TODO: Service Healthcheck and sleep???
      while True:
         sleep (10)

         #TODO clean up files. 
         #TODO what other useful things could this thread do 

   else:
      sleep (_args.listentime)

if __name__ == '__main__':
	main()