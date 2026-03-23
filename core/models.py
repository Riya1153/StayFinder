from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Hostel(models.Model):
    GENDER_CHOICES = [('G', 'Girls'), ('B', 'Boys')]

    title = models.CharField(max_length=200)  # Ex: Matrichaya Hostel
    location = models.CharField(max_length=255)  # Ex: Uttara, Dhaka
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)  # 3500 BDT
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    stars = models.IntegerField(default=5)

    # Facilities (Figma Page 6)
    has_wifi = models.BooleanField(default=True)
    has_cctv = models.BooleanField(default=True)
    has_food = models.BooleanField(default=False)
    has_cleaning = models.BooleanField(default=True)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hostels/', null=True, blank=True)

    def __str__(self):
        return self.title