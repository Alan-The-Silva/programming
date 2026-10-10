import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    new = datetime.datetime.now()
    return render(request, "newyear/index.html", {
       "newyear":new.month == 1 and new.day == 1
    })