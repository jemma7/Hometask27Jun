from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('launch Chrome browser')
def launch_browser(self):
    self.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')



@when('open OrangeHRM homepage')
def open_orangeHRM(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    self.driver.maximize_window()


@then('Login OrangeHRM Admin page')
def login_amin_page(self):
    # name_password =self.driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/span').text
    # name = name_password[13:19]
    # password = name_password[32:41]
    self.driver.find_element(By.ID,"txtUsername").send_keys("Admin")
    self.driver.find_element(By.ID,"txtPassword").send_keys("admin123")
    self.driver.find_element(By.ID,"btnLogin").click()


@then('Add a user')
def add_user(self):
    self.driver.find_element(By.LINK_TEXT,"Admin").click()
    self.driver.find_element(By.ID,"btnAdd").click()
    self.driver.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Ananya Dash")
    self.driver.find_element(By.ID,"systemUser_userName").send_keys("Anaya30")
    self.driver.find_element(By.ID,"systemUser_password").send_keys("Anaya4567")
    self.driver.find_element(By.ID,"systemUser_confirmPassword").send_keys("Anaya4567")
    self.driver.find_element(By.ID,"btnSave").click()


@then('Verify a user is added')
def verify_user_added(self):
    self.driver.find_element(By.NAME,"searchSystemUser[userName]").send_keys("Anaya30")
    self.driver.find_element(By.ID,"searchBtn").click()
    status =self.driver.find_element(By.LINK_TEXT,"Anaya30").is_displayed()
    assert status is True


@then('close the browser')
def close_browser(self):
    self.driver.close()