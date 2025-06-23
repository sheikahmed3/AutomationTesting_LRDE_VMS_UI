from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        # Step 1: Open login page of LRDE_VMS_UI
        driver.get("http://192.168.0.182:8084/LRDE_VMS_UI/Signin.jsp")

        # Step 2: Enter username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "loginname"))
        )
        username_field.click()
        username_field.send_keys("exult")  

        # Step 3: Enter password
        password_field = driver.find_element(By.NAME, "loginpwd")
        password_field.click()
        password_field.send_keys("exult")  

        # Step 4: Click login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']"))
        )
        login_button.click()

        # Step 5: Wait for redirect to home page
        WebDriverWait(driver, 20).until(
            EC.url_contains("/LRDE_VMS_UI/Home.jsp")  
        )

        # Step 6: Check successful login
        current_url = driver.current_url
        if "Home.jsp" in current_url:
            print("Login successful. Home page loaded:", current_url)
            return driver  #  RETURN the driver so other scripts can use it
        else:
            print("❌ Login failed or wrong redirect. URL:", current_url)
            driver.quit()
            return None

    except Exception as e:
        print("Test failed:", str(e))
        driver.quit()
        return None  #  Return None on failure


# Only call for standalone testing
# if __name__ == "__main__":
#     test_login()
