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
        print("Highest: %dC on %s %d " %(a[3],months[int(a[0][1])][1],int(a[0][2])))
        print("Lowest: %dC on %s %d" %(a[4],months[int(a[1][1])][1],int(a[1][2])))
        print("Humid: %d%% on %s %d" %(a[5],months[int(a[2][1])][1],int(a[2][2])))
        
        
    elif opt == "-a":
        print("Highest Average: %dC " % (a[1]/a[0]) )
        print("Lowest Average: %dC " % (a[2]/a[0]) )
        print("Average Humidity: %d%% " % (a[3]/a[0]) )
        
    elif opt == "-c":
        print("%d %s %d-%d" %(a[0],a[1], int(a[2]), int(a[3]) ) )
