from machine import Pin
import time
import pycom

#Lookup table for shiftregister connected to nixie tubes
DIG1_tbl = [0b0000010000, 0b0000100000, 0b0001000000, 0b0010000000, 0b0100000000, 0b1000000000, 0b0000000001, 0b0000000010, 0b0000000100, 0b0000001000]
DIG2_tbl = [0b0000010000, 0b0001000000, 0b0010000000, 0b0100000000, 0b1000000000, 0b0000100000, 0b0000000001, 0b0000000010, 0b0000000100, 0b0000001000]
DIG3_tbl = [0b0000000010, 0b0000010000, 0b0000001000, 0b0000100000, 0b0001000000, 0b0010000000, 0b0100000000, 0b1000000000, 0b0000000100, 0b0000000001]



#Function whichs take a decimal and converts it to a equivalent 10-bit value for shift register, concatate the bitstring and shifts it out
def num_2_disp(DIG1, DIG2, DOT1, DIG3, DIG4, DIG5, DIG6, DOT2):
    data = (((((DIG1_tbl[DIG1] << 10) + DIG2_tbl[DIG2]) << 2) + DOT1) << 10) + DIG3_tbl[DIG3] #Concatete bit
    shift_out_data(data)


#Shifts out a 32 bitstring to shift register
def shift_out_data(data):
    lat_pin.value(0)

    mask = 0b1
    i = 0
    while i < 32 :
        dat_pin.value(data & mask)
        clk_pin.value(1)
        data = data>>1
        clk_pin.value(0)

        i = i + 1

    lat_pin.value(1)
