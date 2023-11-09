import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from dotenv import load_dotenv

load_dotenv()

RC_USERNAME = os.getenv("RC_USERNAME")
RC_PASSWORD = os.getenv("RC_PASSWORD")

RCTV_AUTH_USERNAME = os.getenv("RCTV_AUTH_USERNAME")
RCTV_AUTH_PASSWORD = os.getenv("RCTV_AUTH_PASSWORD")

# - start chrome in kiosk mode
options = webdriver.ChromeOptions()

# very important and crucial for our brand.
options.add_argument("--kiosk")
# rctogether shows 'do you want to receive notifications' dialog...! get rid.
options.add_argument("--disable-notifications")
# remove "chrome is controlled by automated software" message
options.add_experimental_option("excludeSwitches", ["enable-automation"])

service = webdriver.ChromeService(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)
# - go to recurse.rctogether.com
driver.get("https://recurse.rctogether.com")
# - waits to be on recurse.com
wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.current_url == "https://www.recurse.com/login")
# wait for input/password fields
wait.until(lambda driver: driver.find_element(By.ID, "email"))
# fill out email/password
driver.find_element(By.ID, "email").send_keys(RC_USERNAME)
driver.find_element(By.ID, "password").send_keys(RC_PASSWORD)
# click 'Log in' button -- <input with name="commit" and value="Log in"
driver.find_element(By.CSS_SELECTOR, "input[name='commit'][value='Log in']").click()
# - waits to be back at recurse.rctogether.com
wait.until(lambda driver: driver.current_url == "https://recurse.rctogether.com/")
# wait 5 seconds
driver.implicitly_wait(5)
# find the '_gridworld_session' cookie
cookie = driver.get_cookie("_gridworld_session")
# - changes cookie samesite (lax -> None)
cookie["sameSite"] = "None"
# delete cookie, add it back
driver.delete_cookie("_gridworld_session")
driver.add_cookie(cookie)
# wait 5 seconds again
driver.implicitly_wait(5)
# - go to user:pass@rctv.recurse.com/app/0 (with u/p from .env file as well)
driver.get(f"https://{RCTV_AUTH_USERNAME}:{RCTV_AUTH_PASSWORD}@rctv.recurse.com/app/1")

while True:
    # - TODO check connection to selenium (fetch driver.title ?), restart if broken? restart script? kill script and let service restart it?
    time.sleep(60)
    pass
