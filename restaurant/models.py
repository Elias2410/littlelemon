from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(
        validators=[
            MaxValueValidator(6),
            MinValueValidator(0)
        ]
    )
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.Name
    
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    Inventory = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    
    def __str__(self):
        return self.Title