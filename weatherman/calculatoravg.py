#!/usr/bin/env python3
import csv
from helperfunctions import display
class AverageCalculator:

    def __init__(self):
        self.highsum=0
        self.lowsum=0
        self.humsum=0
        self.totaldays=0
    
    def calculate_avg(self,data_file_name):
        with open(data_file_name, "r") as data_file:
            reader= csv.reader(data_file)
            next(reader)
            extractor = csv.DictReader(data_file, dialect="unix", delimiter= "," , quoting= csv.QUOTE_NONE)
            for row in extractor:
                if row["Max TemperatureC"]:
                    self.highsum+= int(row["Max TemperatureC"])
                if row["Min TemperatureC"]:
                    self.lowsum+= int(row["Min TemperatureC"]) 
                if row[" Mean Humidity"]:
                    self.humsum+= int(row[" Mean Humidity"])
                self.totaldays+=1
        
    def report(self):
        display("-a",self.totaldays,self.highsum,self.lowsum,self.humsum)             
        
