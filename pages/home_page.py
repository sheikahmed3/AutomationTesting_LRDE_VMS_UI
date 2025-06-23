from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import test_login


def test_home():
    driver = test_login()
    if not driver:
        print("Login failed, test aborted.")
        return

    try:
        # Open Home Page
        driver.get("http://192.168.0.182:8084/LRDE_VMS_UI/Home.jsp")

        # Wait for an element to confirm Home Page is loaded (adjust selector as needed)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "openNav"))  # Example: menu button
        )
        print("Home page loaded successfully.")

    except Exception as e:
        print(f"Error occurred while loading Home page: {e}")

    finally:
        time.sleep(3)
        driver.quit()

# Run test
# test_home()
