from django.test import TestCase, Client
from django.urls import reverse, resolve
from .forms import BookingSearchForm
from core.models import Owner, Hostel
from core.views import (
    front_page, registration, login_view,
    forget_password, add_hostel, dashboard, hostel_list,
    property_details # <--- Ensure this is imported
)

# ================================================
# MODEL TEST — Owner
# ================================================
class OwnerModelTest(TestCase):
    def setUp(self):
        self.owner = Owner.objects.create(
            name="Rahim Uddin",
            phone="01711111111",
            email="rahim@example.com"
        )

    def test_01_owner_created(self):
        self.assertEqual(Owner.objects.count(), 1)

    def test_02_owner_name(self):
        self.assertEqual(self.owner.name, "Rahim Uddin")

    def test_03_owner_phone(self):
        self.assertEqual(self.owner.phone, "01711111111")

    def test_04_owner_email(self):
        self.assertEqual(self.owner.email, "rahim@example.com")

    def test_05_owner_str(self):
        self.assertEqual(str(self.owner), "Rahim Uddin")


# ================================================
# MODEL TEST — Hostel
# ================================================
class HostelModelTest(TestCase):
    def setUp(self):
        self.owner = Owner.objects.create(
            name="Test Owner",
            phone="01700000000",
            email="owner@test.com"
        )
        self.hostel = Hostel.objects.create(
            title="Matrichaya Hostel",
            location="Uttara, Dhaka",
            price_per_month=3500.00,
            gender="G",
            stars=5,
            has_wifi=True,
            has_cctv=True,
            has_food=False,
            has_cleaning=True,
            owner=self.owner
        )

    def test_06_hostel_created(self):
        self.assertEqual(Hostel.objects.count(), 1)

    def test_07_hostel_title(self):
        self.assertEqual(self.hostel.title, "Matrichaya Hostel")

    def test_08_hostel_location(self):
        self.assertEqual(self.hostel.location, "Uttara, Dhaka")

    def test_09_hostel_price(self):
        self.assertEqual(float(self.hostel.price_per_month), 3500.00)

    def test_10_hostel_gender(self):
        self.assertEqual(self.hostel.gender, "G")

    def test_11_hostel_stars(self):
        self.assertEqual(self.hostel.stars, 5)

    def test_12_hostel_wifi(self):
        self.assertTrue(self.hostel.has_wifi)

    def test_13_hostel_food_false(self):
        self.assertFalse(self.hostel.has_food)

    def test_14_hostel_str(self):
        self.assertEqual(str(self.hostel), "Matrichaya Hostel")

    def test_15_hostel_owner_linked(self):
        self.assertEqual(self.hostel.owner.name, "Test Owner")

    def test_16_owner_delete_cascades(self):
        self.owner.delete()
        self.assertEqual(Hostel.objects.count(), 0)


# ================================================
# URL TEST
# ================================================
class URLTest(TestCase):
    def test_17_front_page_url(self):
        self.assertEqual(resolve('/').func, front_page)

    def test_18_registration_url(self):
        self.assertEqual(resolve('/registration/').func, registration)

    def test_19_login_url(self):
        self.assertEqual(resolve('/login/').func, login_view)

    def test_20_forget_password_url(self):
        self.assertEqual(resolve('/forget-password/').func, forget_password)

    def test_21_dashboard_url(self):
        self.assertEqual(resolve('/dashboard/').func, dashboard)

    def test_22_hostel_list_url(self):
        self.assertEqual(resolve('/hostels/').func, hostel_list)


# ================================================
# VIEW TEST
# ================================================
class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_23_front_page_status(self):
        res = self.client.get(reverse('front_page'))
        self.assertEqual(res.status_code, 200)

    def test_24_front_page_template(self):
        res = self.client.get(reverse('front_page'))
        self.assertTemplateUsed(res, 'front_page.html')

    def test_25_registration_status(self):
        res = self.client.get(reverse('registration'))
        self.assertEqual(res.status_code, 200)

    def test_26_registration_template(self):
        res = self.client.get(reverse('registration'))
        self.assertTemplateUsed(res, 'registration.html')

    def test_27_login_status(self):
        res = self.client.get(reverse('login'))
        self.assertEqual(res.status_code, 200)

    def test_28_login_template(self):
        res = self.client.get(reverse('login'))
        self.assertTemplateUsed(res, 'login.html')

    def test_29_dashboard_status(self):
        res = self.client.get(reverse('dashboard'))
        self.assertEqual(res.status_code, 200)

    def test_30_unknown_url_404(self):
        res = self.client.get('/this-does-not-exist/')
        self.assertEqual(res.status_code, 404)


# =========================================================
# Hostel List & Property Details
# =========================================================

class HostelListViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_31_hostel_list_page_loads(self):
        url = reverse('hostel_list')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "MOONSCAPE")
        self.assertContains(res, "ARKAM KPLOTAN")
        self.assertContains(res, "Nagar Chayaneer")
        self.assertTemplateUsed(res, 'hostel_list.html')

class PropertyDetailsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_32_moonscape_details_load(self):
        url = reverse('property_details', args=[1])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "MOONSCAPE")
        self.assertContains(res, "FEATURES & FACILITIES")

    def test_33_arkam_details_load(self):
        url = reverse('property_details', args=[2])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "ARKAM KPLOTAN")

    def test_34_nagar_details_load(self):
        url = reverse('property_details', args=[3])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "NAGAR CHAYANEER")


# =========================================================
# SEARCHING SECTOR — URL TESTS
# =========================================================
class SearchingSectorURLTest(TestCase):

    def test_35_searching_sector_url_resolves(self):
        from core.views import searching_sector
        self.assertEqual(resolve('/searching-sector/').func, searching_sector)

    def test_36_search_results_url_resolves(self):
        from core.views import search_results
        self.assertEqual(resolve('/search-results/').func, search_results)

    def test_37_searching_sector_named_url(self):
        self.assertEqual(reverse('searching_sector'), '/searching-sector/')

    def test_38_search_results_named_url(self):
        self.assertEqual(reverse('search_results'), '/search-results/')


# =========================================================
# SEARCHING SECTOR — PAGE LOAD TESTS
# =========================================================
class SearchingSectorPageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_39_page_returns_200(self):
        res = self.client.get(reverse('searching_sector'))
        self.assertEqual(res.status_code, 200)

    def test_40_correct_template_used(self):
        res = self.client.get(reverse('searching_sector'))
        self.assertTemplateUsed(res, 'searching_sector.html')

    def test_41_page_contains_buy_option(self):
        res = self.client.get(reverse('searching_sector'))
        self.assertContains(res, 'Buy')

    def test_42_page_contains_rent_option(self):
        res = self.client.get(reverse('searching_sector'))
        self.assertContains(res, 'Rent')

    def test_43_page_contains_roommates_option(self):
        res = self.client.get(reverse('searching_sector'))
        self.assertContains(res, 'Roommates')

    def test_44_page_contains_tell_us_button(self):
       pyt res = self.client.get(reverse('searching_sector'))
        self.assertContains(res, 'Tell Us Your Requirement')

    def test_45_page_contains_manual_button(self):
        res = self.client.get(reverse('searching_sector'))
        self.assertContains(res, 'MANUAL')

    def test_46_page_contains_for_booking_banner(self):
        res = self.client.get(reverse('searching_sector'))
        self.assertContains(res, 'FOR BOOKING')


# =========================================================
# SEARCHING SECTOR — BUY CATEGORY TESTS
# =========================================================
class BuyCategorySearchTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('search_results')

    def test_47_buy_returns_200(self):
        res = self.client.get(self.url, {'category': 'buy'})
        self.assertEqual(res.status_code, 200)

    def test_48_buy_category_in_context(self):
        res = self.client.get(self.url, {'category': 'buy'})
        self.assertEqual(res.context['category'], 'buy')

    def test_49_buy_property_type_in_context(self):
        res = self.client.get(self.url, {'category': 'buy', 'property_type': 'Apartment/Flats'})
        self.assertEqual(res.context['property_type'], 'Apartment/Flats')

    def test_50_buy_size_in_context(self):
        res = self.client.get(self.url, {'category': 'buy', 'size': '1000 sqft to 1499 sqft'})
        self.assertEqual(res.context['size'], '1000 sqft to 1499 sqft')

    def test_51_buy_city_in_context(self):
        res = self.client.get(self.url, {'category': 'buy', 'city': 'Dhaka'})
        self.assertEqual(res.context['city'], 'Dhaka')

    def test_52_buy_location_in_context(self):
        res = self.client.get(self.url, {'category': 'buy', 'location': 'Dhanmondi'})
        self.assertEqual(res.context['location'], 'Dhanmondi')

    def test_53_buy_full_form(self):
        data = {'category': 'buy', 'property_type': 'Flat', 'size': 'Less than 500 sqft', 'city': 'Chittagong', 'location': 'Agrabad'}
        res = self.client.get(self.url, data)
        self.assertEqual(res.status_code, 200)
        for k, v in data.items():
            self.assertEqual(res.context[k], v)

    def test_54_buy_missing_optional_defaults_empty(self):
        res = self.client.get(self.url, {'category': 'buy'})
        self.assertEqual(res.context['location'], '')


# =========================================================
# SEARCHING SECTOR — RENT CATEGORY TESTS
# =========================================================
class RentCategorySearchTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('search_results')

    def test_55_rent_returns_200(self):
        res = self.client.get(self.url, {'category': 'rent'})
        self.assertEqual(res.status_code, 200)

    def test_56_rent_category_in_context(self):
        res = self.client.get(self.url, {'category': 'rent'})
        self.assertEqual(res.context['category'], 'rent')

    def test_57_rent_tenant_type_family(self):
        res = self.client.get(self.url, {'category': 'rent', 'tenant_type': 'Family'})
        self.assertEqual(res.context['tenant_type'], 'Family')

    def test_58_rent_tenant_type_female(self):
        res = self.client.get(self.url, {'category': 'rent', 'tenant_type': 'Female'})
        self.assertEqual(res.context['tenant_type'], 'Female')

    def test_59_rent_tenant_type_male(self):
        res = self.client.get(self.url, {'category': 'rent', 'tenant_type': 'Male'})
        self.assertEqual(res.context['tenant_type'], 'Male')

    def test_60_rent_price_min_in_context(self):
        res = self.client.get(self.url, {'category': 'rent', 'price_min': '10000'})
        self.assertEqual(res.context['price_min'], '10000')

    def test_61_rent_price_max_in_context(self):
        res = self.client.get(self.url, {'category': 'rent', 'price_max': '30000'})
        self.assertEqual(res.context['price_max'], '30000')

    def test_62_rent_full_form(self):
        data = {'category': 'rent', 'property_type': 'Sublet', 'tenant_type': 'Male', 'price_min': '15000', 'price_max': '35000'}
        res = self.client.get(self.url, data)
        self.assertEqual(res.status_code, 200)
        for k, v in data.items():
            self.assertEqual(res.context[k], v)

    def test_63_rent_price_lac_format(self):
        res = self.client.get(self.url, {'category': 'rent', 'price_min': '1 lac', 'price_max': '2 lac'})
        self.assertEqual(res.context['price_min'], '1 lac')
        self.assertEqual(res.context['price_max'], '2 lac')


# =========================================================
# SEARCHING SECTOR — ROOMMATES CATEGORY TESTS
# =========================================================
class RoommatesCategorySearchTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('search_results')

    def test_64_roommates_returns_200(self):
        res = self.client.get(self.url, {'category': 'roommates'})
        self.assertEqual(res.status_code, 200)

    def test_65_roommates_category_in_context(self):
        res = self.client.get(self.url, {'category': 'roommates'})
        self.assertEqual(res.context['category'], 'roommates')

    def test_66_roommates_commercial_mess(self):
        res = self.client.get(self.url, {'category': 'roommates', 'residence_type': 'Commercial Mess'})
        self.assertEqual(res.context['residence_type'], 'Commercial Mess')

    def test_67_roommates_independent_mess(self):
        res = self.client.get(self.url, {'category': 'roommates', 'residence_type': 'Independent Mess'})
        self.assertEqual(res.context['residence_type'], 'Independent Mess')

    def test_68_roommates_hostel(self):
        res = self.client.get(self.url, {'category': 'roommates', 'residence_type': 'Hostel'})
        self.assertEqual(res.context['residence_type'], 'Hostel')

    def test_69_roommates_room_type_2_person(self):
        res = self.client.get(self.url, {'category': 'roommates', 'room_type': '2 Person in One Room'})
        self.assertEqual(res.context['room_type'], '2 Person in One Room')

    def test_70_roommates_room_type_4_plus(self):
        res = self.client.get(self.url, {'category': 'roommates', 'room_type': '4+ Person in One Room'})
        self.assertEqual(res.context['room_type'], '4+ Person in One Room')

    def test_71_roommates_gender_female(self):
        res = self.client.get(self.url, {'category': 'roommates', 'gender': 'Female'})
        self.assertEqual(res.context['gender'], 'Female')

    def test_72_roommates_gender_male(self):
        res = self.client.get(self.url, {'category': 'roommates', 'gender': 'Male'})
        self.assertEqual(res.context['gender'], 'Male')

    def test_73_roommates_characteristics(self):
        res = self.client.get(self.url, {'category': 'roommates', 'characteristics': 'Non-smoker, quiet'})
        self.assertEqual(res.context['characteristics'], 'Non-smoker, quiet')

    def test_74_roommates_full_form(self):
        data = {'category': 'roommates', 'residence_type': 'Hostel', 'room_type': '3 Person in One Room', 'gender': 'Female', 'price_min': '3000', 'price_max': '10000', 'characteristics': 'Clean preferred'}
        res = self.client.get(self.url, data)
        self.assertEqual(res.status_code, 200)
        for k, v in data.items():
            self.assertEqual(res.context[k], v)


class BookingSectorTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('searching_sector')

    # Test 1: Check if the form is valid with correct data
    def test_form_validation(self):
        data = {
            'category': 'rent',
            'rent_property': '1',  # Apartment
            'tenant_type': '2',  # Female
            'rent_min': '10000',
            'rent_max': '20000'
        }
        form = BookingSearchForm(data=data)
        self.assertTrue(form.is_valid())

    # Test 2: Check if the page loads correctly
    def test_page_load(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "FOR BOOKING")  # Checks for your header

    # Test 3: Check default category
    def test_default_category(self):
        form = BookingSearchForm()
        self.assertEqual(form.fields['category'].initial, 'buy')class BookingSectorTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('searching_sector')

    # Test 1: Check if the form is valid with correct data
    def test_form_validation(self):
        data = {
            'category': 'rent',
            'rent_property': '1', # Apartment
            'tenant_type': '2',   # Female
            'rent_min': '10000',
            'rent_max': '20000'
        }
        form = BookingSearchForm(data=data)
        self.assertTrue(form.is_valid())

    # Test 2: Check if the page loads correctly
    def test_page_load(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "FOR BOOKING") # Checks for your header

    # Test 3: Check default category
    def test_default_category(self):
        form = BookingSearchForm()
        self.assertEqual(form.fields['category'].initial, 'buy')

