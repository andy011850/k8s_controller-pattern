from tkinter import BROWSE
from selenium import webdriver
import unittest

# driver的來源
driver = webdriver.Remote(
     command_executor='http://localhost:54635',
     desired_capabilities={
          "browserName": "chrome",
          "platformName": "LINUX"
          }
)

# 執行測試(判斷title)
class selenium_grid (unittest.TestCase):
     def test(self):
          driver.get("https://www.google.com/")
          self.assertEqual('Google', driver.title, 'webpage title are not same')
          driver.quit()

if __name__ == "__main__":
     unittest.main()
