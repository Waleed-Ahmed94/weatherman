#!/usr/bin/env python3
import re
from termcolor import colored, cprint
from func import display

class GraphBar:

    graph=""
    count= 1
    
    
    
    def graph_draw(self,file,year,month):
        for line in file:
            regex = year + r"-" + str(month) + r".*?"
            if re.match(regex,line,0):
                data= line.split(",")
                self.graph= ""
                if data[1] and data[3]:
            
                    for x in range(int(data[1])):
                        if x < int(data[3]):
                            self.graph += colored("+","blue")
                            continue
                        else:
                            self.graph += colored("+", "red")
                
                    display("-c",self.count,self.graph, int(data[3]), int(data[1]) ) 
                
                self.count += 1
