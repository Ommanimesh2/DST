from django.contrib import admin
from .models import Jobs

class AdminProduct(admin.ModelAdmin):
    list_display= ['JobTitle' ]

admin.site.register(Jobs)
