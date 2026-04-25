from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Hostel(models.Model):
    GENDER_CHOICES = [('G', 'Girls'), ('B', 'Boys')]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    stars = models.IntegerField(default=5)

    # Facilities
    has_wifi = models.BooleanField(default=True)
    has_cctv = models.BooleanField(default=True)
    has_food = models.BooleanField(default=False)
    has_cleaning = models.BooleanField(default=True)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hostels/', null=True, blank=True)

    def __str__(self):
        return self.title

class House(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.IntegerField(default=1)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='houses/', null=True, blank=True)

    def __str__(self):
        return self.title