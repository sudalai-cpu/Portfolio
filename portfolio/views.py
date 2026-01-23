from django.shortcuts import render
from .models import Home, Skill, Project, Education

def home(request):
    home_data = Home.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all().order_by('-created_at')
    education = Education.objects.all()
    context = {
        'home': home_data,
        'skills': skills,
        'projects': projects,
        'education': education
    }
    return render(request, 'portfolio/home.html', context)