# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

# Set user's email, password, and Instagram account to follow followers
USER_EMAIL = "EMAIL"
USER_PASSWORD = "PASS"
ACCOUNT = "_rl9"

class InstaFollower:
    def __init__(self):
        # Initialize Chrome webdriver and open Instagram login page
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/accounts/login/")

    def login(self):
        # Wait for login page to load
        time.sleep(5)

        # Click on accept cookies button
        cookies = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        cookies.click()

        # Wait for cookies to be accepted
        time.sleep(3)

        # Enter user's email and password to log in
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        login.send_keys(USER_EMAIL)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(USER_PASSWORD)
        password.send_keys(Keys.ENTER)

        # Wait for login to complete
        time.sleep(5)

        # Click on not now for notifications
        notifications = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notifications.click()

    def find_followers(self):
        # Wait for page to load and navigate to specified Instagram account
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}")

        # Wait for account page to load
        time.sleep(5)

        # Click on followers button
        followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        # Wait for followers list to load
        time.sleep(2)

    def follow(self):
        # Loop through followers and click follow button
        for num in range(1, 100):
            time.sleep(3)
            follow_button = self.driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{num}]/div/div/div/div[3]/div/button')
            if follow_button.text == "Obserwuj":
                follow_button.click()
            else:
                pass

# Create instance of InstaFollower class and execute methods
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
