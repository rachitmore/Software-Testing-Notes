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
    
    # Step 3: Navigate to the "My Account" section
    my_account.click()
    
    # Step 4: Access the "Recurring Payments" page
    recurring_payments_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Recurring payments"))
    )
    recurring_payments_link.click()
    
    # Step 5: Verify the recurring payment history
    recurring_payments_table = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".table-responsive"))
    )
    recurring_payments = recurring_payments_table.find_elements(By.XPATH, "//table/tbody/tr")
    assert len(recurring_payments) > 0, "No recurring payments found in history."
    
    # Verify details of the first recurring payment
    first_payment_description = recurring_payments[0].find_element(By.XPATH, ".//td[1]").text
    first_payment_status = recurring_payments[0].find_element(By.XPATH, ".//td[4]").text
    assert first_payment_description != "", "Recurring payment description is missing."
    assert first_payment_status != "", "Recurring payment status is missing."
    
    print("Test Passed: Recurring Payments history verified successfully.")
    
finally:
    # Close the browser
    driver.quit()
