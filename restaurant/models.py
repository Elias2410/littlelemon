from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

# Create your models here.
class Booking(models.Model):
    Phone_Regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be a 10-digit number, start with 05..."
    )
    Name = models.CharField(max_length=255)
    PhoneNumber = models.CharField(
        max_length=10,
        validators=[Phone_Regex],
        blank=True
    )
    NoOfGusts = models.IntegerField(
        validators=[
            MaxValueValidator(6),
            MinValueValidator(0)
        ]
    )
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.Name + " - " + self.PhoneNumber + " - " + str(self.NoOfGusts) + " Gusts"
    
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