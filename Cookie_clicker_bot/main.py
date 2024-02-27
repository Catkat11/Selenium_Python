# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open the Cookie Clicker game website
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find the cookie element
cookie = driver.find_element(By.ID, "cookie")

# Find all available items to purchase
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

# Set timeout for upgrades check
timeout = time.time() + 5
# Set timeout for 5 minutes
five_min = time.time() + 60*5

# Main loop for clicking the cookie and checking for upgrades
while True:
    cookie.click()

    # Check if it's time to check for upgrades
    if time.time() > timeout:
        # Find all item prices
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Extract prices from elements
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of upgrades with their prices as keys and IDs as values
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get the current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Create dictionary of affordable upgrades
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Print affordable upgrades and purchase them
        print(affordable_upgrades)
        for cost, to_purchase_id in reversed(affordable_upgrades.items()):
            time.sleep(0.03)
            try:
                driver.find_element(By.ID, to_purchase_id).click()
            except:
                continue

        # Reset timeout
        timeout = time.time() + 5

    # Check if it's time to stop the loop and print the cookies per second
    if time.time() > five_min:
        cookie_per_second = driver.find_element(By.ID, "cps").text
        print(cookie_per_second)
        break
