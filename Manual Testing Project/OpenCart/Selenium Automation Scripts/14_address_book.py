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
    
    # Step 3: Navigate to the "Address Book" page
    my_account.click()
    
    address_book_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Address Book"))
    )
    address_book_link.click()
    
    # Step 4: Add a new address
    new_address_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "New Address"))
    )
    new_address_button.click()
    
    first_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-firstname"))
    )
    first_name_input.send_keys("John")
    
    last_name_input = driver.find_element(By.ID, "input-lastname")
    last_name_input.send_keys("Doe")
    
    address_1_input = driver.find_element(By.ID, "input-address-1")
    address_1_input.send_keys("123 Main St")
    
    city_input = driver.find_element(By.ID, "input-city")
    city_input.send_keys("New York")
    
    postcode_input = driver.find_element(By.ID, "input-postcode")
    postcode_input.send_keys("10001")
    
    country_dropdown = driver.find_element(By.ID, "input-country")
    country_dropdown.send_keys("United States")
    
    region_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "input-zone"))
    )
    region_dropdown.send_keys("New York")
    
    default_address_checkbox = driver.find_element(By.NAME, "default")
    default_address_checkbox.click()
    
    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()
    
    # Step 5: Verify the success message for adding the address
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "Your address has been successfully added" in success_message.text, "Address was not added successfully."
    
    # Step 6: Edit the existing address
    edit_address_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Edit']"))
    )
    edit_address_button.click()
    
    first_name_input.clear()
    first_name_input.send_keys("Jane")
    
    last_name_input.clear()
    last_name_input.send_keys("Smith")
    
    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()
    
    # Step 7: Verify the success message for editing the address
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "Your address has been successfully updated" in success_message.text, "Address was not updated successfully."
    
    # Step 8: Delete an address
    delete_address_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete']"))
    )
    delete_address_button.click()
    
    # Step 9: Verify the success message for deleting the address
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "Your address has been successfully deleted" in success_message.text, "Address was not deleted successfully."
    
    print("Test Passed: Address Book operations (add, edit, delete) were successful.")
    
finally:
    # Close the browser
    driver.quit()
