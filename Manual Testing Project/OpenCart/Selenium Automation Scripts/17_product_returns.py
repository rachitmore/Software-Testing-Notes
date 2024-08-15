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
    
    # Step 4: Select an order to return
    order_list = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".table-responsive"))
    )
    orders = order_list.find_elements(By.XPATH, "//table/tbody/tr")
    assert len(orders) > 0, "No orders found in order history."
    
    view_order_button = orders[0].find_element(By.XPATH, ".//a[text()='View']")
    view_order_button.click()
    
    return_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Return']"))
    )
    return_button.click()
    
    # Step 5: Fill in the return form
    reason_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "return_reason_id"))
    )
    reason_dropdown.click()
    
    reason_dropdown.find_element(By.XPATH, "//option[contains(text(),'Dead On Arrival')]").click()
    
    opened_checkbox = driver.find_element(By.XPATH, "//input[@name='opened'][@value='1']")
    opened_checkbox.click()
    
    comment_textarea = driver.find_element(By.XPATH, "//textarea[@name='comment']")
    comment_textarea.send_keys("The product was defective upon arrival.")
    
    agree_checkbox = driver.find_element(By.NAME, "agree")
    agree_checkbox.click()
    
    continue_button = driver.find_element(By.XPATH, "//input[@value='Submit']")
    continue_button.click()
    
    # Step 6: Verify the success message for the return request
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "Thank you for submitting your return request" in success_message.text, "Return request was not submitted successfully."
    
    print("Test Passed: Product return request submitted successfully.")
    
finally:
    # Step 7: Close the browser
    driver.quit()
