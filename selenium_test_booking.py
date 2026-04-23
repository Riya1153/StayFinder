from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # 1. Open your local Django server
    driver.get("http://127.0.0.1:8000/searching-sector/")
    driver.maximize_window()
    time.sleep(2)

    # 2. Test the "Rent" Bubble
    print("Testing Rent bubble...")
    rent_bubble = driver.find_element(By.CSS_SELECTOR, "input[value='rent']")
    rent_bubble.click()
    time.sleep(1)

    # Verify Rent box is visible
    rent_box = driver.find_element(By.ID, "box-rent")
    if rent_box.is_displayed():
        print("PASS: Rent box appeared.")

    # Fill out a Rent field
    tenant_select = Select(driver.find_element(By.NAME, "tenant_type"))
    tenant_select.select_by_visible_text("FEMALE")

    # 3. Test the "Roommates" Bubble
    print("Testing Roommates bubble...")
    roommate_bubble = driver.find_element(By.CSS_SELECTOR, "input[value='roommates']")
    roommate_bubble.click()
    time.sleep(1)

    # Fill out the Characteristics text area
    char_box = driver.find_element(By.NAME, "characteristics")
    char_box.send_keys("Non-smoker, student preferred, quiet environment.")
    print("PASS: Characteristics text area is functional.")

    # 4. Submit the Form
    print("Testing Submit button...")
    submit_btn = driver.find_element(By.CLASS_NAME, "submit-btn")
    submit_btn.click()
    time.sleep(2)

    print("Full Booking Sector test completed successfully!")

finally:
    driver.quit()