#!/usr/bin/env python3
import re

import sys

from termcolor import colored, cprint

def cmp(a,b,c,d,e):
    if c == "max":
        if a > b:
            return [a,d]
        else:
            return [b,e]
    elif c == "min":
        if a < b:
            return [a,d]
        else:
            return [b,e]
    

     


filename = "lahore_weather_"

months = {

      1: ["Jan", "January"],
      2: ["Feb", "February"],
      3: ["Mar", "March"],
      4: ["Apr",  "April"],
      5: ["May",  "May"],
      6: ["Jun",  "June"],
      7: ["Jul",  "July"],
      8: ["Aug",  "August"],
      9: ["Sep",  "September"],
      10: ["Oct", "October"],
      11: ["Nov", "November"],
      12: ["Dec", "December"]
}

max = 0
min = 50
highday = 0
minday = 0
humid = 0
humiday= 0

if(len(sys.argv) < 4 ):
    print("error")
    sys.exit()



path= sys.argv[3]

if sys.argv[1] == "-e":
    year=sys.argv[2]
    for num, month in months.items():

        file = open(path + filename + year + "_" + str(month[0]) + ".txt" , "r")
    
        for line in file:
            regex = year + r"-" + str(num) + r".*?" 
            if re.match(regex,line,0):
                data = line.split(",")
                if data[1]:
                    max, highday = cmp(int(data[1]), max , "max" , data[0], highday )
            
                if data[3]:
                	min, minday = cmp(int(data[3]), min , "min" , data[0] , minday )
                if data[8]:
                	humid, humiday = cmp(int(data[8]), humid , "max" , data[0] , humiday)
                

    day1= highday.split("-")
    day2= minday.split("-")
    day3= humiday.split("-")
    print("Highest: %dC on %s %d " %(max,months[int(day1[1])][1],int(day1[2])))
    print("Lowest: %dC on %s %d" %(min,months[int(day2[1])][1],int(day2[2])))
    print("Humid: %d%% on %s %d" %(humid,months[int(day3[1])][1],int(day3[2])))


elif sys.argv[1] == "-a":
    year, month = sys.argv[2].split("/")
    highsum=0
    lowsum=0
    humsum=0
    totaldays=0
    
    file = open(path + filename + year + "_" + months[int(month)][0] + ".txt" , "r")
    for line in file:
        regex = year + r"-" +str(month) + r".*?"
        if re.match(regex,line,0):
            data= line.split(",")
            if data[1]:
                highsum+= int(data[1])
            if data[3]:
                lowsum+= int(data[3]) 
            if data[8]:
                humsum+= int(data[8])
            totaldays+=1
            
    print("Highest Average: %dC " % (highsum/totaldays) )
    print("Lowest Average: %dC " % (lowsum/totaldays) )
    print("Average Humidity: %d%% " % (humsum/totaldays) )
           
elif sys.argv[1] == "-c":
    year, month = sys.argv[2].split("/")
    count= 1
    
                                   
    file = open(path + filename + year + "_" + months[int(month)][0] + ".txt" , "r")
    for line in file:
        regex = year + r"-" + str(month) + r".*?"
        if re.match(regex,line,0):
            data= line.split(",")
            graph= ""
            if data[1] and data[3]:
            
                for x in range(int(data[1])):
                    if x < int(data[3]):
                        graph += colored("+","blue")
                        continue
                    else:
                        graph += colored("+", "red")
                    
                print("%d %s %d-%d" %(count,graph, int(data[1]), int(data[3]) ) )
            count+=1
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
