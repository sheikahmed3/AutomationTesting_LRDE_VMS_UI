from pages.login_page import test_login
from pages.home_page import test_home
from pages.department_details_page import test_department_details

def main_test():
    test_login()
    test_home()
    test_department_details()

# to run the all test cases:python -m pytest test_main.py --html=r
# git commit : git commit -m "msg"
# git add : git add .
    
