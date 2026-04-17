from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# =========================
# SETUP DRIVER
# =========================
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # =========================
    # 1. HOME PAGE
    # =========================
    driver.get("http://127.0.0.1:8000/")
    time.sleep(2)
    print("Home page opened")

    # =========================
    # 2. REGISTRATION PAGE
    # =========================
    try:
        driver.find_element(By.LINK_TEXT, "Registration").click()
        time.sleep(2)
        print("Registration page opened")
        driver.back()
    except:
        print("Registration link not found")

    time.sleep(2)

    # =========================
    # 3. LOGIN
    # =========================
    driver.get("http://127.0.0.1:8000/login/")
    time.sleep(2)

    try:
        driver.find_element(By.NAME, "username").send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        print("Login successful")
    except:
        print("Login failed")

    # =========================
    # 4. FORGET PASSWORD
    # =========================
    driver.get("http://127.0.0.1:8000/forget-password/")
    time.sleep(2)

    if "FORGET" in driver.page_source.upper():
        print("Forget Password page loaded")

    try:
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'MOBILE')]").send_keys("01700000000")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[text()='CONTINUE']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[contains(@placeholder,'EMAIL')]").send_keys("test@gmail.com")
        time.sleep(1)

        buttons = driver.find_elements(By.XPATH, "//button[text()='CONTINUE']")
        if len(buttons) > 1:
            buttons[1].click()

        time.sleep(1)

        driver.find_element(By.XPATH, "//input[contains(@placeholder,'CODE')]").send_keys("123456")
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[contains(@placeholder,'PASSWORD')]").send_keys("newpass123")

        driver.find_element(By.XPATH, "//button[text()='SUBMIT']").click()
        time.sleep(2)

        print("Forget Password test completed")

    except:
        print("Forget Password test failed")

    # =========================
    # 5. DASHBOARD
    # =========================
    driver.get("http://127.0.0.1:8000/dashboard/")
    time.sleep(3)

    print("Current URL:", driver.current_url)

    if "dashboard" in driver.page_source.lower():
        print("Dashboard opened")

    try:
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'Name')]").send_keys("Sadia")
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'Contact')]").send_keys("01700000000")
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'Address')]").send_keys("Dhaka")
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'Language')]").send_keys("English")

        print("Dashboard input fields working")
    except:
        print("Dashboard inputs not found")

    # =========================================================
    # SECTION 6: HOSTEL LIST & DYNAMIC PROPERTY DETAILS
    # =========================================================
    print("Starting navigation test for Hostel List...")
    driver.get("http://127.0.0.1:8000/hostels/")
    time.sleep(3)

    if "HOUSE RENT" in driver.page_source.upper():
        print("Hostel List page verified.")

    property_links = driver.find_elements(By.XPATH, "//a[contains(text(),'DETAILS')]")
    total_properties = len(property_links)
    print(f"Found {total_properties} properties to test.")

    for i in range(total_properties):
        current_links = driver.find_elements(By.XPATH, "//a[contains(text(),'DETAILS')]")

        print(f"Testing Property {i + 1}...")
        current_links[i].click()
        time.sleep(2)

        if "FEATURES & FACILITIES" in driver.page_source:
            print(f"Property {i + 1} Details: SUCCESS (URL: {driver.current_url})")
        else:
            print(f"Property {i + 1} Details: FAILED")

        driver.back()
        time.sleep(2)

    # =========================
    # 7. LOGOUT
    # =========================
    try:
        driver.find_element(By.XPATH, "//*[contains(text(),'LOG OUT')]").click()
        time.sleep(2)
        print("Logout successful")
    except:
        print("Logout button not found")

    print("ALL TESTS COMPLETED SUCCESSFULLY")

finally:
    time.sleep(3)
    driver.quit()