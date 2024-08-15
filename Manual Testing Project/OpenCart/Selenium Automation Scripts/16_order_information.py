from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome("chromedriver.exe")

try:
    # Step 1: Open the Application URL
    driver.get("https://demo.opencart.com")
    
    # Step 2: Log in as a registered user
    my_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']"))
    )
    my_account.click()
    
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_link.click()
    
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-email"))
    )
    email_input.send_keys("testuser@example.com")
    
    password_input = driver.find_element(By.ID, "input-password")
    password_input.send_keys("password")
    
    login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
    login_button.click()
    
    # Step 3: Navigate to the "Order History" page
    my_account.click()
    
    order_history_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Order History"))
    )
    order_history_link.click()
    
    # Step 4: View the details of a specific order
    order_list = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".table-responsive"))
    )
    orders = order_list.find_elements(By.XPATH, "//table/tbody/tr")
    assert len(orders) > 0, "No orders found in order history."
    
    view_order_button = orders[0].find_element(By.XPATH, ".//a[text()='View']")
    view_order_button.click()
    
    # Step 5: Verify the order information
    order_details = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "content"))
    )
    
    # Verify order ID
    order_id = order_details.find_element(By.XPATH, "//h1[contains(text(),'Order ID')]").text
    assert "Order ID" in order_id, "Order ID is not displayed correctly."
    
    # Verify order status
    order_status = order_details.find_element(By.XPATH, "//td[text()='Order Status']/following-sibling::td").text
    assert order_status != "", "Order status is not available."
    
    # Verify payment and shipping details
    payment_address = order_details.find_element(By.XPATH, "//h3[text()='Payment Address']/following-sibling::address").text
    shipping_address = order_details.find_element(By.XPATH, "//h3[text()='Shipping Address']/following-sibling::address").text
    assert payment_address != "", "Payment address is missing."
    assert shipping_address != "", "Shipping address is missing."
    
    # Verify that products in the order are displayed
    product_list = order_details.find_elements(By.XPATH, "//table[@class='table table-bordered table-hover']/tbody/tr")
    assert len(product_list) > 0, "No products found in the order."
    
    # Verify product details (e.g., name, quantity, price)
    for product in product_list:
        product_name = product.find_element(By.XPATH, ".//td[1]").text
        quantity = product.find_element(By.XPATH, ".//td[3]").text
        price = product.find_element(By.XPATH, ".//td[4]").text
        assert product_name != "", "Product name is missing."
        assert quantity != "", "Product quantity is missing."
        assert price != "", "Product price is missing."
    
    print("Test Passed: Order Information verified successfully.")
    
finally:
    # Close the browser
    driver.quit()
