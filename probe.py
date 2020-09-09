import serial
import time
import csv

ser = serial.Serial('COM5',9600)                                #initialize serial & set com port & baud rate
ser.reset_input_buffer()                                        #flush input buffer, discarding all its contents       

filename = time.strftime("%Y%m%d-%H%M%S")                       #get the date and time

with open(filename + '.csv',"a", newline='') as f:              #open (or create) a csv file titled date and time
    writer = csv.writer(f,delimiter=",")
    writer.writerow(['Date','Time','pH'])

while True:
    try:
        line = ser.readline()                                   #read a line from serial
        line = line.decode("utf-8")                             #decode it using utf-8
        print(line)                                             #output the decoded line

        cur_date = time.strftime('%Y-%m-%d')                    #get current date
        cur_time = time.strftime('%H:%M:%S')                    #get current time
        
        with open(filename + '.csv',"a", newline='') as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([cur_date,cur_time,line])
    except:
        print("Keyboard interrupt, ending session")             #press ctrl + c to end session   
        break