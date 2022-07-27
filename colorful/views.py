from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request, 'colorful/home.html')


def colorize(request):
    color = request.POST['color-name']
    return render(request, 'colorful/color.html', {'color': color})


