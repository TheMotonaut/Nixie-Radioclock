from lib import display


while True:
    time.sleep(1)


    if(disp_sw0.value() && disp_sw1.value()):
        curr_time = time.localtime()

        #Retrieve each digit from current time
        DIG1 = int(str(curr_time.tm_hour)[0])
        DIG2 = int(str(curr_time.tm_hour)[1])
        DIG3 = int(str(curr_time.tm_min)[0])
        DIG4 = int(str(curr_time.tm_min)[1])
        DIG5 = int(str(curr_time.tm_sec)[0])
        DIG6 = int(str(curr_time.tm_sec)[1])

        num_2_disp(DIG1, DIG2, DOT1, DIG3, DIG4, DIG5, DIG6, DOT2)
    else:




        
    
    


