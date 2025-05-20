from django.db import models

# Create your models here.
class Booking(models.Model) :
    name = models.CharField(max_length=225)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
    def __str__(self) :
        return f"{self.name} - {self.booking_date}"


class Menu(models.Model) :
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) :
        return f"{self.title} - ${self.price}"