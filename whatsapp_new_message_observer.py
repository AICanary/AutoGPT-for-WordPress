import pywhatkit
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace the following variables with your information
phone_number = "+923225153870"
chrome_driver_path = "/path/to/chromedriver"
new_message_script_path = "/path/to/new_message_script.py"
db_path = "/path/to/database.db"

# Configure the Chrome driver options
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=./chrome-data")
chrome_options.add_argument("--profile-directory=Default")

# Start the Chrome driver
driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait until the user logs in to WhatsApp Web
wait = WebDriverWait(driver, 300)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "._1awRl")))

# Connect to the database and create the messages table if it doesn't exist
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id TEXT, message TEXT)")
conn.commit()

# Continuously check for new messages from the specified phone number
while True:
    try:
        # Find the chat with the specified phone number
        chat = driver.find_element(By.XPATH, f"//span[@title='{phone_number}']")
        chat_id = chat.get_attribute("data-id")
        
        # Check if there are any new messages in the chat
        new_messages = chat.find_elements(By.XPATH, ".//span[@data-icon='unread']")
        
        if len(new_messages) > 0:
            # Process each new message
            for message in new_messages:
                # Get the message text
                message_text = message.find_element(By.XPATH, "..//span[@class='selectable-text']").\
                                get_attribute("innerHTML").strip()
                
                # Check if the message has already been processed
                c.execute("SELECT id FROM messages WHERE chat_id = ? AND message = ?", (chat_id, message_text))
                result = c.fetchone()
                if result is not None:
                    continue
                
                # Run the new message script
                pywhatkit.exec_script(new_message_script_path)
                
                # Store the message in the database
                c.execute("INSERT INTO messages (chat_id, message) VALUES (?, ?)", (chat_id, message_text))
                conn.commit()
                
                # Mark the message as read
                message.click()
    
    except Exception as e:
        print(e)
    
conn.close()
