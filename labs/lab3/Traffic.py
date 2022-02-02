"""
Dylan Benton Embrey
2/1/2022
Traffic.py
Computer Programming Labs 3: Traffic
Problem: This code will help show the average number of vehicles on the road per day, number of vehicles for all roads,
and the average number of vehicles per road.
This is my work.
"""
import math


def traffic():
    roads_surveyed = eval(input("How many roads were surveyed?"))
    total_num_cars = 0
    cars_per_day = 0
    for i in range(roads_surveyed):
        print("How many days was road", i + 1, "surveyed? ")
        days_surveyed = eval(input(""))
        cars_per_road = 0
        for j in range(days_surveyed):
            print("How many cars traveled on day", j + 1, "? ")
            cars_per_day = eval(input(""))
            total_num_cars = cars_per_day + total_num_cars
            cars_per_road = cars_per_road + cars_per_day
        sum_cars = (cars_per_road / days_surveyed)
        print("Road", i + 1, "average vehicles per day:", sum_cars)
    average_total = (total_num_cars / roads_surveyed)
    print("Total number of vehicles traveled on all roads:", total_num_cars)
    print("Average number of vehicles per road:", average_total)


traffic()
