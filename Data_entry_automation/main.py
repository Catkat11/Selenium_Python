# Import necessary libraries
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Define header with user-agent and language preference
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Send a GET request to Zillow's rental page for Los Angeles
response = requests.get("https://www.zillow.com/los-angeles-ca/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A34.40378463935821%2C%22east%22%3A-117.9008682421875%2C%22south%22%3A33.63662251280971%2C%22west%22%3A-118.9225967578125%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D",
                        headers=header)

# Extract text data from the response
data = response.text
# Raise an exception if the response is not successful
response.raise_for_status()
# Parse the HTML data using BeautifulSoup
soup = BeautifulSoup(data, "html.parser")

# Extract all link elements for the rental listings
all_link_elements = soup.select(".ListItem-c11n-8-84-3__sc-10e22w8-0 a")
all_links = []

# Iterate through each link element and extract the href attribute
for link in all_link_elements:
    href = link["href"]
    # Check if the href attribute contains "http"
    if "http" not in href:
        # If not, prepend the Zillow domain to the href
        if f"https://www.zillow.com{href}" not in all_links:
            all_links.append(f"https://www.zillow.com{href}")
    else:
        # If it contains "http", simply append it to the list
        if href not in all_links:
            all_links.append(href)

# Extract all address elements for the rental listings
all_address_elements = soup.select(".StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0  a")
# Extract text from address elements, splitting on "|" and getting the last part
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

# Extract all price elements for the rental listings
all_price_elements = soup.select(".PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 span")
# Extract text from price elements, cleaning up formatting
all_prices = [price.get_text().split(" ")[0].split("+")[0].split("/")[0] for price in all_price_elements]

# Initialize a Chrome webdriver
driver = webdriver.Chrome()

# Iterate through each rental listing
for n in range(len(all_links)):
    # Open the Google Form link for data submission
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdrF4tr77nv-vMuAf7eOstNktIafNluviTj0M0s1j5fKXzxow/viewform?usp=sf_link")

    # Wait for 3 seconds to ensure page is fully loaded
    time.sleep(3)

    # Find and fill the address input field
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(all_addresses[n])

    # Find and fill the price input field
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(all_prices[n])

    # Find and fill the link input field
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(all_links[n])

    # Find and click the submit button
    button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    button.click()
