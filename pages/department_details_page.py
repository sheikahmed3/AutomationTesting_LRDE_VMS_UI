# test_department_details.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, sys, os, traceback
from datetime import datetime

# Add your project path for import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.login_page import test_login  # Must return driver after successful login

# URLs
ADD_URL = "http://192.168.0.182:8084/LRDE_VMS_UI/AddDepartment.jsp"
VIEW_URL = "http://192.168.0.182:8084/LRDE_VMS_UI/ViewDepartment.jsp"

def wait_for(driver, by, value, click=False, timeout=10):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
    elem = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    if click:
        elem.click()
    return elem

def generate_department_name():
    import random, string, re

    first_char = random.choice(string.ascii_letters)  # Must start with an alphabet
    rest = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
    full = first_char + rest
    cleaned = re.sub(r'[^a-zA-Z0-9_]', '', full.replace(" ", "_"))
    return cleaned

def generate_department_false_name():
    import random, string, re

    first_char = random.choice(string.digits)  # Must start with an alphabet
    rest = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
    full = first_char + rest
    cleaned = re.sub(r'[^a-zA-Z0-9_@^]', '', full.replace(" ", "_"))
    return cleaned

#It is the code for the add the data to the database 
def test_department_details():
    driver = test_login()
    if not driver:
        print("Login failed. Test aborted.")
        return

    try:
        # Step 1: Navigate to AddDepartment.jsp
        print("Opening AddDepartment.jsp")
        driver.get(ADD_URL)
        time.sleep(3)

        # Step 2: Fill department name
        dept_name = generate_department_name()
        print(f"Filling department: {dept_name}")
        dept_field = wait_for(driver, By.NAME, "dptname")
        dept_field.clear()
        dept_field.send_keys(dept_name) 
        time.sleep(5)      

        # Step 3: Click Add
        print("Clicking Add")
        wait_for(driver, By.ID, "Add", click=True)
        time.sleep(5)

        # Step 4: Check redirect manually
        current_url = driver.current_url
        if "ViewDepartment.jsp" in current_url:
            print("Redirected to ViewDepartment.jsp:", current_url)
        else:
            print(f"Not redirected. Still on: {current_url} — assuming Add was successful anyway.")

        # Step 5: Return to AddDepartment.jsp
        print("Returning to AddDepartment.jsp")
        driver.get(ADD_URL)
        time.sleep(5)

        # Step 6: Enter dummy text for Reset test
        dept_false_name = generate_department_false_name()
        print(f"Filling department: {dept_false_name}")
        dept_field = wait_for(driver, By.NAME, "dptname")
        dept_field.clear()
        dept_field.send_keys(dept_false_name)
        time.sleep(5)

        # Step 7: Click Reset
        print("Clicking Reset")
        wait_for(driver, By.ID, "Reset", click=True)
        time.sleep(5)

        # Step 8: Verify field is cleared
        dept_field = wait_for(driver, By.NAME, "dptname")
        if dept_field.get_attribute("value") == "":
            print("Reset successful, field cleared")
        else:
            print(f"Reset failed. Still contains: {dept_field.get_attribute('value')}")

        print("Clicking View")
        wait_for(driver, By.ID, "View", click=True)

        # Step 9: Confirm redirection
        WebDriverWait(driver, 10).until(EC.url_contains("ViewDepartment.jsp"))
        print("View worked. Page loaded:", driver.current_url)

    except Exception as e:
        print("Exception during workflow:")
        traceback.print_exc()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"department_workflow_error_{timestamp}.png")
    finally:
        time.sleep(6)
        driver.quit()

# # Run test
# if __name__ == "__main__":
#     test_department_details()
