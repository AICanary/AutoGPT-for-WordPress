# from auto_whatsapp import auto_whatsapp
# 
# msg = 'This is a test message'
# users = [ "+92 3236040937"]
# auto_whatsapp.sendChat(users, msg)




# import pywhatkit as pw
# 
# # Authenticate with your WhatsApp account
# pw.sendwhatmsg_instantly("+923164760604", "Hello, World!", wait_time=10)
# 
# # Define a listener function to handle incoming messages
# def on_message_received(message):
#     print(f"Received message: {message}")
# 
# # Start the message loop to continuously monitor for incoming messages

import time
from selenium import webdriver
import pywhatkit as pw
def whatsapp(to, message):
    person = [to]
    string = message
    chrome_driver_binary = "chromedriver.exe"
    # Selenium chromedriver path
    driver = webdriver.Chrome(chrome_driver_binary)
    driver.get("https://web.whatsapp.com/")
    #wait = WebDriverWait(driver,10)
    time.sleep(30)
    for name in person:
        print('IN')
        user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
        user.click()
        print(user)
        for _ in range(10):
            text_box = driver.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            text_box.send_keys(string)
            sendbutton = driver.find_elements_by_xpath(
                '//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            sendbutton.click()
            
whatsapp("+923164760604", "Hello, World!")