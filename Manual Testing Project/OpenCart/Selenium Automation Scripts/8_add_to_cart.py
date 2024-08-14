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
    
    # Step 4: Click the "Add to Cart" button
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-cart"))
    )
    add_to_cart_button.click()
    
    # Wait for the success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "Success: You have added" in success_message.text, "Product was not added to the cart."
    
    # Step 5: Verify that the product is added to the cart by checking the cart summary
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cart"))
    )
    cart_button.click()
    
    cart_items = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@class='dropdown-menu pull-right']//a[text()='iPhone']"))
    )
    assert cart_items.is_displayed(), "Product is not visible in the cart."
    
    print("Test Passed: Product was successfully added to the cart.")
    
finally:
    # Close the browser
    driver.quit()
