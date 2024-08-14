from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome("chromedriver.exe")

try:
    # Step 1: Open the Application URL
    driver.get("https://demo.opencart.com")
    
    # Step 2: Enter a product name or keyword in the search bar
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "search"))
    )
    search_input.send_keys("iPhone")
    
    # Step 3: Click the 'Search' button
    search_button = driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
    search_button.click()
    
    # Step 4: Verify that the search results page displays relevant products
    search_results = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Search - iPhone']"))
    )
    assert search_results.is_displayed(), "Search failed, search results not displayed."
    
    # Verify that at least one product is listed
    products_listed = driver.find_elements(By.CSS_SELECTOR, ".product-layout")
    assert len(products_listed) > 0, "Search failed, no products found."
    
    print("Test Passed: Search functionality is working as expected.")
    
finally:
    # Close the browser
    driver.quit()
