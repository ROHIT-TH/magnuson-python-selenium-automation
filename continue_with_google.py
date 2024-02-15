import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set Chrome options to detach the browser
options = Options()
options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Open the URL and maximize the window
driver.get('https://www.magnusonhotels.com/')
driver.maximize_window()

# Click on the login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "loginbtn")))
login_button.click()

# Click on the 'Sign up now' link
signup_now_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[6]/div/div[1]/div[2]/form/div[5]/div/div/div/p/a")))
signup_now_link.click()

# Click on the 'Sign up with email' link
signup_with_email_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[6]/div/div[1]/div[3]/form/div[11]/div/div/a")))
signup_with_email_link.click()

# Click on the 'Next' button
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div/button/span")))
next_button.click()

# Enter the name
enter_name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "firstName")))
enter_name_input.send_keys("Magnuson_User")

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[2]/div/div/div/div/button/span").click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div[2]/select/option[8]"))).click()

# Select date
enter_date_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/input")))
enter_date_input.send_keys("25")

# Select year
enter_year_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[3]/div/div/div[1]/div/div[1]/input")))
enter_year_input.send_keys("1998")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/select/option[3]"))).click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[2]/div/div[1]/div/div/button/span"))).click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/span/div[1]/div/div[1]/div/div[3]/div"))).click()

driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()

time.sleep(2)

Pass = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input")
Pass.send_keys("Test@123")

Confirm = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
Confirm.send_keys("Test@123")

driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[1]/div/form/span/section/div/div/div/div[3]/div/div[1]/div/div/div[1]/div/input").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div[2]/div[2]/div/div[2]/div/div/div/div/button/span"))).click()
