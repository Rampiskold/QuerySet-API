
from django.shortcuts import render
from .forms import *


def hotel(request):
    form = HotelForm(request.POST or None)
    # return render(request, 'hotel/hotel.html', locals())

