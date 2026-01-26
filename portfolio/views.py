from django.shortcuts import render
from .models import Home, Skill, Project, Education, AboutSection

def home(request):
    home_data = Home.objects.first()
    skills = Skill.objects.all().order_by('category')
    projects = Project.objects.all().order_by('-created_at')
    education = Education.objects.all()
    context = {
        'home': home_data,
        'skills': skills,
        'projects': projects,
        'education': education
    }
    return render(request, 'portfolio/home.html', context)

from .forms import ContactForm
from django.shortcuts import redirect

def about(request):
    home_data = Home.objects.first()
    sections = AboutSection.objects.all().order_by('order')
    return render(request, 'portfolio/about.html', {
        'home': home_data,
        'sections': sections
    })

def contact(request):
    home_data = Home.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {'form': form, 'home': home_data})