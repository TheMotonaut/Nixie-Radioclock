import time
import machine
import pycom
from network import WLAN

#Pin setup
disp_clk = Pin('P11', mode=Pin.OUT) #Clock pin
disp_data = Pin('P10', mode=Pin.OUT) #Data pin
disp_lat = Pin('P9', mode=Pin.OUT) #Latch pin
disp_blk = Pin('P8', mode=Pin.OUT) #Blanking pin

#Si4705 GPIO pins
gpio1 = Pin('', mode.Pin.OPEN_DRAIN)
gpio2 = Pin('', mode.Pin.OPEN_DRAIN)

#SPI to Si4705 
spi = SPI(1, mode=SPI.MASTER, baudrate=350000, polarity=0, phase=0, firsbit=SPI.MSB, pins=('', '', ''))



pycom.heartbeat(False)

clk_pin.value(1)
dat_pin.value(0)
lat_pin.value(0)
blk_pin.value(1)



#Connect to WLAN
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid="AndroidAP", auth=(WLAN.WPA2, "hgyg8367"))

while not wlan.isconnected():
    machine.idle()


#Connect to NTP-server 
print("Connected")
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
while not rtc.synced():
    machine.idle()

time.timezone(60**2)
