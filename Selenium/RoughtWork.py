import unittest
from selenium import webdriver

class GoogleTest(unittest.TestCase):  # ✅ Must inherit from unittest.TestCase

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_google_title(self):  # ✅ Test method must start with "test_"
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
