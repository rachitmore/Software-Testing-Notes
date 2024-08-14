from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome("chromedriver.exe")

try:
    # Step 1: Open the Application URL
    driver.get("https://demo.opencart.com")
    
    # Step 2: Click on 'My Account' drop-down and select 'Login'
    my_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']"))
    )
    my_account.click()
    
    login_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_option.click()
    
    # Step 3: Click on the 'Forgotten Password' link
    forgotten_password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Forgotten Password"))
    )
    forgotten_password.click()
    
    # Step 4: Enter a registered email address
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-email"))
    )
    email_input.send_keys("pavanoltraining@gmail.com")
    
    # Step 5: Click the 'Continue' button
    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()
    
    # Step 6: Verify that a confirmation message is displayed
    confirmation_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success']"))
    )
    assert confirmation_message.is_displayed(), "Forgot Password failed, confirmation message not displayed."
    print("Test Passed: Forgot Password confirmation message displayed successfully.")
    
finally:
    # Close the browser
    driver.quit()
