from django import forms

class BookingSearchForm(forms.Form):
    # The 3 Bubbles (Category Selector)
    CATEGORY_CHOICES = [('buy', 'Buy'), ('rent', 'Rent'), ('roommates', 'Roommates')]
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.RadioSelect,
        initial='buy'
    )

    # --- COMMON FIELDS (Used in multiple boxes) ---
    city = forms.ChoiceField(
        choices=[('dhaka', 'Dhaka')],
        initial='dhaka',
        required=False
    )
    location = forms.ChoiceField(
        choices=[('any', 'Any'), ('bashundhara', 'Bashundhara R/A'), ('uttara', 'Uttara'), ('dhanmondi', 'Dhanmondi')],
        required=False
    )

    # --- DROP DOWN DATA FOR BUY ---
    buy_property = forms.ChoiceField(choices=[('1', 'APARTMENT'), ('2', 'FLAT')], required=False)
    size_sqft = forms.ChoiceField(choices=[
        ('any', 'Any'), ('<900', 'Less than 900 sqft'), ('901-1100', '901 to 1100 sqft'),
        ('1101-1400', '1101 to 1400 sqft'), ('1401-1800', '1401 to 1800 sqft')
    ], required=False)
    buy_price = forms.ChoiceField(choices=[
        ('any', 'Any Price'), ('50l', 'Under 50 Lac'), ('1c', '50 Lac - 1 Crore'), ('above', 'Above 1 Crore')
    ], required=False)

    # --- DROP DOWN DATA FOR RENT ---
    rent_property = forms.ChoiceField(choices=[('1', 'APARTMENT'), ('2', 'FLAT'), ('3', 'SUBLET')], required=False)
    tenant_type = forms.ChoiceField(choices=[('1', 'FAMILY'), ('2', 'FEMALE'), ('3', 'MALE')], required=False)
    # Rent uses dropdowns for Min/Max based on your design
    rent_min = forms.ChoiceField(choices=[('min', 'Min'), ('5000', '5000'), ('10000', '10000'), ('20000', '20000')], required=False)
    rent_max = forms.ChoiceField(choices=[('max', 'Max'), ('10000', '10000'), ('30000', '30000'), ('50000', '50000')], required=False)

    # --- DROP DOWN DATA FOR ROOMMATES ---
    res_type = forms.ChoiceField(choices=[('1', 'COMMERCIAL MESS'), ('2', 'INDEPENDENT MESS'), ('3', 'HOSTEL')], required=False)
    room_type = forms.ChoiceField(choices=[('1', '2 Person'), ('2', '3 Person'), ('3', '4 Person')], required=False)
    gender = forms.ChoiceField(choices=[('1', 'FEMALE'), ('2', 'MALE')], required=False)

    # NEW: Monthly Rent for Roommates
    roommate_rent = forms.ChoiceField(choices=[
        ('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('5000', '5000'), ('above', 'Above 20000')
    ], required=False)

    # NEW: Roommates Characteristics (Requirement box)
    characteristics = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'e.g. Non-smoker, Student, etc.',
            'style': 'width: 100%; height: 60px; border-radius: 5px;'
        })
    )