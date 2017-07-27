#!/usr/bin/env python3
import csv
from termcolor import colored, cprint
from helperfunctions import display

class GraphBar:

    def __init__(self):
        self.graph=""
        self.count= 1
    
    def draw_graph(self,data_file_name):
        with open(data_file_name, "r") as data_file:
            reader= csv.reader(data_file)
            next(reader)
            extractor = csv.DictReader(data_file, dialect="unix", delimiter= "," , quoting= csv.QUOTE_NONE)
            for row in extractor:
                self.graph= ""
                if row["Max TemperatureC"] and row["Min TemperatureC"]:
                    for x in range(int(row["Max TemperatureC"])):
                        if x < int(row["Min TemperatureC"]):
                            self.graph += colored("+","blue")
                            continue
                        else:
                            self.graph += colored("+", "red")
                    display("-c",self.count,self.graph, int(row["Min TemperatureC"]), int(row["Max TemperatureC"]) ) 
                self.count += 1
