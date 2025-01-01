from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH

try:
    # Test Case 1: Open Flipkart and close the login popup
    driver.get("https://www.flipkart.com")
    time.sleep(2)  # Wait for the page to load
    try:
        close_login_popup = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_login_popup.click()
        print("Test Case 1: Login popup closed - PASS")
    except Exception as e:
        print("Test Case 1: Login popup closed - FAIL", e)

    # Test Case 2: Search for a product
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for search results
    try:
        results = driver.find_elements(By.CLASS_NAME, "_4rR01T")
        if results:
            print("Test Case 2: Product search - PASS")
        else:
            print("Test Case 2: Product search - FAIL (No results found)")
    except Exception as e:
        print("Test Case 2: Product search - FAIL", e)

    # Test Case 3: Open a product page
    try:
        first_product = results[0]
        first_product.click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
        if "laptop" in driver.title.lower():
            print("Test Case 3: Open product page - PASS")
        else:
            print("Test Case 3: Open product page - FAIL (Incorrect product page)")
    except Exception as e:
        print("Test Case 3: Open product page - FAIL", e)

    # Test Case 4: Add to cart
    try:
        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
        add_to_cart_button.click()
        time.sleep(3)
        print("Test Case 4: Add to cart - PASS")
    except Exception as e:
        print("Test Case 4: Add to cart - FAIL", e)

    # Test Case 5: Logout (if applicable)
    try:
        # Assuming the user is logged in
        user_menu = driver.find_element(By.XPATH, "//div[contains(text(),'My Account')]")
        user_menu.click()
        logout_button = driver.find_element(By.XPATH, "//div[contains(text(),'Logout')]")
        logout_button.click()
        time.sleep(2)
        print("Test Case 5: Logout - PASS")
    except Exception as e:
        print("Test Case 5: Logout - FAIL (User might not be logged in)", e)

except Exception as e:
    print("Error during execution:", e)

finally:
    # Close the browser
    driver.quit()
