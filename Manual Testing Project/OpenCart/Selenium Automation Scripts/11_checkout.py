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
    
    # Step 4: Add the product to the shopping cart
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-cart"))
    )
    add_to_cart_button.click()
    
    # Wait for the success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "Success: You have added" in success_message.text, "Product was not added to the cart."
    
    # Step 5: Proceed to the checkout process
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cart"))
    )
    cart_button.click()
    
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))
    )
    checkout_button.click()
    
    # Step 6: Log in as a registered user
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-email"))
    )
    email_input.send_keys("testuser@example.com")
    
    password_input = driver.find_element(By.ID, "input-password")
    password_input.send_keys("password")
    
    login_button = driver.find_element(By.ID, "button-login")
    login_button.click()
    
    # Step 7: Complete the billing, shipping, and payment details
    
    # Step 7.1: Billing Details
    billing_continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-payment-address"))
    )
    billing_continue_button.click()
    
    # Step 7.2: Delivery Details
    delivery_continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-shipping-address"))
    )
    delivery_continue_button.click()
    
    # Step 7.3: Delivery Method
    delivery_method_continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-shipping-method"))
    )
    delivery_method_continue_button.click()
    
    # Step 7.4: Payment Method
    agree_terms_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "agree"))
    )
    agree_terms_checkbox.click()
    
    payment_method_continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-payment-method"))
    )
    payment_method_continue_button.click()
    
    # Step 8: Confirm the order and verify the success message
    confirm_order_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-confirm"))
    )
    confirm_order_button.click()
    
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Your order has been placed!']"))
    )
    assert success_message.is_displayed(), "Order confirmation message is not displayed."
    
    print("Test Passed: Checkout process is working as expected.")
    
finally:
    # Close the browser
    driver.quit()
