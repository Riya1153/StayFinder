from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Driver
driver = webdriver.Chrome()

try:
    # 1. Open the specific property details page
    # Using the ID from your screenshot (property-details/4/)
    print("Navigating to Unique Boy's Hostel Details...")
    driver.get("http://127.0.0.1:8000/property-details/4/")
    driver.maximize_window()
    time.sleep(2)

    # 2. Verify Title
    title = driver.find_element(By.TAG_NAME, "h1").text
    if "UNIQUE BOY'S HOSTEL" in title:
        print(f"PASS: Title verified -> {title}")

    # 3. Verify Owner and Location
    owner = driver.find_element(By.XPATH, "//*[contains(text(), 'UNIQUE HOSTEL MANAGEMENT')]")
    location = driver.find_element(By.XPATH, "//*[contains(text(), 'Farmgate, Dhaka')]")
    print(f"PASS: Owner ({owner.text}) and Location ({location.text}) are correct.")

    # 4. Verify Specific Facilities (The Checkmark List)
    facilities_to_check = [
        "Walking distance from Farmgate Bus Stand",
        "Biometric Attendance System",
        "Indoor Games Room",
        "Weekly Special Lunch"
    ]

    print("Checking Features & Facilities...")
    for item in facilities_to_check:
        try:
            element = driver.find_element(By.XPATH, f"//*[contains(text(), '{item}')]")
            print(f" - Found Facility: {item}")
        except:
            print(f" - MISSING Facility: {item}")

    # 5. Verify Buttons
    book_now = driver.find_element(By.XPATH, "//button[contains(text(), 'BOOK NOW')]")
    back_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'BACK TO LIST')]")

    if book_now.is_displayed() and back_btn.is_displayed():
        print("PASS: Navigation and Booking buttons are visible.")

except Exception as e:
    print(f"An error occurred during testing: {e}")


try:
    print("\nNavigating to BOYS-STAY Details...")
    driver.get("http://127.0.0.1:8000/property-details/5/")
    driver.maximize_window()
    time.sleep(2)

    # Verify Title
    title = driver.find_element(By.TAG_NAME, "h1").text
    if "BOYS-STAY" in title:
        print(f"PASS: Title verified -> {title}")

    # Verify Owner and Location
    owner = driver.find_element(By.XPATH, "//*[contains(text(), 'STAY SOLUTIONS LTD')]")
    location = driver.find_element(By.XPATH, "//*[contains(text(), 'Mirpur 2, Dhaka')]")
    print(f"PASS: Owner and Location are correct.")

    # Verify Specific Facilities
    facilities_to_check = [
        "Near Mirpur Stadium",
        "Personal Storage Lockers",
        "Paid Laundry Service",
        "24-hour Front Desk Assistance"
    ]

    print("Checking Features & Facilities...")
    for item in facilities_to_check:
        try:
            driver.find_element(By.XPATH, f"//*[contains(text(), '{item}')]")
            print(f" - Found Facility: {item}")
        except:
            print(f" - MISSING Facility: {item}")

    # Verify Buttons
    book_now = driver.find_element(By.CLASS_NAME, "book-now-btn")
    if book_now.is_displayed():
        print("PASS: Book Now button is visible.")

except Exception as e:
    print(f"Error on BOYS-STAY: {e}")


try:
    print("\nNavigating to GHAR-AANGAN HOSTEL Details...")
    driver.get("http://127.0.0.1:8000/property-details/6/")
    time.sleep(2)

    # Verify Title
    title = driver.find_element(By.TAG_NAME, "h1").text
    if "GHAR-AANGAN HOSTEL" in title:
        print(f"PASS: Title verified -> {title}")

    # Verify Owner and Location
    owner = driver.find_element(By.XPATH, "//*[contains(text(), 'DHAKA LIVING CO.')]")
    location = driver.find_element(By.XPATH, "//*[contains(text(), 'Bashundhara R/A, Dhaka')]")
    print(f"PASS: Owner and Location are correct.")

    # Verify Specific Facilities
    facilities_to_check = [
        "Premium Study Environment",
        "Shared Living Area with TV",
        "Ironing Facilities",
        "Solar Power Backup"
    ]

    print("Checking Features & Facilities...")
    for item in facilities_to_check:
        try:
            driver.find_element(By.XPATH, f"//*[contains(text(), '{item}')]")
            print(f" - Found Facility: {item}")
        except:
            print(f" - MISSING Facility: {item}")

except Exception as e:
    print(f"Error on GHAR-AANGAN: {e}")

finally:
    time.sleep(2)
    driver.quit()
    print("Test for  Boy's Hostel Completed.")