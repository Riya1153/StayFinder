from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Driver
driver = webdriver.Chrome()

def run_girls_hostel_tests():
    try:
        # --- TEST 1: MATRICHAYA GIRL'S HOSTEL (ID: 7) ---
        print("Navigating to MATRICHAYA GIRL'S HOSTEL Details...")
        driver.get("http://127.0.0.1:8000/property-details/7/")
        driver.maximize_window()
        time.sleep(2)

        # Verify Title
        title = driver.find_element(By.TAG_NAME, "h1").text
        if "MATRICHAYA GIRL'S HOSTEL" in title:
            print(f"PASS: Title verified -> {title}")

        # Verify Owner and Location
        owner = driver.find_element(By.XPATH, "//*[contains(text(), 'MATRICHAYA PROPERTIES')]")
        location = driver.find_element(By.XPATH, "//*[contains(text(), 'Azimpur, Dhaka')]")
        print(f"PASS: Owner ({owner.text}) and Location ({location.text}) are correct.")

        # Verify Facilities
        facilities_7 = ["Strict In-out Entry Log", "Professional Female Warden", "Close to Azimpur Market"]
        for item in facilities_7:
            try:
                driver.find_element(By.XPATH, f"//*[contains(text(), '{item}')]")
                print(f" - Found Facility: {item}")
            except:
                print(f" - MISSING Facility: {item}")


        # --- TEST 2: COZY HOMES (ID: 8) ---
        print("\nNavigating to COZY HOMES Details...")
        driver.get("http://127.0.0.1:8000/property-details/8/")
        time.sleep(2)

        title = driver.find_element(By.TAG_NAME, "h1").text
        if "COZY HOMES" in title:
            print(f"PASS: Title verified -> {title}")

        owner = driver.find_element(By.XPATH, "//*[contains(text(), 'COZY LIVING GROUP')]")
        location = driver.find_element(By.XPATH, "//*[contains(text(), 'Banani, Dhaka')]")
        print(f"PASS: Owner and Location are correct.")

        facilities_8 = ["Luxury Suite Options", "Daily Garbage Collection", "Prayer Room Facility"]
        for item in facilities_8:
            try:
                driver.find_element(By.XPATH, f"//*[contains(text(), '{item}')]")
                print(f" - Found Facility: {item}")
            except:
                print(f" - MISSING Facility: {item}")


        # --- TEST 3: ECO-STAY (ID: 9) ---
        print("\nNavigating to ECO-STAY Details...")
        driver.get("http://127.0.0.1:8000/property-details/9/")
        time.sleep(2)

        title = driver.find_element(By.TAG_NAME, "h1").text
        if "ECO-STAY" in title:
            print(f"PASS: Title verified -> {title}")

        owner = driver.find_element(By.XPATH, "//*[contains(text(), 'GREEN REAL ESTATE')]")
        location = driver.find_element(By.XPATH, "//*[contains(text(), 'Gulshan 1, Dhaka')]")
        print(f"PASS: Owner and Location are correct.")

        facilities_9 = ["Eco-friendly Lighting", "Community Workstation", "Complimentary Tea/Coffee Machine"]
        for item in facilities_9:
            try:
                driver.find_element(By.XPATH, f"//*[contains(text(), '{item}')]")
                print(f" - Found Facility: {item}")
            except:
                print(f" - MISSING Facility: {item}")

        # Final Verification of Common Elements
        book_now = driver.find_element(By.CLASS_NAME, "book-now-btn")
        back_btn = driver.find_element(By.CLASS_NAME, "back-btn")
        if book_now.is_displayed() and back_btn.is_displayed():
            print("\nPASS: Navigation and Booking buttons are verified on the final page.")

    except Exception as e:
        print(f"\nAn error occurred during testing: {e}")

    finally:
        time.sleep(2)
        driver.quit()
        print("\nAll Girls' Hostel Detail Tests Completed.")

if __name__ == "__main__":
    run_girls_hostel_tests()