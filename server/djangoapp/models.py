# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    # Field for the name of the car make
    name = models.CharField(max_length=100, unique=True)
    # Field for a brief description of the car make
    description = models.TextField(blank=True, null=True)
    # You can add any other fields as needed
    established_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1886)],  # The first automobile was created in 1886
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class CarModel(models.Model):
    # Many-To-One relationship with CarMake
    car_make = models.ForeignKey(CarMake, related_name='car_models', on_delete=models.CASCADE)
    # Name of the car model
    name = models.CharField(max_length=100)
    # Type of car model with limited choices
    CAR_TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        # Add more choices as per requirement
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    # Year of the car model with constraints on values
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )
    # You can add additional fields as necessary
    color = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.car_make.name}"
