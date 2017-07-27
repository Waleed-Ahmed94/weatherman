#!/usr/bin/env python3
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

def display(opt,*a):
    if opt == "-e":
        max_temp_day,min_temp_day,most_humid_day,max_temp,min_temp,most_humid = a 
        print("Highest: %dC on %s %d " %(max_temp,months[int(max_temp_day[1])][1],int(max_temp_day[2])))
        print("Lowest: %dC on %s %d" %(min_temp,months[int(min_temp_day[1])][1],int(min_temp_day[2])))
        print("Humid: %d%% on %s %d" %(most_humid,months[int(most_humid_day[1])][1],int(most_humid_day[2])))
        
    elif opt == "-a":
        totaldays,high_avg,min_avg,avg_humid = a
        print("Highest Average: %dC " % (high_avg/totaldays) )
        print("Lowest Average: %dC " % (min_avg/totaldays) )
        print("Average Humidity: %d%% " % (avg_humid/totaldays) )
        
    elif opt == "-c":
        print("%d %s %d-%d" %(a[0],a[1], int(a[2]), int(a[3]) ) )
