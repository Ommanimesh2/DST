from django.contrib import admin
from .models import Renting,Orders,query

class AdminProduct(admin.ModelAdmin):
    list_display= ['Name' , 'payement_mode']

admin.site.register(Renting)
admin.site.register(Orders)
admin.site.register(query)