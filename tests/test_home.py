from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from test_login import test_login  
import time

def test_home():
    # Get the driver from login
    driver = test_login()  # Assumes test_login logs in and returns a driver

    # Step 1: Navigate to Home Page
    driver.get("http://192.168.0.182:8084/LRDE_VMS_UI/Home.jsp")  

    try:
        # Step 2: Click on the menu button (span with id="openNav")
        menu_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "openNav"))
        )
        menu_button.click()
        time.sleep(1)

        # Step 3: Click on Department Details from the menu
        department_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Department Details' and @href='AddDepartment.jsp']"))
        )
        department_link.click()
        print("✅ Department Details link clicked successfully.")

    except Exception as e:
        print(f"❌ Error occurred: {e}")

    finally:
        time.sleep(3)
        driver.quit()

test_home()
