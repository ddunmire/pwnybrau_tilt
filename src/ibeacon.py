from bleson.core.types import Advertisement
from bleson.core.hci.type_converters import hex_string

#ibeacon_advertisement
# this class defines all the properties as defined in the apple ibeacon standard 
# fieldname     : position  : example 
# ManufactureID : 0-1       : x04 x00
# ibeacon const : 2-3       : x02 x15
# UUID          : 4-19      : xa495bb10c5b14b44b5121370f02d74de
# Major         : 20-21     : x004a
# Minor         : 22-23     : x0400
# power         : 24        : x00
# RSSI          : 25        : x
class iBeacon_advertisement:
    def __init__(self, advertisement):
        self.advertisement = advertisement

    def is_ibeacon(self):
        if self.advertisement.mfg_data is None:
            return False

        elif ("4c 00 02 15" in hex_string(self.advertisement.mfg_data[0:4])):
            return True
        else:
            return False

#    @property
#    def raw_advertisement(self):
#        return self.advertisement

    @property
    def uuid(self):
        uuid = hex_string(self.advertisement.mfg_data[4:20])
        return uuid.replace(" ","")

    @property
    def major(self):
        major = int.from_bytes(self.advertisement.mfg_data[20:22], 'big')
        return major

    @property
    def minor(self):
        tmp=self.advertisement.mfg_data[22:24]
        minor = int.from_bytes(tmp, 'big')
        return minor

    @property
    def power(self):
        return self.advertisement.tx_pwr_lvl

    @property    
    def rssi(self):
        return self.advertisement.rssi
