from django.contrib import admin
from .models import *                # or from .models import "ModuleName" 

# Register your models here.
admin.site.register(Module_Name) 

# Changing the Django Admin Header Text
admin.site.site_header = 'Project Name'    
