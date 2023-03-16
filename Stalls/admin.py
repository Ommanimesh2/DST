from django.contrib import admin
from .models import Stalls

class AdminProduct(admin.ModelAdmin):
    list_display= ['Stalltopic']

admin.site.register(Stalls)