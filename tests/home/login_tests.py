from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox(executable_path="C:\\Users\\Demoriel Purnell\\"
                                                   "workspace_python\\drivers\\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(7)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")
        result = lp.verifyLoginSuccessful()
        assert result == False
        driver.quit()
