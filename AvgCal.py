#!/usr/bin/env python3
import re
from func import display
class AverageCalculator:

    highsum=0
    lowsum=0
    humsum=0
    totaldays=0
    
    
    
    def avg_cal(self,file,year,month):
        for line in file:
            regex = year + r"-" +str(month) + r".*?"
            if re.match(regex,line,0):
                data= line.split(",")
                if data[1]:
                    self.highsum+= int(data[1])
                if data[3]:
                    self.lowsum+= int(data[3]) 
                if data[8]:
                    self.humsum+= int(data[8])
                self.totaldays+=1
        
            
            
    def dis(self):
        display("-a",self.totaldays,self.highsum,self.lowsum,self.humsum)             
        
