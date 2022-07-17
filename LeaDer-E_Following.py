#login Information
username = "E-mail@Address.com"
password = "Your Pretty Password Here"

######################################################################################################################
#Links
Vid1 = ('https://www.tiktok.com/@to 100 commenters follow')
Vid2 = ('https://www.tiktok.com/@to 200 commenters follow')
Vid3 = ('https://www.tiktok.com/@to 300 commenters follow')
Vid4 = ('https://www.tiktok.com/@to 400 commenters follow')
Vid5 = ('https://www.tiktok.com/@to 500 commenters follow')
Vid6 = ('https://www.tiktok.com/@to 600 commenters follow')
Vid7 = ('https://www.tiktok.com/@to 700 commenters follow')
Vid8 = ('https://www.tiktok.com/@to 800 commenters follow')
Vid9 = ('https://www.tiktok.com/@to 900 commenters follow')
Vid10 = ('https://www.tiktok.com/@to 1000 commenters follow')

######################################################################################################################

print('#I hope you like this tool, and it be useful for you to use it, and you can support me at: "www.buymeacoffee.com/LeaDer.E"')
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import  Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import *
from selenium.webdriver import *
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.relative_locator import locate_with
import time
import logging
import os
import time
import random
import time
import undetected_chromedriver.v2 as uc
import undetected_chromedriver as uc
import os
from pathlib import Path
options = Options()

######################################################################################################################

#Browser Choosen
browser_name = "undetectable"
if browser_name == "chrome":
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    #options.add_argument("user-data-dir=/home/eslammustafa/.config/google-chrome/Default")
    options.headless = True
    driver = webdriver.Chrome(executable_path="/home/leader/Desktop/Python Workstation/Tiktok Follower/chromedriver", chrome_options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
elif browser_name == "firefox":
    driver = webdriver.Firefox(executable_path="/home/eslammustafa/Desktop/PY Projects/geckodriver")
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options= options)

elif browser_name == "undetectable":
    chrome_options = uc.ChromeOptions()
    driver = uc.Chrome(use_subprocess=True,
    options=chrome_options,
    seleniumwire_options={}
    )
    #driver = uc.Chrome()
    #options = uc.ChromeOptions()

elif browser_name == 'stealth':
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=r"/home/eslammustafa/Desktop/PY Projects/chromedriver")
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

else:
    print ("Please pass the correct browser name: " + browser_name)

######################################################################################################################

#Scrolling
def Scrolling():
    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 4000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 6000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 8000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 10000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 12000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 14000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 16000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 18000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 20000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 22000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 24000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 26000)")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 28000)")
    driver.execute_script("window.scrollTo(0, 5000)")
    driver.execute_script("window.scrollTo(0, 0)")

######################################################################################################################

#Press Follow
def Press():
    try:
        driver.find_element(By.CSS_SELECTOR, "#app > div.tiktok-ywuvyb-DivBodyContainer.e1irlpdw0 > div.tiktok-w4ewjk-DivShareLayoutV2.elmjn4l0 > div > div.tiktok-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2.elmjn4l2 > div.tiktok-1gk89rh-DivShareInfo.ekmpd5l2 > div.tiktok-1hdrv89-DivShareTitleContainer.ekmpd5l3 > div > div.tiktok-1h3j14u-DivFollowButtonWrapper.e18e4obn4 > button").click()
        print('[♥] Follow Done [>.-]')
        driver.back()
    except NoSuchElementException:
        print('[+] Already Following [^,^]')
        driver.back()

######################################################################################################################

#Followers
def Followers():
    #Follow No.(1)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[1]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(2)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[2]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(3)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[3]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[3]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(4)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[4]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[4]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(5)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[5]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[5]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(6)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[6]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[6]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(7)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[7]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[7]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(8)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[8]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[8]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(9)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[9]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[9]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(10)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[10]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[10]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(11)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[11]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[11]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(12)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[12]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[12]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(13)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[13]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[13]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(14)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[14]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[14]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(15)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[15]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[15]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(16)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[16]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[16]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(17)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[17]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[17]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(18)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[18]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[18]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(19)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[19]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[19]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(20)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[20]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[20]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(21)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[21]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[21]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(22)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[22]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[22]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(23)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[23]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[23]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(24)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[24]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[24]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(25)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[25]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[25]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(26)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[26]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[26]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(27)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[27]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[27]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(28)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[28]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[28]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(29)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[29]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[29]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(30)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[30]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[30]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(31)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[31]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[31]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(32)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[32]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[32]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(33)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[33]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[33]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(34)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[34]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[34]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(35)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[35]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[35]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(36)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[36]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[36]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(37)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[37]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[37]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(38)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[38]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[38]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(39)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[39]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[39]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(40)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[40]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[40]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(41)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[41]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[41]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(42)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[42]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[42]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(43)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[43]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[43]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(44)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[44]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[44]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(45)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[45]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[45]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(46)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[46]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[46]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(47)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[47]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[47]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(48)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[48]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[48]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(49)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[49]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[49]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(50)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[50]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[50]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(51)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[51]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[51]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(52)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[52]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[52]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(53)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[53]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[53]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(54)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[54]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[54]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(55)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[55]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[55]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(56)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[56]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[56]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(57)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[57]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[57]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(58)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[58]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[58]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(59)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[59]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[59]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(60)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[60]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[60]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(61)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[61]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[61]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(62)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[62]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[62]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(63)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[63]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[63]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(64)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[64]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[64]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(65)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[65]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[65]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(66)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[66]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[66]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(67)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[67]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[67]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(68)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[68]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[68]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(69)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[69]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[69]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(70)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[70]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[70]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(71)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[71]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[71]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(72)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[72]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[72]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(73)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[73]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[73]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(74)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[74]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[74]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(75)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[75]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[75]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(76)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[76]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[76]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(77)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[77]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[77]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(78)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[78]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[78]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(79)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[79]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[79]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(80)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[80]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[80]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(81)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[81]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[81]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(82)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[82]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[82]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(83)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[83]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[83]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(84)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[84]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[84]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(85)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[85]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[85]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(86)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[86]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[86]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(87)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[87]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[87]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(88)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[88]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[88]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(89)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[89]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[89]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(90)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[90]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[90]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(91)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[91]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[91]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(92)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[92]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[92]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(93)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[93]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[93]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(94)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[94]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[94]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(95)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[95]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[95]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(96)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[96]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[96]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(97)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[97]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[97]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(98)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[98]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[98]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(99)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[99]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[99]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()

    #Follow No.(100)
    time.sleep(3)
    Scrolling()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/div[100]/div[1]/div[1]/a").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[100]/div[1]/div[1]/a").click()
        time.sleep(2)
    Press()



######################################################################################################################

#Login
url1 = ('https://www.tiktok.com/login/phone-or-email/email')
driver.get(url1)
time.sleep(2)
print('login process...')
password1 = driver.find_element(By.CSS_SELECTOR, '#loginContainer > div.tiktok-xabtqf-DivLoginContainer.exd0a430 > form > div.tiktok-15iauzg-DivContainer.ewblsjs0 > div > input')
password1.send_keys(password)
print('password done')
username1 = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[3]/input')
username1.send_keys(username)
print('email done')
print('Login Succsessfull')
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/form/button").click()
time.sleep(30)

######################################################################################################################

#startup
driver.get(Vid1)
print ("Going to Vedio No.: [1]..")
time.sleep(5)
Followers()

driver.get(Vid2)
print ("Going to Vedio No.: [2]..")
time.sleep(5)
Followers()

driver.get(Vid3)
print ("Going to Vedio No.: [3]..")
time.sleep(5)
Followers()

driver.get(Vid4)
print ("Going to Vedio No.: [4]..")
time.sleep(5)
Followers()

driver.get(Vid5)
print ("Going to Vedio No.: [5]..")
time.sleep(5)
Followers()

driver.get(Vid6)
print ("Going to Vedio No.: [6]..")
time.sleep(5)
Followers()

driver.get(Vid7)
print ("Going to Vedio No.: [7]..")
time.sleep(5)
Followers()

driver.get(Vid8)
print ("Going to Vedio No.: [8]..")
time.sleep(5)
Followers()

driver.get(Vid9)
print ("Going to Vedio No.: [9]..")
time.sleep(5)
Followers()

driver.get(Vid10)
print ("Going to Vedio No.: [10]..")
time.sleep(5)
Followers()
