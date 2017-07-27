#!/usr/bin/env python3
import sys
import csv
from helperfunctions import months
from extremefinder import ExtremeFinder
from calculatoravg import AverageCalculator
from bargraph import GraphBar

filename = "lahore_weather_"

if(len(sys.argv) < 4 ):
    print("error")
    sys.exit()

path= sys.argv[3]

if sys.argv[1] == "-e":
    year=sys.argv[2]
    ext_finder = ExtremeFinder()
    for num, month in months.items():
        data_file_name= ("%s%s%s_%s.txt" %(path, filename , year, month[0]))
        ext_finder.extreme_search(data_file_name)
    ext_finder.report("-e")

elif sys.argv[1] == "-a":
    year, month = sys.argv[2].split("/")
    avg_calculator = AverageCalculator()
    data_file_name= ("%s%s%s_%s.txt" %(path, filename , year, months[int(month)][0]))
    avg_calculator.calculate_avg(data_file_name)
    avg_calculator.report()
     
elif sys.argv[1] == "-c":
    year, month = sys.argv[2].split("/")
    graph_drawer = GraphBar()
    data_file_name = ("%s%s%s_%s.txt" %(path, filename , year, months[int(month)][0]))
    graph_drawer.draw_graph(data_file_name)
