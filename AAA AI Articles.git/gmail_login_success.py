# import requests
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# 
# # Start a new browser instance
# browser = webdriver.Chrome(ChromeDriverManager().install())
# 
# # Navigate to a website
# url = "https://google.com"
# browser.get(url)
# 
# # Get cookies from the browser and convert them to a format compatible with `requests`
# selenium_cookies = browser.get_cookies()
# cookie_jar = {cookie["name"]: cookie["value"] for cookie in selenium_cookies}
# 
# # Get headers (e.g., User-Agent) and create a headers dictionary
# headers = {
#     "User-Agent": browser.execute_script("return navigator.userAgent;")
# }
# 
# # Close the browser
# browser.quit()
# 
# # Send a request with the cookies and headers
# response = requests.get(url, headers=headers, cookies=cookie_jar)
# 
# # Print the response content
# print(response.text)
#


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
# import time
# 
# # Replace with your Google Account credentials
# email = "aqsakhanlahore8@gmail.com"
# password = "rooftop1234$"
# 
# # Start a new browser instance
# browser = webdriver.Chrome(ChromeDriverManager().install())
# 
# # Navigate to the Google login page
# browser.get("https://accounts.google.com/signin")
# 
# # Enter email and proceed
# browser.implicitly_wait(4)
# email_field = browser.find_element_by_id("identifierId").click()
# console.log(email_field )
# email_field.send_keys(email)
# email_field.send_keys(Keys.ENTER)
# time.sleep(3)  # Wait for the password input to appear
# 
# # Enter password and submit
# password_field = browser.find_element_by_name("password")
# password_field.send_keys(password)
# password_field.send_keys(Keys.ENTER)
# time.sleep(5)  # Wait for the login process to complete
# 
# # Visit a website
# url = "https://bing.com"
# browser.get(url)
# 
# # Your browsing activity will now be recorded in your Google Account
# 
# # Close the browser when done
# browser.quit()



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# 
# # Replace with your Google Account credentials
# email = "aqsakhanlahore8@gmail.com"
# password = "rooftop1234$"
# 
# # Start a new browser instance using a Service object
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# 
# # Navigate to the Google login page
# driver.get("https://accounts.google.com/signin")
# driver.maximize_window()
# 
# # Enter email and proceed
# email_field = driver.find_element(By.ID, "identifierId")
# email_field.send_keys(email, Keys.ENTER)
# 
# # Wait for the password input to appear
# wait = WebDriverWait(driver, 60)
# element = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
# 
# # Enter password and submit
# password_field = driver.find_element(By.NAME, "password")
# password_field.send_keys(password)
# 
# # Click the submit button
# submit_button = driver.find_element(By.XPATH, "//span[@class='RveJvd snByac']")
# submit_button.click()
# 
# # Add any additional browsing actions here

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# import os
# 
# # Set the path to your Chrome user profile (replace "YourUserName" with your actual username)
# chrome_user_data_dir = r"C:\Users\imran\AppData\Local\Google\Chrome\User Data"
# 
# # Create Chrome options with the user profile
# chrome_options = Options()
# chrome_options.add_argument(f"--user-data-dir={chrome_user_data_dir}")
# 
# # Start a new browser instance using a Service object and Chrome options
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)
# wait = WebDriverWait(driver, 60)
# # Navigate to a website
# 
# 
# url = "https://bing.com"
# print(url)
# driver.get(url)
# 
# # Your browsing activity will now be recorded in your Google Account
# 
# # Close the browser when done
# driver.quit()


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# 
# options = webdriver.ChromeOptions()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--remote-debugging-port=9222")
# 
# # Use ChromeDriverManager to automatically download and manage the correct ChromeDriver version
# browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
# 
# # Navigate to a website
# url = "https://bing.com"
# browser.get(url)
# 
# # Do your automation tasks here
# 
# # Close the browser
# browser.quit()



import pyautogui
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc


# email = "aqsakhanlahore8@gmail.com"
# password = "rooftop1234$"


user_id = "aqsakhanlahore8@gmail.com"
user_pw = "rooftop1234$"

options = uc.ChromeOptions()
# options.add_argument('--headless')
driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(15)

driver.get(url='https://accounts.google.com/signin/v2/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2F'
        '%3Fgws_rd%3Dssl&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

time.sleep(5)
pyautogui.write(user_id)
pyautogui.press('tab', presses=3)
pyautogui.press('enter')

time.sleep(10)
pyautogui.write(user_pw)
pyautogui.press('enter')


