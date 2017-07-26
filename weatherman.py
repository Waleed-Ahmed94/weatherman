#!/usr/bin/env python3
import re
import sys
from func import months
from Obj import extremefinder
from AvgCal import AverageCalculator
from bargraph import GraphBar

filename = "lahore_weather_"

if(len(sys.argv) < 4 ):
    print("error")
    sys.exit()

path= sys.argv[3]

if sys.argv[1] == "-e":
    year=sys.argv[2]
    myobj = extremefinder()

    for num, month in months.items():

        file = open(path + filename + year + "_" + str(month[0]) + ".txt" , "r")
    
        myobj.extreme_search(file,year,num)
    
    myobj.dis(sys.argv[1])


elif sys.argv[1] == "-a":
    year, month = sys.argv[2].split("/")
    
    myobj = AverageCalculator()
    file = open(path + filename + year + "_" + months[int(month)][0] + ".txt" , "r")
    
    myobj.avg_cal(file,year,month)
    
    myobj.dis()
     
elif sys.argv[1] == "-c":
    year, month = sys.argv[2].split("/")
    
    myobj = GraphBar()
                                   
    file = open(path + filename + year + "_" + months[int(month)][0] + ".txt" , "r")
    
    myobj.graph_draw(file,year,month)
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
