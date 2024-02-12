import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configure logging
logging.basicConfig(filename='log/LOGIN.txt' , level=logging.INFO , format='%(asctime)s - %(levelname)s - %(message)s')

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
    logging.info(step_description)
    print(step_description)

try:
    log_step("Clicking on the login button")
    driver.find_element(By.CLASS_NAME, "loginbtn").click()

    log_step("Entering email")
    foremail = driver.find_element(By.ID, "email")
    foremail.send_keys("login044@yopmail.com")

    log_step("Entering password")
    forpassword = driver.find_element(By.ID, "password")
    forpassword.send_keys("Test@123")

    log_step("Clicking on the login button")
    driver.find_element(By.ID, "login_btn").click()

    log_step("Waiting for 6 seconds after successful login")
    time.sleep(6)

    log_step("Searching for a hotel")
    value = driver.find_element(By.ID, "avl-location")
    value.send_keys("Magnuson Hotel Sandy Lodge Newquay, Hilgrove Road, Newquay, UK")
    time.sleep(2)

    log_step("Clicking on the search button")
    search_hotel = driver.find_element(By.XPATH, "//button[text()='Search']")
    search_hotel.click()
    time.sleep(3)

    log_step("Refreshing the page")
    driver.refresh()
    time.sleep(8)

    log_step("Clicking on a hotel link")
    driver.find_element(By.LINK_TEXT, "Magnuson Hotel Sandy Lodge Newquay").click()
    time.sleep(4)

    log_step("Clicking on a button")
    driver.find_element(By.XPATH, '//*[@id="hotel-detail-page"]/div[1]/div/div/div[1]/a').click()
    time.sleep(2)

    log_step("Clicking on a button")
    driver.find_element(By.XPATH,'//*[@id="roomsanchor"]/div/div[1]/div[2]/div/div[2]/div/a').click()
    time.sleep(6)

    log_step("Clicking on a button")
    driver.find_element(By.ID,"NextBtnForIMA").click()
    time.sleep(2)

    log_step("Clicking on a checkbox")
    driver.find_element(By.ID,"checkbox1").click()

    log_step("Clicking on a button")
    driver.find_element(By.ID,"reserve-button").click()

    log_step("Switching to iframe")
    iframeforCC = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/form/div[1]/fieldset[2]/div[1]/div/iframe")
    driver.switch_to.frame(iframeforCC)

    log_step("Entering Credit Card value")
    CC_Value = driver.find_element(By.XPATH, "/html/body/form/input")
    CC_Value.send_keys("0#@#@#@#")
    driver.switch_to.default_content()

    log_step("Entering name")
    name = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/form/div[1]/fieldset[1]/div/input")
    name.send_keys("%#%&%#&%&")

    log_step("Entering month")
    enter_month = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/form/div[1]/fieldset[2]/div[2]/input[1]")
    enter_month.send_keys("#$")

    log_step("Entering year")
    enter_year = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/form/div[1]/fieldset[2]/div[2]/input[2]")
    enter_year.send_keys("$%")

    log_step("Switching to iframe")
    iframe_CVV = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/form/div[1]/fieldset[2]/div[3]/div/iframe")
    driver.switch_to.frame(iframe_CVV)

    log_step("Entering CVV value")
    CVV_value = driver.find_element(By.XPATH,"/html/body/form/input")
    CVV_value.send_keys(1)
    driver.switch_to.default_content()

    log_step("Clicking on a button")
    driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/form/div[3]/button").click()

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")

