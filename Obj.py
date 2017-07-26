#!/usr/bin/env python3
from func import display
import re

class extremefinder:
    
    max = 0
    min = 50
    humid = 0
    highday = 0
    minday = 0
    humidday = 0
    
    
    
    def cmp(self, opt, a, day):
        if opt == "maxtemp":
            if a > self.max:
                self.max = a
                self.highday = day
        
        elif opt == "mintemp":
            if a < self.min:
                self.min = a
                self.minday = day
            
        elif opt == "mosthumid":
            if a > self.humid:
                self.humid = a
                self.humidday = day
                
    
    def extreme_search(self, file,year,num):
        for line in file:
            regex = year + r"-" + str(num) + r".*?" 
            if re.match(regex,line,0):
                data = line.split(",")
                if data[1]:
                    self.cmp("maxtemp",int(data[1]),data[0])
            
                if data[3]:
                	self.cmp("mintemp",int(data[3]),data[0])
                if data[8]:
                	self.cmp("mosthumid", int(data[8]),data[0])
            
            
    def dis(self, opt):
         display(opt,self.highday.split("-"),self.minday.split("-"),self.humidday.split("-"),self.max,self.min,self.humid)
        

