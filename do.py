import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome()  # Use the appropriate driver
        self.driver.get("http://127.0.0.1:5500/test.html")  # Replace with the actual login page URL

    def test_valid_login(self):
        driver = self.driver
        # Step 1: Enter valid credentials
        driver.find_element(By.ID, "username").send_keys("valid_user")
        driver.find_element(By.ID, "password").send_keys("valid_password")
        driver.find_element(By.ID, "login_button").click()

        # Step 2: Verify successful login
        time.sleep(2)  # Wait for the page to load
        self.assertIn("Dashboard", driver.title, "Login failed with valid credentials")

    def test_invalid_login(self):
        driver = self.driver
        # Step 1: Enter invalid credentials
        driver.find_element(By.ID, "username").send_keys("invalid_user")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.ID, "login_button").click()

        # Step 2: Verify error message
        time.sleep(2)  # Wait for the error message
        error_message = driver.find_element(By.ID, "error_message").text
        self.assertEqual(error_message, "Invalid username or password", "Error message mismatch")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

# Run the test case
if __name__ == "__main__":
    unittest.main()
