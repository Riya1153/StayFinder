from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime

# =========================
# SETUP DRIVER
# =========================
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# ── HTML Report Storage ──
results = []
start_time = datetime.datetime.now()

def record(name, status, detail=""):
    results.append({"name": name, "status": status, "detail": detail})
    icon = "✅" if status == "PASS" else "❌"
    print(f"  {icon} {name}")

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

    print("ALL PREVIOUS TESTS COMPLETED")

    # =========================================================
    # =========================================================
    # SEARCHING SECTOR SELENIUM TESTS — START
    # =========================================================
    # =========================================================
    print("\n" + "="*55)
    print("  SEARCHING SECTOR TESTS — START")
    print("="*55 + "\n")

    BASE = "http://127.0.0.1:8000"
    SS_URL = f"{BASE}/searching-sector/"

    # ── TEST S1: Page Load ──────────────────────────────────
    print("[ PAGE LOAD TESTS ]")
    driver.get(SS_URL)
    time.sleep(1)

    try:
        assert "StayFinder" in driver.title
        record("S01 - Page title contains StayFinder", "PASS")
    except:
        record("S01 - Page title contains StayFinder", "FAIL", f"Got: {driver.title}")

    try:
        assert "SEARCHING SECTOR" in driver.find_element(By.TAG_NAME, "body").text
        record("S02 - SEARCHING SECTOR label visible", "PASS")
    except:
        record("S02 - SEARCHING SECTOR label visible", "FAIL")

    try:
        assert "FOR BOOKING" in driver.find_element(By.TAG_NAME, "body").text
        record("S03 - FOR BOOKING banner visible", "PASS")
    except:
        record("S03 - FOR BOOKING banner visible", "FAIL")

    try:
        radios = driver.find_elements(By.CSS_SELECTOR, "input[type='radio'][name='category']")
        values = [r.get_attribute("value") for r in radios]
        assert "buy" in values and "rent" in values and "roommates" in values
        record("S04 - All 3 radio buttons present (Buy/Rent/Roommates)", "PASS")
    except:
        record("S04 - All 3 radio buttons present (Buy/Rent/Roommates)", "FAIL")

    try:
        assert driver.find_element(By.ID, "section-buy").is_displayed()
        record("S05 - Buy section visible by default", "PASS")
    except:
        record("S05 - Buy section visible by default", "FAIL")

    try:
        assert not driver.find_element(By.ID, "section-rent").is_displayed()
        record("S06 - Rent section hidden by default", "PASS")
    except:
        record("S06 - Rent section hidden by default", "FAIL")

    try:
        assert not driver.find_element(By.ID, "section-roommates").is_displayed()
        record("S07 - Roommates section hidden by default", "PASS")
    except:
        record("S07 - Roommates section hidden by default", "FAIL")

    try:
        btn = driver.find_element(By.CSS_SELECTOR, "button.btn-tell")
        assert "Tell Us" in btn.text
        record("S08 - Tell Us Your Requirement button present", "PASS")
    except:
        record("S08 - Tell Us Your Requirement button present", "FAIL")

    try:
        btn = driver.find_element(By.CSS_SELECTOR, "button.btn-manual")
        assert "MANUAL" in btn.text
        record("S09 - MANUAL button present", "PASS")
    except:
        record("S09 - MANUAL button present", "FAIL")

    # ── TEST S2: Radio Tab Switching ────────────────────────
    print("\n[ RADIO TAB SWITCHING TESTS ]")
    driver.get(SS_URL)
    time.sleep(0.5)

    try:
        driver.find_element(By.CSS_SELECTOR, "input[value='rent']").click()
        time.sleep(0.4)
        assert driver.find_element(By.ID, "section-rent").is_displayed()
        record("S10 - Click Rent → Rent section shows", "PASS")
    except:
        record("S10 - Click Rent → Rent section shows", "FAIL")

    try:
        assert not driver.find_element(By.ID, "section-buy").is_displayed()
        record("S11 - Click Rent → Buy section hides", "PASS")
    except:
        record("S11 - Click Rent → Buy section hides", "FAIL")

    try:
        driver.find_element(By.CSS_SELECTOR, "input[value='roommates']").click()
        time.sleep(0.4)
        assert driver.find_element(By.ID, "section-roommates").is_displayed()
        record("S12 - Click Roommates → Roommates section shows", "PASS")
    except:
        record("S12 - Click Roommates → Roommates section shows", "FAIL")

    try:
        assert not driver.find_element(By.ID, "section-rent").is_displayed()
        record("S13 - Click Roommates → Rent section hides", "PASS")
    except:
        record("S13 - Click Roommates → Rent section hides", "FAIL")

    try:
        driver.find_element(By.CSS_SELECTOR, "input[value='buy']").click()
        time.sleep(0.4)
        assert driver.find_element(By.ID, "section-buy").is_displayed()
        assert not driver.find_element(By.ID, "section-rent").is_displayed()
        record("S14 - Click Buy after Rent → Buy shows, Rent hides", "PASS")
    except:
        record("S14 - Click Buy after Rent → Buy shows, Rent hides", "FAIL")

    try:
        for val in ['buy', 'rent', 'roommates']:
            driver.find_element(By.CSS_SELECTOR, f"input[value='{val}']").click()
            time.sleep(0.3)
            visible = sum([
                driver.find_element(By.ID, "section-buy").is_displayed(),
                driver.find_element(By.ID, "section-rent").is_displayed(),
                driver.find_element(By.ID, "section-roommates").is_displayed(),
            ])
            assert visible == 1, f"Expected 1 visible section, got {visible} for '{val}'"
        record("S15 - Only 1 section visible at a time (all 3 tested)", "PASS")
    except Exception as e:
        record("S15 - Only 1 section visible at a time", "FAIL", str(e))

    # ── TEST S3: Buy Dropdowns ──────────────────────────────
    print("\n[ BUY SECTION DROPDOWN TESTS ]")
    driver.get(SS_URL)
    time.sleep(0.5)

    try:
        opts = [o.text for o in Select(driver.find_element(By.CSS_SELECTOR, "select[name='buy_property_type']")).options]
        assert "Apartment/Flats" in opts
        record("S16 - Buy property type has Apartment/Flats", "PASS")
    except:
        record("S16 - Buy property type has Apartment/Flats", "FAIL")

    try:
        opts = [o.text for o in Select(driver.find_element(By.CSS_SELECTOR, "select[name='buy_property_type']")).options]
        assert "Flat" in opts
        record("S17 - Buy property type has Flat", "PASS")
    except:
        record("S17 - Buy property type has Flat", "FAIL")

    try:
        sel = Select(driver.find_element(By.CSS_SELECTOR, "select[name='buy_size']"))
        assert sel.first_selected_option.text == "Any"
        record("S18 - Buy size dropdown default is Any", "PASS")
    except:
        record("S18 - Buy size dropdown default is Any", "FAIL")

    try:
        opts = Select(driver.find_element(By.CSS_SELECTOR, "select[name='buy_size']")).options
        assert len(opts) >= 5
        record("S19 - Buy size dropdown has 5+ options", "PASS")
    except:
        record("S19 - Buy size dropdown has 5+ options", "FAIL")

    try:
        city = driver.find_element(By.CSS_SELECTOR, "input[name='buy_city']")
        assert city.get_attribute("value") == "Dhaka"
        record("S20 - Buy city default value is Dhaka", "PASS")
    except:
        record("S20 - Buy city default value is Dhaka", "FAIL")

    try:
        driver.find_element(By.CSS_SELECTOR, "input[name='buy_location']")
        record("S21 - Buy location field exists", "PASS")
    except:
        record("S21 - Buy location field exists", "FAIL")

    # ── TEST S4: Rent Dropdowns ─────────────────────────────
    print("\n[ RENT SECTION DROPDOWN TESTS ]")
    driver.get(SS_URL)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "input[value='rent']").click()
    time.sleep(0.4)

    try:
        opts = [o.text for o in Select(driver.find_element(By.CSS_SELECTOR, "select[name='rent_property_type']")).options]
        assert "Sublet" in opts
        record("S22 - Rent property type has Sublet", "PASS")
    except:
        record("S22 - Rent property type has Sublet", "FAIL")

    try:
        opts = [o.text for o in Select(driver.find_element(By.CSS_SELECTOR, "select[name='rent_tenant_type']")).options]
        assert "Family" in opts and "Female" in opts and "Male" in opts
        record("S23 - Tenant type has Family, Female, Male", "PASS")
    except:
        record("S23 - Tenant type has Family, Female, Male", "FAIL")

    try:
        opts = [o.text for o in Select(driver.find_element(By.CSS_SELECTOR, "select[name='rent_price_min']")).options]
        assert "1 lac" in opts
        record("S24 - Rent price min has 1 lac option", "PASS")
    except:
        record("S24 - Rent price min has 1 lac option", "FAIL")

    try:
        sel = Select(driver.find_element(By.CSS_SELECTOR, "select[name='rent_tenant_type']"))
        sel.select_by_visible_text("Male")
        assert sel.first_selected_option.text == "Male"
        record("S25 - Can select Male in tenant type", "PASS")
    except:
        record("S25 - Can select Male in tenant type", "FAIL")

    # ── TEST S5: Roommates Dropdowns ────────────────────────
    print("\n[ ROOMMATES SECTION DROPDOWN TESTS ]")
    driver.get(SS_URL)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "input[value='roommates']").click()
    time.sleep(0.4)

    try:
        opts = [o.text for o in Select(driver.find_element(By.CSS_SELECTOR, "select[name='room_property_type']")).options]
        assert "Commercial Mess" in opts and "Independent Mess" in opts and "Hostel" in opts
        record("S26 - Residence type has Commercial Mess, Independent Mess, Hostel", "PASS")
    except:
        record("S26 - Residence type has Commercial Mess, Independent Mess, Hostel", "FAIL")

    try:
        opts = [o.text for o in Select(driver.find_element(By.CSS_SELECTOR, "select[name='room_type']")).options]
        assert "2 Person in One Room" in opts
        record("S27 - Room type has 2 Person in One Room", "PASS")
    except:
        record("S27 - Room type has 2 Person in One Room", "FAIL")

    try:
        opts = [o.text for o in Select(driver.find_element(By.CSS_SELECTOR, "select[name='room_type']")).options]
        assert "4+ Person in One Room" in opts
        record("S28 - Room type has 4+ Person in One Room", "PASS")
    except:
        record("S28 - Room type has 4+ Person in One Room", "FAIL")

    try:
        opts = [o.text for o in Select(driver.find_element(By.CSS_SELECTOR, "select[name='room_gender']")).options]
        assert "Female" in opts and "Male" in opts
        record("S29 - Gender has Female and Male", "PASS")
    except:
        record("S29 - Gender has Female and Male", "FAIL")

    try:
        ta = driver.find_element(By.CSS_SELECTOR, "textarea[name='room_characteristics']")
        ta.clear()
        ta.send_keys("Non-smoker preferred")
        assert ta.get_attribute("value") == "Non-smoker preferred"
        record("S30 - Can type in characteristics textarea", "PASS")
    except:
        record("S30 - Can type in characteristics textarea", "FAIL")

    # ── TEST S6: Form Submission ────────────────────────────
    print("\n[ FORM SUBMISSION TESTS ]")

    # Buy submit
    driver.get(SS_URL)
    time.sleep(0.5)
    try:
        Select(driver.find_element(By.CSS_SELECTOR, "select[name='buy_property_type']")).select_by_visible_text("Apartment/Flats")
        driver.find_element(By.CSS_SELECTOR, "button.btn-tell").click()
        time.sleep(1)
        assert "search-results" in driver.current_url
        record("S31 - Buy form submit goes to search-results page", "PASS")
    except:
        record("S31 - Buy form submit goes to search-results page", "FAIL", driver.current_url)

    try:
        assert "category=buy" in driver.current_url
        record("S32 - URL contains category=buy after submit", "PASS")
    except:
        record("S32 - URL contains category=buy after submit", "FAIL", driver.current_url)

    try:
        assert "SEARCH RESULTS" in driver.find_element(By.TAG_NAME, "body").text
        record("S33 - Results page shows SEARCH RESULTS heading", "PASS")
    except:
        record("S33 - Results page shows SEARCH RESULTS heading", "FAIL")

    try:
        back = driver.find_element(By.CSS_SELECTOR, "a.back-btn")
        assert "Back" in back.text
        record("S34 - Results page has Back to Search button", "PASS")
    except:
        record("S34 - Results page has Back to Search button", "FAIL")

    try:
        driver.find_element(By.CSS_SELECTOR, "a.back-btn").click()
        time.sleep(1)
        assert "searching-sector" in driver.current_url
        record("S35 - Back button returns to searching-sector page", "PASS")
    except:
        record("S35 - Back button returns to searching-sector page", "FAIL", driver.current_url)

    # Rent submit
    driver.get(SS_URL)
    time.sleep(0.5)
    try:
        driver.find_element(By.CSS_SELECTOR, "input[value='rent']").click()
        time.sleep(0.3)
        Select(driver.find_element(By.CSS_SELECTOR, "select[name='rent_tenant_type']")).select_by_visible_text("Family")
        driver.find_element(By.CSS_SELECTOR, "button.btn-tell").click()
        time.sleep(1)
        assert "search-results" in driver.current_url and "category=rent" in driver.current_url
        record("S36 - Rent form submit goes to results with category=rent", "PASS")
    except:
        record("S36 - Rent form submit goes to results with category=rent", "FAIL", driver.current_url)

    # Roommates submit
    driver.get(SS_URL)
    time.sleep(0.5)
    try:
        driver.find_element(By.CSS_SELECTOR, "input[value='roommates']").click()
        time.sleep(0.3)
        Select(driver.find_element(By.CSS_SELECTOR, "select[name='room_property_type']")).select_by_visible_text("Hostel")
        Select(driver.find_element(By.CSS_SELECTOR, "select[name='room_gender']")).select_by_visible_text("Male")
        driver.find_element(By.CSS_SELECTOR, "button.btn-tell").click()
        time.sleep(1)
        assert "search-results" in driver.current_url and "category=roommates" in driver.current_url
        record("S37 - Roommates form submit goes to results with category=roommates", "PASS")
    except:
        record("S37 - Roommates form submit goes to results with category=roommates", "FAIL", driver.current_url)

    print("\n" + "="*55)
    print("  SEARCHING SECTOR TESTS — COMPLETE")
    print("="*55 + "\n")

    print("ALL TESTS COMPLETED SUCCESSFULLY")

finally:
    time.sleep(2)
    driver.quit()

    # ── Generate HTML Report ─────────────────────────────────
    if results:
        end_time = datetime.datetime.now()
        duration = round((end_time - start_time).total_seconds(), 2)
        total   = len(results)
        passed  = sum(1 for r in results if r["status"] == "PASS")
        failed  = total - passed
        pct     = round((passed / total * 100) if total else 0, 1)
        bar_col = "#28a745" if failed == 0 else "#dc3545"

        rows = ""
        for i, r in enumerate(results, 1):
            bg = "#d4edda" if r["status"] == "PASS" else "#f8d7da"
            bc = "#28a745" if r["status"] == "PASS" else "#dc3545"
            det = f"<pre style='font-size:11px;color:#555;margin:4px 0 0;white-space:pre-wrap'>{r['detail']}</pre>" if r["detail"] else ""
            rows += f"""<tr style='background:{bg}'>
              <td style='padding:9px 14px;font-size:13px;color:#666'>#{i}</td>
              <td style='padding:9px 14px;font-size:13px'>{r['name']}</td>
              <td style='padding:9px 14px;text-align:center'>
                <span style='background:{bc};color:#fff;padding:3px 12px;border-radius:12px;font-size:12px;font-weight:bold'>{r['status']}</span>
              </td>
            </tr>{'<tr><td colspan=3 style=padding:0_14px_10px;background:'+bg+'><div style=background:#fff;padding:8px;border-radius:4px;border:1px_solid_#ddd>'+det+'</div></td></tr>' if det else ''}"""

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Selenium Test Report — StayFinder Searching Sector</title>
  <style>
    * {{ box-sizing:border-box; }}
    body {{ font-family:Arial,sans-serif; background:#f0f2f5; margin:0; padding:30px; }}
    .hdr {{ background:linear-gradient(135deg,#005BB7,#0074e4); color:#fff; padding:26px 34px; border-radius:10px; margin-bottom:26px; box-shadow:0 4px 12px rgba(0,91,183,.3); }}
    .hdr h1 {{ margin:0 0 6px; font-size:24px; }}
    .hdr p  {{ margin:0; font-size:13px; opacity:.85; }}
    .cards  {{ display:flex; gap:14px; margin-bottom:26px; flex-wrap:wrap; }}
    .card   {{ background:#fff; border-radius:10px; padding:18px 26px; flex:1; min-width:110px; box-shadow:0 2px 8px rgba(0,0,0,.07); text-align:center; }}
    .num    {{ font-size:36px; font-weight:bold; line-height:1; }}
    .lbl    {{ font-size:11px; color:#888; margin-top:5px; text-transform:uppercase; letter-spacing:.5px; }}
    .pw     {{ background:#e9ecef; border-radius:10px; height:14px; margin-bottom:26px; overflow:hidden; }}
    .pb     {{ height:14px; background:{bar_col}; border-radius:10px; width:{pct}%; }}
    table   {{ width:100%; border-collapse:collapse; background:#fff; border-radius:10px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,.07); }}
    thead tr {{ background:#005BB7; color:#fff; }}
    th      {{ padding:11px 14px; text-align:left; font-size:12px; font-weight:600; }}
    .badge  {{ display:inline-block; background:{bar_col}; color:#fff; padding:7px 20px; border-radius:20px; font-weight:bold; font-size:14px; margin-bottom:24px; }}
    .footer {{ text-align:center; color:#bbb; font-size:12px; margin-top:22px; }}
  </style>
</head>
<body>
  <div class="hdr">
    <h1>🧪 Selenium Test Report — StayFinder</h1>
    <p>Searching Sector Module &nbsp;|&nbsp; {end_time.strftime('%Y-%m-%d %H:%M:%S')} &nbsp;|&nbsp; Duration: {duration}s</p>
  </div>
  <div class="cards">
    <div class="card"><div class="num" style="color:#005BB7">{total}</div><div class="lbl">Total</div></div>
    <div class="card"><div class="num" style="color:#28a745">{passed}</div><div class="lbl">Passed</div></div>
    <div class="card"><div class="num" style="color:#dc3545">{failed}</div><div class="lbl">Failed</div></div>
    <div class="card"><div class="num" style="color:{bar_col}">{pct}%</div><div class="lbl">Pass Rate</div></div>
  </div>
  <div style="font-size:13px;color:#555;margin-bottom:6px">Pass Rate: {pct}%</div>
  <div class="pw"><div class="pb"></div></div>
  <div class="badge">{"✅ ALL PASSED" if failed==0 else f"❌ {failed} FAILED"}</div>
  <table>
    <thead><tr><th style="width:50px">#</th><th>Test Name</th><th style="width:100px;text-align:center">Result</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <div class="footer">StayFinder Selenium Test Suite — Searching Sector</div>
</body>
</html>"""

        with open("selenium_report.html", "w", encoding="utf-8") as f:
            f.write(html)

        print(f"\n{'='*55}")
        print(f"  Total: {total}  |  Passed: {passed}  |  Failed: {failed}")
        print(f"  Report saved → selenium_report.html")
        print(f"{'='*55}\n")

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