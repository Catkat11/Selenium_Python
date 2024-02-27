# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

# Set user's email and password for Tinder login
USER_EMAIL = "YOUR_EMAIL"
USER_PASSWORD = "YOUR_PASSWORD"

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open Tinder website
driver.get("http://tinder.com/")

# Wait for page to load
time.sleep(3)

# Click on accept cookies button
cookies = driver.find_element(By.XPATH, '//*[@id="s-2082074848"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

# Wait for login button to load
time.sleep(3)

# Click on login with Facebook button
login = driver.find_element(By.XPATH, '//*[@id="s-2082074848"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

# Wait for Facebook login button to load
time.sleep(3)

# Click on login with Facebook button
facebook = driver.find_element(By.XPATH, '//*[@id="s484511372"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook.click()

# Wait for Facebook login popup window to load
time.sleep(3)

# Switch to Facebook login popup window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Click on accept cookies button in Facebook login popup
facebook_cookies = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[1]')
facebook_cookies.click()

# Enter Facebook email and password
time.sleep(1)
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(USER_EMAIL)

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(USER_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to main window
driver.switch_to.window(base_window)
print(driver.title)

# Wait for Tinder to ask for location access and notifications
time.sleep(15)

# Click on allow for location access
localization = driver.find_element(By.XPATH, '//*[@id="s484511372"]/main/div/div/div/div[3]/button[1]')
localization.click()

# Click on allow for notifications
notifications = driver.find_element(By.XPATH, '//*[@id="s484511372"]/main/div/div/div/div[3]/button[2]')
notifications.click()

# Swipe right (like) on profiles for 100 times
for n in range(100):
    time.sleep(3)
    try:
        print("Trying")

        # Click on like button
        like_button = driver.find_element(By.XPATH, '//*[@id="s-2082074848"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            # If match occurs, click on match popup
            match = driver.find_element(By.CSS_SELECTOR, '.itsAMatch a')
            match.click()

        except NoSuchElementException:
            time.sleep(3)

# Wait before quitting the driver
time.sleep(3)
driver.quit()
