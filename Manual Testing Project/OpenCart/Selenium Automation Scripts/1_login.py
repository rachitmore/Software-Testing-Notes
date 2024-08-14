from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome('chromedriver.exe')

try:
    # Step 1: Open the Application URL
    driver.get("https://demo.opencart.com")
    
    # Step 2: Click on 'My Account' drop-down
    my_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']"))
    )
    my_account.click()
    
    # Step 3: Click on 'Login'
    login_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_option.click()
    
    # Step 4: Enter valid email address and password
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-email"))
    )
    email_input.send_keys("pavanoltraining@gmail.com")
    
    password_input = driver.find_element(By.ID, "input-password")
    password_input.send_keys("P@ssw0rd")
    
    # Step 5: Click on the 'Login' button
    login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
    login_button.click()
    
    # Step 6: Verify that the user is successfully logged in
    account_header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='My Account']"))
    )
    assert account_header.is_displayed(), "Login failed, 'My Account' page not displayed."
    print("Test Passed: User successfully logged in.")
    
finally:
    # Close the browser
    driver.quit()
