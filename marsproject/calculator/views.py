# what season it is
# temp 

# srtructure from mars.py

# Utilities
from datetime import datetime
import requests
from rest_framework.decorators import action
from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from .forms import CalculateMars


def calculate(request):
    form = CalculateMars
    if request.method == 'POST':
        form = CalculateMars(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            data = {'age': calc_age(age), 'weight': calc_weight(weight)}
            return render(request, 'calculator.html', {'data': data})

    return render(request, 'calculator.html', {'form': form})


def calc_weight(w):
    """
    request is the users weight in lbs
    """
    # mars gravity / earth gravity (m/s^2)
    weight = w * (3.721 / 9.807)

    return str(round(weight, 2))


def calc_age(a):
    """
    function for how old you are in mars years (sols?)
    request is the users age in earth years
    """
    # earth days in a year / mars days in a year
    age = a * (365 / 687)

    return str(round(age, 2))

def calc_jump(j):
    """
    request is how high the user can jump in inches
    """

    jump = j + j * .625

    return jump
