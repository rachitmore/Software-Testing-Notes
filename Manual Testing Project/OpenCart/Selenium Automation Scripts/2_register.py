from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome("chromedriver.exe")

try:
    # Step 1: Open the Application URL
    driver.get("https://demo.opencart.com")
    
    # Step 2: Click on 'My Account' drop-down and select 'Register'
    my_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']"))
    )
    my_account.click()
    
    register_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
    )
    register_option.click()
    
    # Step 3: Fill in the required fields
    driver.find_element(By.ID, "input-firstname").send_keys("John")
    driver.find_element(By.ID, "input-lastname").send_keys("Doe")
    driver.find_element(By.ID, "input-email").send_keys("johndoe@example.com")
    driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    driver.find_element(By.ID, "input-password").send_keys("P@ssw0rd")
    driver.find_element(By.ID, "input-confirm").send_keys("P@ssw0rd")
    
    # Step 4: Agree to the Privacy Policy
    driver.find_element(By.NAME, "agree").click()
    
    # Step 5: Click the 'Continue' button
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    
    # Step 6: Verify that the registration is successful
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Your Account Has Been Created!']"))
    )
    assert success_message.is_displayed(), "Registration failed, success message not displayed."
    print("Test Passed: Registration successful.")
    
finally:
    # Close the browser
    driver.quit()
