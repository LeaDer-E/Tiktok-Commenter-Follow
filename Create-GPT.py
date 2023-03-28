import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new ChromeOptions object
options = Options()

# Add the argument to run Chrome in headless mode
options.add_argument('--headless')

# Add the argument to use a fake user agent
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

# Add the argument to disable images loading
options.add_argument('blink-settings=imagesEnabled=false')

# Set the window size to 1920x1080
options.add_argument('--window-size=1920,1080')

# Set the maximum time to wait for a page to load
options.page_load_strategy = 'eager'

# Create a new Chrome webdriver with the options
driver = webdriver.Chrome(options=options)

# setup undetected chromedriver
driver = uc.Chrome()

# Going to signup / login page
driver.get("https://chat.openai.com/")



start_num = 0  # Initialize the starting number


def Start():
    # Locate the input tag with Tag NAme: Input
    wait = WebDriverWait(driver, 10)
    input_tag = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'input')))
    while True:
        for i in range(start_num, 1000000): # Loop through numbers starting from the previous number or 000000 to 999999
            try:
                # Try entering the number 3 times, with a pause of 0.4 seconds between each attempt
                for j in range(3):
                    try:
                        try:
                            input_tag.clear() # Clear the input tag before entering a new value
                            input_tag.send_keys(f"{i:06d}") # Format the number with leading zeros and enter it into the input tag
                            time.sleep(0.4) # pause the program for 0.4 seconds between every number
                            break
                        except:
                            time.sleep(1) # is used to pause the program for 1 second in case an error occurs
                    except:
                        try:
                            input_tag.clear() # Clear the input tag before entering a new value
                            input_tag.send_keys(f"{i:06d}") # Format the number with leading zeros and enter it into the input tag
                            time.sleep(0.4) #pause the program for 0.4 seconds between every number
                            break
                        except:
                            time.sleep(1) # is used to pause the program for 1 second in case an error occurs.
                else:
                    # If all tries fail, print an error message, and i'm sorry to told you that but u maybe ave to restart the program :D
                    print(f"Error: failed to enter value {i:06d}")
            except:
                # Try entering the number 3 times, with a pause of 0.4 seconds between each attempt
                for j in range(3):
                    try:
                        try:
                            input_tag.clear() # Clear the input tag before entering a new value
                            input_tag.send_keys(f"{i:06d}") # Format the number with leading zeros and enter it into the input tag
                            time.sleep(0.4) # pause the program for 0.4 seconds between every number
                            break
                        except:
                            time.sleep(1) # is used to pause the program for 1 second in case an error occurs
                    except:
                        try:
                            input_tag.clear() # Clear the input tag before entering a new value
                            input_tag.send_keys(f"{i:06d}") # Format the number with leading zeros and enter it into the input tag
                            time.sleep(0.4) #pause the program for 0.4 seconds between every number
                            break
                        except:
                            time.sleep(1) # is used to pause the program for 1 second in case an error occurs.
                else:
                    # If all tries fail, print an error message, and i'm sorry to told you that but u maybe ave to restart the program :D
                    print(f"Error: failed to enter value {i:06d}")