from django.test import TestCase, Client
from django.urls import reverse
from core.models import Hostel  # Replace 'core' with your actual app name if different

class StayFinderLogicTests(TestCase):
    def setUp(self):
        # Client handles the requests without needing a running server
        self.client = Client()

    # =========================================================
    # 1. PAGE LOAD & TEMPLATE TESTS (Status 200)
    # =========================================================
    def test_main_pages_status_and_templates(self):
        """Verify pages load AND use the correct HTML templates"""
        pages = {
            'front_page': 'front_page.html',
            'registration': 'registration.html',
            'login': 'login.html',
            'add_hostel': 'add_hostel.html',
            'dashboard': 'dashboard.html',
            'hostel_list': 'hostel_list.html',
            'boys_hostel': 'boys_hostel.html',
            'girls_hostel': 'girls_hostel.html',
            'searching_sector': 'searching_sector.html',
            'search_page': 'search.html',
            'requirement': 'requirement.html',
            'payment_process': 'payment_process.html',
            'payment_method': 'payment_method.html'
        }
        for name, template in pages.items():
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 200, f"Page {name} failed to load!")
            self.assertTemplateUsed(response, template, f"Page {name} used wrong template!")

    # =========================================================
    # 2. DYNAMIC CONTENT & CONTEXT TESTS
    # =========================================================
    def test_property_details_content(self):
        """Test that property details load the correct ID and specific HTML text"""
        for test_id in [1, 4, 7]:  # Test a House, a Boy's Hostel, and a Girl's Hostel
            url = reverse('property_details', args=[test_id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['id'], test_id)
            self.assertContains(response, "FEATURES & FACILITIES")

    def test_searching_sector_form_context(self):
        """Check if the search form is present in the context"""
        response = self.client.get(reverse('searching_sector'))
        self.assertIn('form', response.context)

    # =========================================================
    # 3. REDIRECT LOGIC TESTS (POST Requests)
    # =========================================================
    def test_dashboard_redirect_flow(self):
        """POST to dashboard should redirect to search_page"""
        response = self.client.post(reverse('dashboard'), {
            'name': 'Test User',
            'email': 'test@example.com'
        })
        self.assertRedirects(response, reverse('search_page'))

    def test_requirement_submission_flow(self):
        """POST to requirement should redirect back to search_page"""
        data = {
            'name': 'Student A',
            'requirement': 'Need a room in Mirpur'
        }
        response = self.client.post(reverse('requirement'), data)
        self.assertRedirects(response, reverse('search_page'))

    def test_complete_payment_sequence(self):
        """Test the full sequence of redirects in the payment system"""
        # Step 1: Process
        step1 = self.client.post(reverse('payment_process'), {'nid': '12345'})
        self.assertRedirects(step1, reverse('payment_method'))

        # Step 2: Method
        step2 = self.client.post(reverse('payment_method'), {'method': 'bkash'})
        self.assertRedirects(step2, reverse('search_page'))

    # =========================================================
    # 4. EDGE CASES & SECURITY TESTS
    # =========================================================
    def test_404_on_non_existent_page(self):
        """Verify that an invalid URL returns a 404 error"""
        response = self.client.get('/this-page-does-not-exist/')
        self.assertEqual(response.status_code, 404)

    def test_property_details_invalid_type(self):
        """Verify that property details fails if the ID is not an integer"""
        from django.urls import NoReverseMatch
        with self.assertRaises(NoReverseMatch):
            reverse('property_details', args=['abc'])

    def test_dashboard_methods(self):
        """Check if dashboard accepts both GET and POST"""
        # Test GET
        get_res = self.client.get(reverse('dashboard'))
        self.assertEqual(get_res.status_code, 200)
        # Test POST
        post_res = self.client.post(reverse('dashboard'))
        self.assertEqual(post_res.status_code, 302)

    # =========================================================
    # 5. HTML CONTENT VALIDATION
    # =========================================================
    def test_front_page_branding(self):
        """Check if the site brand name 'StayFinder' appears on the homepage"""
        response = self.client.get(reverse('front_page'))
        # Using string check instead of assertContains for specific headers
        self.assertContains(response, "StayFinder")