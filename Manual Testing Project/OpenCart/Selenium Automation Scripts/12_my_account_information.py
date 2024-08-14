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
    
    # Step 3: Navigate to "My Account Information"
    my_account.click()
    
    account_info_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))
    )
    account_info_link.click()
    
    edit_account_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Edit your account information"))
    )
    edit_account_link.click()
    
    # Step 4: Update the account details
    first_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-firstname"))
    )
    first_name_input.clear()
    first_name_input.send_keys("NewFirstName")
    
    last_name_input = driver.find_element(By.ID, "input-lastname")
    last_name_input.clear()
    last_name_input.send_keys("NewLastName")
    
    email_input = driver.find_element(By.ID, "input-email")
    email_input.clear()
    email_input.send_keys("newemail@example.com")
    
    telephone_input = driver.find_element(By.ID, "input-telephone")
    telephone_input.clear()
    telephone_input.send_keys("123456789")
    
    # Step 5: Save the changes and verify the success message
    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()
    
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "Success: Your account has been successfully updated." in success_message.text, "Account information was not updated successfully."
    
    # Step 6: Verify that the updated information is reflected correctly
    account_info_link.click()  # Navigate back to account information
    
    first_name_value = driver.find_element(By.ID, "input-firstname").get_attribute("value")
    last_name_value = driver.find_element(By.ID, "input-lastname").get_attribute("value")
    email_value = driver.find_element(By.ID, "input-email").get_attribute("value")
    telephone_value = driver.find_element(By.ID, "input-telephone").get_attribute("value")
    
    assert first_name_value == "NewFirstName", "First name was not updated correctly."
    assert last_name_value == "NewLastName", "Last name was not updated correctly."
    assert email_value == "newemail@example.com", "Email was not updated correctly."
    assert telephone_value == "123456789", "Telephone was not updated correctly."
    
    print("Test Passed: My Account Information is updated and verified successfully.")
    
finally:
    # Close the browser
    driver.quit()
