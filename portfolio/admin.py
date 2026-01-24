from django.contrib import admin

from .models import Home, Skill, Category, Project, Education, Contact

# Register your models here.
admin.site.register(Home)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Contact)
