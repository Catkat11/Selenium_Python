# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# Set LinkedIn account credentials and phone number for job applications
ACCOUNT_EMAIL = "EMAIL"
ACCOUNT_PASSWORD = "PASS"
NUMBER = "333333333"

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open LinkedIn job search page for Python developer positions in Katowice area
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3616254230&f_LF=f_AL&geoId=90009829&keywords=python%20developer&location=Katowice%20i%20okolice&refresh=true")

# Click on the login button
login_button = driver.find_element(By.LINK_TEXT, "Zaloguj się")
login_button.click()

# Wait for login page to load
time.sleep(5)

# Enter email and password to log in
username = driver.find_element(By.ID, "username")
username.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

# Wait for login to complete
time.sleep(5)

# Find all job listings on the page
all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

# Iterate through each job listing
for job in all_jobs:
    print("Trying")
    job.click()
    time.sleep(5)

    try:
        # Click on easy apply button if available
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        easy_apply.click()

        # Wait for apply modal to load
        time.sleep(5)

        # Enter phone number if prompted
        number = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
        if number.text == "":
            number.send_keys(NUMBER)

        # Click on appropriate submit button based on application complexity
        submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            # If application is complex, skip and close modal
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            # If application is straightforward, submit and close modal
            submit_button.click()
            time.sleep(2)
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()

    except NoSuchElementException:
        print("Exception occurred, skipping job.")
        continue

# Wait before quitting the driver
time.sleep(5)
driver.quit()
