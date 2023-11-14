# Ovde definisemo lokatore za elemente na Login page-u i metode
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage():
    email_field_id = "Email"
    password_field_id = "Password"
    login_button_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    logout_link_text = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.username_field = self.driver.find_element(By.ID,self.email_field_id)
        self.username_field.clear()
        time.sleep(2)
        self.username_field.send_keys(username)
        time.sleep(3)

    def enter_password(self,password):
        self.password_field = self.driver.find_element(By.ID,self.password_field_id )
        self.password_field.clear()
        time.sleep(2)
        self.password_field.send_keys(password)
        time.sleep(3)


    def click_on_login_button(self):
        self.login_button = self.driver.find_element(By.XPATH,self.login_button_xpath)
        self.login_button.click()
        time.sleep(3)

    def click_on_logout(self):
        self.login_link = self.driver.find_element(By.LINK_TEXT,self.logout_link_text)
        self.login_link.click()
        time.sleep(3)
