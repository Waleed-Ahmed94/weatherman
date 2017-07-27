#!/usr/bin/env python3
from helperfunctions import display
import csv

class ExtremeFinder:
    
    def __init__(self):
        self.max= 0
        self.min = 50
        self.humid = 0
        self.highday = 0
        self.minday = 0
        self.humidday = 0
    
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
                
    def extreme_search(self, data_file_name):
        with open(data_file_name, "r") as data_file:
            reader= csv.reader(data_file)
            next(reader)
            extractor = csv.DictReader(data_file, dialect="unix", delimiter= "," , quoting= csv.QUOTE_NONE)
            date= "PKT"
            for row in extractor:
                if "PKT" not in row.keys():
                    date = "PKST"
                if row["Max TemperatureC"]:
                    self.cmp("maxtemp",int(row["Max TemperatureC"]),row[date])
                if row["Min TemperatureC"]:
                	self.cmp("mintemp",int(row["Min TemperatureC"]),row[date])
                if row[" Mean Humidity"]:
                	self.cmp("mosthumid", int(row[" Mean Humidity"]),row[date])
            
    def report(self, opt):
         display(opt,self.highday.split("-"),self.minday.split("-"),self.humidday.split("-"),self.max,self.min,self.humid)
        

