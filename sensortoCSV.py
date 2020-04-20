#Before running type in -- >sudo apt-get upgrade in the terminal
#Then type --- > sudo apt-get upgrade 
import RPi.GPIO as GPIO
import csv
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
try:
    while True:
        if GPIO.input(17):
            p = "High"
            print(p)
            time.sleep(3)
            p = str(1)
            reporttime = (time.strftime("%H"+":"+"%M"+":"+"%S"))
            csvresult = open("/home/pi/Desktop/test1.csv", "a")
            csvresult.write(p + "," + reporttime + "\n")
            csvresult.close()
        else:
            p = "Low"
            print(p)
            time.sleep(3)
            p = str(0)
            reporttime = (time.strftime("%H"+":"+"%M"+":"+"%S"))
            csvresult = open("/home/pi/Desktop/test1.csv", "a") #a -- > appends and w -- > clears the file and takes in new readings.
            csvresult.write(p + "," + reporttime + "\n")
            csvresult.close()
    
finally:
    GPIO.cleanup()
    