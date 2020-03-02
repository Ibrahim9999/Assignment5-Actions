import math
from datetime import date

def firstrun():
    return "success"

def area(radius):
    return math.pi*radius*radius

def firstlast(list):
    return list[0], list[len(list) - 1]

def days(date1, date2):
    return (date1 - date2).days