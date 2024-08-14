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
    
    # Enter valid email address and password
    driver.find_element(By.ID, "input-email").send_keys("pavanoltraining@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("P@ssw0rd")
    
    # Click on the 'Login' button
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    
    # Step 3: Click on 'My Account' drop-down and select 'Logout'
    my_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']"))
    )
    my_account.click()
    
    logout_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    )
    logout_option.click()
    
    # Step 4: Verify that the logout is successful
    logout_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Account Logout']"))
    )
    assert logout_message.is_displayed(), "Logout failed, success message not displayed."
    print("Test Passed: Logout successful.")
    
finally:
    # Close the browser
    driver.quit()
