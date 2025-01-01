from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver (replace with your WebDriver path)
driver = webdriver.Chrome()

try:
    # Navigate to Amazon.in
    driver.get("https://www.amazon.in")
    
    # Maximize the browser window
    driver.maximize_window()

    # Find the search bar using XPath and search for "laptop"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='twotabsearchtextbox']"))
    )
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)
    
    # Wait for results to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']"))
        
    )

    # Locate product titles and prices
    titles = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")
    
    # Print the first few results
    print("Top results:")
    for i in range(min(len(titles), len(prices), 5)):  # Print up to 5 results
        print(f"{i+1}. {titles[i].text} - ₹{prices[i].text}")
    
finally:
    # Quit the WebDriver
    driver.quit()
