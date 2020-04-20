import csv

file = open('/home/pi/Desktop/test.csv','r') #Path to file
showfile = file.read()
file.close()
print(showfile)