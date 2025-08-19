from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options


def new_session():
    options = Options()
    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.turacoaddis.com")
    driver.fullscreen_window()
    return driver

def run_contact_us_test(driver):

    contact_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'scroll-button') and contains(text(), 'Contact Us')]"))
    )
    contact_button.click()

    time.sleep(1.5) 

    # Wait for contact form to be visible
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "contact-form"))
    )
    
    time.sleep(2)
    name_text_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "name"))
    )

    email_text_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "email"))
    )

    phone_text_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "phone"))
    )

    message_text_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "message"))
    )


    submit_button_clickable = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "submit-btn"))
    )


    name_text_box.send_keys("Test Name")
    email_text_box.send_keys("test@test.com")
    phone_text_box.send_keys("6134134804")
    message_text_box.send_keys("this is an automated test")

    submit_button_clickable.click()

def run_room_reservation(driver, room_type): 

    rooms_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'scroll-button') and contains(text(), 'Rooms')]"))
    )
    rooms_button.click()

    time.sleep(1.5)

    book_now_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, room_type))
    )
    
    book_now_button.click()
    driver.fullscreen_window()

    today = datetime.now()
    check_in_date = (today + timedelta(days=3)).strftime("%Y-%m-%d")
    check_out_date = (today + timedelta(days=4)).strftime("%Y-%m-%d")

    driver.execute_script(f"document.getElementById('check-in').value = '{check_in_date}';")
    driver.execute_script("document.getElementById('check-in').dispatchEvent(new Event('change'));")
        
    driver.execute_script(f"document.getElementById('check-out').value = '{check_out_date}';")
    driver.execute_script("document.getElementById('check-out').dispatchEvent(new Event('change'));")

    guests_dropdown = Select(WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "guests"))
    ))
    guests_dropdown.select_by_visible_text("2 Guests")

    name_text_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "name"))
    )

    email_text_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "email"))
    )

    phone_text_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "phone"))
    )

    name_text_box.send_keys("Test Name")
    email_text_box.send_keys("test@test.com")
    phone_text_box.send_keys("6134134804")

    reserve_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "submit-btn"))
    )

    reserve_button.click()


room_type_css = {
    "standard": ".section1 .book .custom-link",
    "deluxe": ".section2 .book .custom-link",
    "double": ".section3 .book .custom-link",
}# Test Standard Room
try:
    print("Starting Standard Room test...")
    driver = new_session()
    run_room_reservation(driver, room_type_css["standard"])
    print("✓ Standard Room test completed successfully")
except Exception as e:
    print(f"✗ Standard Room test failed: {e}")
finally:
    try:
        driver.quit()
    except:
        pass

# Test Deluxe Room
try:
    print("Starting Deluxe Room test...")
    driver = new_session()
    run_room_reservation(driver, room_type_css["deluxe"])
    print("✓ Deluxe Room test completed successfully")
except Exception as e:
    print(f"✗ Deluxe Room test failed: {e}")
finally:
    try:
        driver.quit()
    except:
        pass

# Test Double Room
try:
    print("Starting Double Room test...")
    driver = new_session()
    run_room_reservation(driver, room_type_css["double"])
    print("✓ Double Room test completed successfully")
except Exception as e:
    print(f"✗ Double Room test failed: {e}")
finally:
    try:
        driver.quit()
    except:
        pass

# Test Contact Us
try:
    print("Starting Contact Us test...")
    driver = new_session()
    run_contact_us_test(driver)
    print("✓ Contact Us test completed successfully")
except Exception as e:
    print(f"✗ Contact Us test failed: {e}")
finally:
    try:
        driver.quit()
    except:
        pass
