from machine import Pin
import time
import pycom

DIG1 = [0b0000010000, 0b0000100000, 0b0001000000, 0b0010000000, 0b0100000000, 0b1000000000, 0b0000000001, 0b0000000010, 0b0000000100, 0b0000001000]
DIG2 = [0b0000010000, 0b0001000000, 0b0010000000, 0b0100000000, 0b1000000000, 0b0000100000, 0b0000000001, 0b0000000010, 0b0000000100, 0b0000001000]
DIG3 = [0b0000000010, 0b0000010000, 0b0000001000, 0b0000100000, 0b0001000000, 0b0010000000, 0b0100000000, 0b1000000000, 0b0000000100, 0b0000000001]

def shift_out_data(data):
    lat_pin.value(0)

    mask = 0b1
    i = 0
    while i < 32 :
        dat_pin.value(data & mask)
        #print(data & mask)
        clk_pin.value(1)
        data = data>>1
        clk_pin.value(0)

        i = i + 1

    lat_pin.value(1)

#data = ((((( << 10) + DIG2) << 2) + DOT1) << 10) + DIG3 #Concatete bits
DOT1 = 0b01
for i in range(0,10):
    for j in range(0,10):
        
        for k in range(0,10):
            #DOT1 = ~DOT1
            time.sleep(0.5)
            pycom.rgbled(0x660000)
            data = (((((DIG1[i] << 10) + DIG2[j]) << 2) + DOT1) << 10) + DIG3[k] #Concatete bit
            #print(bin(data))
            shift_out(data)
            time.sleep(0.5)




