from django.contrib import admin

from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    #pass
    
    #shows fields to display in the admin table
    list_display = ['name', 'species', 'breed', 'age', 'sex']