from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Replace with the browser WebDriver you are using

try:
    # Test Case 1: Open Amazon India and verify title
    driver.get("https://www.amazon.in")
    time.sleep(2)  # Wait for the page to load
    if "Amazon" in driver.title:
        print("Test Case 1: Open Amazon - PASS")
    else:
        print("Test Case 1: Open Amazon - FAIL")

    # Test Case 2: Search for iPhone
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("iPhone 14")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for search results
    try:
        results = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
        if results:
            print("Test Case 2: Search for iPhone - PASS")
        else:
            print("Test Case 2: Search for iPhone - FAIL (No results found)")
    except Exception as e:
        print("Test Case 2: Search for iPhone - FAIL", e)

    # Test Case 3: Click on the first product
    try:
        first_product = results[0]
        first_product.click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
        if "iPhone" in driver.title:
            print("Test Case 3: Open iPhone product page - PASS")
        else:
            print("Test Case 3: Open iPhone product page - FAIL (Incorrect page)")
    except Exception as e:
        print("Test Case 3: Open iPhone product page - FAIL", e)

    # Test Case 4: Add to Cart
    try:
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()
        time.sleep(3)
        cart_confirmation = driver.find_element(By.XPATH, "//h1[contains(text(), 'Added to Cart')]")
        if cart_confirmation:
            print("Test Case 4: Add to Cart - PASS")
        else:
            print("Test Case 4: Add to Cart - FAIL (No confirmation found)")
    except Exception as e:
        print("Test Case 4: Add to Cart - FAIL", e)

    # Test Case 5: Proceed to Buy
    try:
        proceed_to_buy_button = driver.find_element(By.NAME, "proceedToRetailCheckout")
        proceed_to_buy_button.click()
        time.sleep(3)
        if "Sign-In" in driver.title or "Checkout" in driver.title:
            print("Test Case 5: Proceed to Buy - PASS")
        else:
            print("Test Case 5: Proceed to Buy - FAIL (Failed to navigate to checkout)")
    except Exception as e:
        print("Test Case 5: Proceed to Buy - FAIL", e)

except Exception as e:
    print("Error during execution:", e)

finally:
    # Close the browser
    driver.quit()
