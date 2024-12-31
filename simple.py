from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (ensure the correct WebDriver executable is in your PATH or provide its location)
driver = webdriver.Chrome()

try:
    # Navigate to the localhost page
    driver.get("http://127.0.0.1:5501/dashboard.html")  # Replace 8000 with the correct port if different
    
    # Locate the h3 tag
    h3_element = driver.find_element(By.TAG_NAME, "h3")
    
    # Assert if the text is 'Hello'
    if h3_element.text.strip() == "Hello":
        print("Test Passed: <h3> contains 'Hello'")
    else:
        print(f"Test Failed: <h3> contains '{h3_element.text}' instead of 'Hello'")
finally:
    # Close the browser
    driver.quit()
