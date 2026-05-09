from django.db import models
from django.contrib.auth.models import User


class Owner(models.Model):
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    password = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name or self.email or "Owner"




class Hostel(models.Model):
    GENDER_CHOICES = [('G', 'Girls'), ('B', 'Boys')]
    title = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=255, blank=True)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    room_details = models.CharField(max_length=255, blank=True, null=True, help_text="e.g. 3-Bed Sharing (Spacious Room)")
    meal_plan = models.TextField(blank=True, null=True, help_text="Describe the meal system and menu")
    facilities_list = models.TextField(blank=True, null=True, help_text="Enter other facilities (one per line)")

    # This ForeignKey now works because Owner is properly defined
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='hostels/', null=True, blank=True)

    def __str__(self):
        return self.title or "Hostel"

class BoysHostel(Hostel):
    class Meta:
        proxy = True
        verbose_name = "Boys Hostel"
        verbose_name_plural = "Boys Hostel List"

class GirlsHostel(Hostel):
    class Meta:
        proxy = True
        verbose_name = "Girls Hostel"
        verbose_name_plural = "Girls Hostel List"

class House(models.Model):
    title = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=255, blank=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rooms = models.IntegerField(default=1)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='houses/', null=True, blank=True)
    facilities = models.TextField(help_text="Enter facilities separated by commas", blank=True, null=True)

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



class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, blank=True, null=True)
    # This stores the plain text for your admin view
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


from django.db import models


class Application(models.Model):
    # Links to both models (one will be empty depending on the booking)
    house = models.ForeignKey('House', on_delete=models.CASCADE, related_name='applications', null=True, blank=True)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE, related_name='applications', null=True, blank=True)


    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    check_in_date = models.DateField()
    roommates_count = models.IntegerField(default=0)
    stay_duration = models.CharField(max_length=100)


    current_address = models.TextField()
    own_phone = models.CharField(max_length=20)
    guardian_phone = models.CharField(max_length=20)
    nid_number = models.CharField(max_length=50)


    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        property_title = self.house.title if self.house else self.hostel.title
        return f"Application from {self.full_name} for {property_title}"



class PaymentFeedback(models.Model):
    PAYMENT_CHOICES = [
        ('CASH', 'Cash'),
        ('BKASH', 'bKash'),
        ('ATM', 'ATM'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    rating = models.IntegerField(default=0)
    complaint = models.TextField(blank=True, null=True)


    def __str__(self):
        user_email = self.user.email if self.user else "Guest"
        return f"{user_email} - {self.payment_method}"