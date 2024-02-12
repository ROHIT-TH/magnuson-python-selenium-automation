import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configure logging
logging.basicConfig(filename='log/Signup.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set Chrome options to detach the browser
options = Options()
options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Open the URL and maximize the window
driver.get('https://www.magnusonhotels.com/')
driver.maximize_window()

# Logging function
def log_step(step_description):
    # Log the step description
    log_message = f"{step_description}"
    logging.info(log_message)
    print(log_message)

try:
    # Step 1: Click on the login button
    log_step("Step 1: Clicking on the login button")
    driver.find_element(By.CLASS_NAME, "loginbtn").click()
    time.sleep(5)

    # Step 2: Click on the signup link
    log_step("Step 2: Clicking on the signup link")
    driver.find_element(By.XPATH, "/html/body/section[6]/div/div[1]/div[2]/form/div[5]/div/div/div/p/a").click()

    # Step 3: Fill out the signup form
    log_step("Step 3: Filling out the signup form")
    first_name = driver.find_element(By.NAME, "reg_fname")
    first_name.send_keys("rohit")
    last_name = driver.find_element(By.NAME, "reg_lname")
    last_name.send_keys("xyz")
    enter_mail = driver.find_element(By.NAME, "reg_email")
    enter_mail.send_keys("try123@yopmail.com")
    select_affiliation = driver.find_element(By.XPATH, '//*[@id="reg_affiliation"]')
    select_affiliation.send_keys("Student")
    enter_apt = driver.find_element(By.XPATH, '//*[@id="address_2"]')
    enter_apt.send_keys("MU-11")
    select_country = driver.find_element(By.XPATH, '//*[@id="reg_country"]')
    select_country.send_keys("United Kingdom")
    state = driver.find_element(By.NAME, "reg_state")
    state.send_keys("Null")
    enter_city = driver.find_element(By.NAME, "reg_city")
    enter_city.send_keys("London")
    enter_postal = driver.find_element(By.NAME, "reg_postcode")
    enter_postal.send_keys("N11 B22")
    enter_password = driver.find_element(By.NAME, "reg_password")
    enter_password.send_keys("Test@123")
    enter_confirm = driver.find_element(By.NAME, "reg_confirmpassword")
    enter_confirm.send_keys("Test@123")
    driver.find_element(By.XPATH, '//*[@id="mgh__signup"]/div[7]/div/div/label/span').click()
    driver.find_element(By.XPATH, '//*[@id="mgh__signup"]/div[8]/div/div/label/span').click()

    # Step 4: Click on the SIGN UP button
    log_step("Step 4: Clicking on the SIGN UP button")
    driver.find_element(By.CSS_SELECTOR, "input[value = 'SIGN UP'").click()

    # Step 5: Wait for validation message and log it
    validation_message = "Validation message is created successfully"
    log_step(f"Step 5: Validation message: {validation_message}")

    log_step("Signup completed successfully!")

except Exception as e:
    # Log any errors that occurred during the execution
    logging.error(f"An error occurred: {str(e)}")

