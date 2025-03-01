from django.contrib import admin
from .models import CarMake, CarModel

# Inline class to manage CarModel entries within CarMake
class CarModelInline(admin.TabularInline): 
    model = CarModel  # Specify the model to be used as inline
    extra = 1  # Number of empty forms to display for adding new car models

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'car_make', 'type')  # Fields to display in the admin list view
    list_filter = ('year', 'car_make', 'type')  # Filter options for the admin list view
    search_fields = ('name',)  # Searchable fields in the admin interface

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'established_year', 'description')  # Fields to display in the admin list view
    search_fields = ('name',)  # Searchable fields for CarMake
    inlines = [CarModelInline]  # Use inline class to manage CarModels with CarMake

# Registering models with their respective admin configurations
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
