from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome("chromedriver.exe")

try:
    # Step 1: Open the Application URL
    driver.get("https://demo.opencart.com")
    
    # Step 2: Search for the first product and add it to the comparison list
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "search"))
    )
    search_input.send_keys("iPhone")
    search_button = driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
    search_button.click()
    
    add_to_compare_iphone = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-original-title='Compare this Product']"))
    )
    add_to_compare_iphone.click()
    
    # Wait for the success message
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    
    # Step 3: Search for the second product and add it to the comparison list
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys("MacBook")
    search_button.click()
    
    add_to_compare_macbook = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-original-title='Compare this Product']"))
    )
    add_to_compare_macbook.click()
    
    # Wait for the success message
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    
    # Step 4: Navigate to the comparison page
    compare_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "product comparison"))
    )
    compare_link.click()
    
    # Step 5: Verify that the selected products are displayed for comparison
    comparison_table = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "content"))
    )
    
    # Check that both products are in the comparison table
    assert "iPhone" in comparison_table.text, "iPhone is not in the comparison table."
    assert "MacBook" in comparison_table.text, "MacBook is not in the comparison table."
    
    print("Test Passed: Both products are successfully added to the comparison list.")
    
finally:
    # Close the browser
    driver.quit()
