from django.contrib import admin
from .models import Renting

class AdminProduct(admin.ModelAdmin):
    list_display= ['JobTitle' ]

admin.site.register()
