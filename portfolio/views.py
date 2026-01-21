from django.shortcuts import render
from .models import Home

def home(request):
    home_data = Home.objects.first()
    context = {'home': home_data}
    return render(request, 'portfolio/home.html', context)