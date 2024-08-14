from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome("chromedriver.exe")

try:
    # Step 1: Open the Application URL
    driver.get("https://demo.opencart.com")
    
    # Step 2: Search for a product (e.g., "iPhone")
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "search"))
    )
    search_input.send_keys("iPhone")
    search_button = driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
    search_button.click()
    
    # Step 3: Click on the product to view its details
    product_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "iPhone"))
    )
    product_link.click()
    
    # Step 4: Verify that the product details page is displayed
    product_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='iPhone']"))
    )
    assert product_name.is_displayed(), "Product name is not displayed on the product details page."
    
    # Verify that the product price is displayed
    product_price = driver.find_element(By.XPATH, "//h2[text()='$123.20']")
    assert product_price.is_displayed(), "Product price is not displayed on the product details page."
    
    # Verify that the product availability is displayed
    availability = driver.find_element(By.XPATH, "//li[contains(text(), 'Availability')]")
    assert availability.is_displayed(), "Product availability is not displayed on the product details page."
    
    print("Test Passed: Product Display Page is showing correct information.")
    
finally:
    # Close the browser
    driver.quit()
