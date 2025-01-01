from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_search_result():
    # Initialize WebDriver (Update the path if necessary)
    driver = webdriver.Chrome()

    try:
        # Step 1: Open google.com
        driver.get("https://www.google.com")
        driver.maximize_window()
        # time.sleep(2)

        # Step 2: Locate the search bar and type "fisat"
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("fisat")
        search_box.send_keys(Keys.RETURN)
        # time.sleep(1)

        # Step 3: Check if search results are displayed
        results = driver.find_elements(By.XPATH, "//div[@class='g']")
        if len(results) > 0:
            print("Test Passed: Search results are displayed.")
        else:
            print("Test Failed: No search results found.")
    except Exception as e:
        print(f"Test Failed: An error occurred - {e}")
    finally:
        # Close the browser
        driver.quit()

# Run the test case
test_search_result()
