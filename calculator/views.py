# what season it is
# temp 

# srtructure from mars.py

# Utilities
from datetime import datetime
import requests
from django.shortcuts import render

def clac_weight(request):
    """
    request is the users weight in lbs
    """
    # mars gravity / earth gravity (m/s^2)
    weight = request * (3.721 / 9.807)

    return render(request, 'calc.html', {'weight': weight})


def calc_age(request):
    """
    function for how old you are in mars years (sols?)
    request is the users age in earth years
    """
    # earth days in a year / mars days in a year
    age = request * (365 / 687)

    return render(request, 'calc.html', {'age': age})


def calc_jump(request):
    """
    request is how high the user can jump in inches
    """

    jump = request + request * .625

    return render(request, 'calc.html', {'jump': jump})
