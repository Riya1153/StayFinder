from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name or self.email or "Owner"


class Hostel(models.Model):
    GENDER_CHOICES = [('G', 'Girls'), ('B', 'Boys')]

    title = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=255, blank=True)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    stars = models.IntegerField(default=5)

    has_wifi = models.BooleanField(default=True)
    has_cctv = models.BooleanField(default=True)
    has_food = models.BooleanField(default=False)
    has_cleaning = models.BooleanField(default=True)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='hostels/', null=True, blank=True)

    def __str__(self):
        return self.title or "Hostel"


class House(models.Model):
    title = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=255, blank=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rooms = models.IntegerField(default=1)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='houses/', null=True, blank=True)

    def __str__(self):
        return self.title or "House"


class UserProfile(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.full_name or self.email or "User Profile"


class BookingRequest(models.Model):
    property_for = models.CharField(max_length=50, blank=True)
    property_type = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)

    tenant_type = models.CharField(max_length=100, blank=True)
    monthly_rent_min = models.CharField(max_length=100, blank=True)
    monthly_rent_max = models.CharField(max_length=100, blank=True)
    room_type = models.CharField(max_length=100, blank=True)
    gender_requirement = models.CharField(max_length=100, blank=True)
    roommate_characteristics = models.TextField(blank=True)

    def __str__(self):
        return self.property_for or self.property_type or "Booking Request"


class RequirementAlert(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    mobile_no = models.CharField(max_length=20, blank=True)
    requirement = models.TextField(blank=True)

    def __str__(self):
        return self.name or self.email or "Requirement Alert"


class ApplicationForm(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    check_in_date = models.CharField(max_length=50, blank=True, null=True)
    number_of_roommates = models.CharField(max_length=50, blank=True, null=True)
    stay_duration = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    parent_phone_number = models.CharField(max_length=20, blank=True, null=True)
    nid_or_passport = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact = models.CharField(max_length=20, blank=True, null=True)
    copy_id_number = models.CharField(max_length=100, blank=True, null=True)
    draft_email_address = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name or self.email or "Application Form"


class PaymentFeedback(models.Model):
    payment_method = models.CharField(max_length=50, blank=True)
    rating = models.CharField(max_length=20, blank=True)
    complaint = models.TextField(blank=True)

    def __str__(self):
        return self.payment_method or "Payment Feedback"