from django.test import TestCase, Client
from django.urls import reverse, resolve
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