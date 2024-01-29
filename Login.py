from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.magnusonhotels.com/')
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "loginbtn").click()
# Enter email
foremail = driver.find_element(By.ID, "email")
foremail.send_keys("login04@yopmail.com")
# Enter password
forpassword = driver.find_element(By.ID, "password")
forpassword.send_keys("Test@123")
# Click on the login button
driver.find_element(By.ID, "login_btn").click()
# Wait for 10 seconds after successful login
time.sleep(6)
# Now, you can perform other actions after login
# For example, click on another button or navigate to another page
value = driver.find_element(By.ID,"avl-location")
value.send_keys("Magnuson Hotel Sandy Lodge Newquay, Hilgrove Road, Newquay, UK")
time.sleep(2)
search_hotel = driver.find_element(By.XPATH,"//button[text()='Search']")
search_hotel.click()
time.sleep(3)
driver.refresh()
time.sleep(8)
driver.find_element(By.LINK_TEXT,"Magnuson Hotel Sandy Lodge Newquay").click()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="hotel-detail-page"]/div[1]/div/div/div[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="roomsanchor"]/div/div[1]/div[2]/div/div[2]/div/a').click()
time.sleep(6)
driver.find_element(By.ID,"NextBtnForIMA").click()
time.sleep(2)
driver.find_element(By.ID,"checkbox1").click()
driver.find_element(By.ID,"reserve-button").click()
iframeforCC = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/form/div[1]/fieldset[2]/div[1]/div/iframe")
driver.switch_to.frame(iframeforCC)
CC_Value = driver.find_element(By.XPATH, "/html/body/form/input")
CC_Value.send_keys("0000 0000 0000 0000000")
driver.switch_to.default_content()
name = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/form/div[1]/fieldset[1]/div/input")
name.send_keys("%#%&%#&%&")
enter_month = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/form/div[1]/fieldset[2]/div[2]/input[1]")
enter_month.send_keys("#$")
enter_year = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/form/div[1]/fieldset[2]/div[2]/input[2]")
enter_year.send_keys("$%")
iframe_CVV = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/form/div[1]/fieldset[2]/div[3]/div/iframe")
driver.switch_to.frame(iframe_CVV)
CVV_value = driver.find_element(By.XPATH,"/html/body/form/input")
CVV_value.send_keys("^$%")
driver.switch_to.default_content()







