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
    password_input.send_keys("oldpassword")
    
    login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
    login_button.click()
    
    # Step 3: Navigate to "Change Password"
    my_account.click()
    
    password_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Password"))
    )
    password_link.click()
    
    # Step 4: Update the password
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-password"))
    )
    password_input.clear()
    password_input.send_keys("newpassword")
    
    confirm_password_input = driver.find_element(By.ID, "input-confirm")
    confirm_password_input.clear()
    confirm_password_input.send_keys("newpassword")
    
    # Step 5: Save the changes and verify the success message
    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()
    
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "Success: Your password has been successfully updated." in success_message.text, "Password was not updated successfully."
    
    # Step 6: Log out and log in again with the new password to verify the update
    my_account.click()
    
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    )
    logout_link.click()
    
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
    password_input.send_keys("newpassword")
    
    login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
    login_button.click()
    
    # Verify that the login is successful with the new password
    my_account = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='My Account']"))
    )
    assert my_account.is_displayed(), "Login with the new password was not successful."
    
    print("Test Passed: Password was successfully updated and verified.")
    
finally:
    # Close the browser
    driver.quit()
