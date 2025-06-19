from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Step 2: Open login page of LRDE_VMS_UI
    driver.get("http://192.168.0.182:8084/LRDE_VMS_UI/Signin.jsp")

    # Step 3: Enter username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "loginname"))
    )
    username_field.click()
    username_field.send_keys("exult")  # Replace with valid username

    # Step 4: Enter password
    password_field = driver.find_element(By.NAME, "loginpwd")
    password_field.click()
    password_field.send_keys("exult")  # Replace with valid password

    # Step 5: Submit form (either using ENTER or clicking login button)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']"))
    )
    login_button.click()

    # Step 6: Wait for redirect to home page
    WebDriverWait(driver, 20).until(
        EC.url_contains("http://192.168.0.182:8084/LRDE_VMS_UI/Home.jsp")  # Change to match your actual home URL
    )

    # Step 7: Verify successful login (by URL, title, or specific element)
    current_url = driver.current_url
    if "http://192.168.0.182:8084/LRDE_VMS_UI/Home.jsp" in current_url:
        print("✅ Login successful. Home page loaded:", current_url)
    else:
        print("❌ Login failed or wrong redirect. URL:", current_url)

except Exception as e:
    print("❌ Test failed:", str(e))

finally:
    driver.quit()
