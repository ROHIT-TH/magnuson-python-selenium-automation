import logging
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Create a timestamp for the log file name
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_name = f'selenium_logs_{timestamp}.log'



# ghfdhgf
# Configure logging
logging.basicConfig(filename='log/Forget_password.txt', level=logging.INFO, format='%(message)s')

# Set Chrome options to detach the browser
options = Options()
options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Function to log HTML element details
def log_element_on_click(locator, by):
    element = driver.find_element(by, locator)
    element_tag_name = element.tag_name
    logging.info(f"Clicked on element '{locator}' with Tag Name: {element_tag_name}, Locator: {by}")

try:
    # Open the URL and maximize the window
    driver.get('https://www.magnusonhotels.com/')
    driver.maximize_window()

    # Clicking on the login button
    log_element_on_click(".loginbtn", By.CLASS_NAME)

    # Clicking on the forgot password link
    log_element_on_click("/html/body/section[6]/div/div[1]/div[2]/form/div[2]/div[2]/div/a", By.XPATH)

    # Entering email for password reset
    log_element_on_click("forgotemail", By.ID)

    # Clicking on the reset button
    log_element_on_click("/html/body/section[6]/div/div[1]/div[4]/form/div[2]/div/div/input", By.XPATH)

    time.sleep(5)

    # Open a new tab
    driver.execute_script("window.open('about:blank', '_blank');")

    # Switch to the second tab
    driver.switch_to.window(driver.window_handles[1])

    # Open the second URL in the second tab
    driver.get('https://www.yopmail.com')

    # Entering email for reset on Yopmail
    log_element_on_click("login", By.ID)

    # Clicking on the reset submit button
    log_element_on_click("/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div/div[4]/button/i", By.XPATH)

    time.sleep(10)

    # Switching to iframe for reset email
    iframe_reset = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div[3]/div/div[1]/iframe")
    driver.switch_to.frame(iframe_reset)

    # Clicking on the reset link
    log_element_on_click("/html/body/main/div/div/div/center/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table[3]/tbody/tr/td/table/tbody/tr/td/a", By.XPATH)

    driver.switch_to.default_content()

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
    print(f"An error occurred: {str(e)}")
