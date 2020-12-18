import time
import machine
import pycom
from network import WLAN

#Pin setup for display with shift registers
disp_clk = Pin('', mode=Pin.OUT) #Clock pin
disp_data = Pin('', mode=Pin.OUT) #Data pin
disp_lat = Pin('', mode=Pin.OUT) #Latch pin
disp_blk = Pin('', mode=Pin.OUT) #Blanking pin
disp_sw0 = Pin('', mode=Pin.IN, pull=Pin.PULL_UP)
disp_sw1 = Pin('', mode=Pin.IN, pull=Pin.PULL_UP)

#Default values for display
clk_pin.value(1)
dat_pin.value(0)
lat_pin.value(0)
blk_pin.value(1)

#Si4705 GPIO pins
gpio1 = Pin('', mode.Pin.OPEN_DRAIN)
gpio2 = Pin('', mode.Pin.OPEN_DRAIN)

#SPI to Si4705 
spi = SPI(1, mode=SPI.MASTER, baudrate=350000, polarity=0, phase=0, firsbit=SPI.MSB, pins=('', '', ''))



#Connect to WLAN
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid="AndroidAP", auth=(WLAN.WPA2, "hgyg8367"))

while not wlan.isconnected():
    machine.idle()


#Connect to NTP-server and setup time
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
while not rtc.synced():
    machine.idle()

#Stockholm timezone
time.timezone(60**2)
