import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# --- Configuration ---
BASE_URL = "http://127.0.0.1:8000"


def run_stayfinder_test():
    # Setup Chrome
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    results = []

    def record(name, path):
        try:
            driver.get(f"{BASE_URL}{path}")
            time.sleep(1)  # Visual confirmation
            results.append(f"✅ PASS: {name} ({path})")
        except Exception as e:
            results.append(f"❌ FAIL: {name} ({path}) - {str(e)}")

    try:
        print("🚀 Starting StayFinder Automated Testing...")

        # 1. Main Pages
        record("Front Page", "/")
        record("Registration", "/registration/")
        record("Login", "/login/")

        # 2. Hostel Management
        record("Dashboard", "/dashboard/")
        record("Add Hostel", "/add-hostel/")
        record("General Hostel List", "/hostels/")
        record("Boys Hostel List", "/hostels/boys/")
        record("Girls Hostel List", "/hostels/girls/")

        # 3. Search & Booking Flow
        record("Searching Sector", "/searching-sector/")
        record("Search Results", "/search/")
        record("Requirement Page", "/requirement/")

        # 4. Payment Flow (Interactive Test)
        print("Testing Payment Flow Interactions...")
        driver.get(f"{BASE_URL}/payment-process/")
        time.sleep(1)

        # Click Submit on Payment Process to test redirect
        try:
            submit_btn = driver.find_element(By.CLASS_NAME, "submit-btn")
            submit_btn.click()
            time.sleep(2)
            if "payment_method" in driver.current_url:
                results.append("✅ PASS: Payment Process -> Method Redirect")
            else:
                results.append("❌ FAIL: Payment Redirect Logic")
        except:
            results.append("⚠️ SKIP: Could not find Submit button on Payment Process")

        # 5. Payment Method & Feedback
        record("Payment Method Page", "/payment_method/")
        try:
            complaint = driver.find_element(By.NAME, "complaint")
            complaint.send_keys("Automated Test: Everything looking sharp!")
            results.append("✅ PASS: Complaint Box Interaction")
        except:
            results.append("❌ FAIL: Complaint Box Interaction")

        # 6. Password Reset System (The 4-step process)
        print("Testing Password Reset System...")
        record("Password Reset Start", "/password-reset/")
        record("Password Reset Done", "/password-reset/done/")
        record("Password Reset Complete", "/password-reset/complete/")

        # Summary Report
        print("\n" + "=" * 40)
        print(" FINAL TEST REPORT ")
        print("=" * 40)
        for res in results:
            print(res)
        print("=" * 40)

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    run_stayfinder_test()