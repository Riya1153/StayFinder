from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Driver
driver = webdriver.Chrome()

try:
    # 1. Navigate to the Boy's Hostel List page
    # Make sure your Django server is running!
    print("Navigating to Boy's Hostel List...")
    driver.get("http://127.0.0.1:8000/hostels/boys/")
    driver.maximize_window()

    # 2. Verify Page Header
    header = driver.find_element(By.TAG_NAME, "h1").text
    if "BOY'S HOSTEL LIST" in header:
        print("PASS: Page header is correct.")

    # 3. Count the number of hostel cards
    # Assuming your cards have a class like 'hostel-card' or are inside the white divs
    hostel_cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'card')] or //h3/parent::div")
    print(f"INFO: Found {len(hostel_cards)} hostel cards on the page.")

    # 4. Verify specific hostel names are present
    hostels_to_check = ["UNIQUE BOY'S HOSTEL", "BOYS STAY", "GHAR ANAGAN HOSTEL"]
    for name in hostels_to_check:
        try:
            driver.find_element(By.XPATH, f"//*[contains(text(), '{name}')]")
            print(f"PASS: {name} is visible.")
        except:
            print(f"FAIL: {name} was not found on the page.")

    # 5. Test the "Call for Price" badge visibility
    badges = driver.find_elements(By.XPATH, "//*[contains(text(), 'CALL FOR PRICE')]")
    if len(badges) > 0:
        print(f"PASS: {len(badges)} price badges found.")

    # 6. Test the "DETAILS" button for the first hostel
    print("Testing 'DETAILS' button click...")
    details_buttons = driver.find_elements(By.XPATH,
                                           "//button[contains(text(), 'DETAILS')] or //a[contains(text(), 'DETAILS')]")

    if details_buttons:
        details_buttons[0].click()
        time.sleep(2)
        print("PASS: Clicked Details button successfully.")
    else:
        print("FAIL: No Details buttons found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(2)
    driver.quit()
    print("Test Completed.")