from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
import argparse

# example to run: python3 your_script_name.py your_username your_password "Body Power" "Salil"
parser = argparse.ArgumentParser(description="Automate booking process with Selenium.")
parser.add_argument("username", help="Your username for login.")
parser.add_argument("password", help="Your password for login.")
parser.add_argument("course_name", help="Name of the course to search for.")
parser.add_argument("instructor_name", help="Name of the instructor to search for.")
args = parser.parse_args()


# serv = Service('/snap/bin/firefox.geckodriver')
# driver = webdriver.Firefox(service=serv)
driver = webdriver.Firefox()

# driver.get('https://engine.surfconext.nl/authentication/idp/single-sign-on/key:20230503?SAMLRequest=fVLLbtswEPwVgXfqQb8awnLgxghqIEVdW%2BmhN4ZaOUSlpcqlUufvS8mPuD34QpC7w5ndnZ3fH5o6egNHxmLOsjhlEaC2pcF9zp6LR%2F6J3S%2FmpJpatHLZ%2BVfcwu8OyEfhI5I8ZnLWOZRWkSGJqgGSXsvd8uuTFHEqW2e91bZm0ZIInA9SDxapa8DtwL0ZDc%2Fbp5y9et%2BSTBJtEUH7mDpXhTscfIx1Utu9wWSQS4hsYk2pcc%2BiVajFoPJD%2FWcKwACG%2FxhUqB7QGz2AE1O2CYU2a%2BBk9shD6Be8S5GKUTpJRyx6tE7D0HLOKlUTsGi9ytly%2B12MZ7O76o5neiz4uBRTrtJU8WpSaYBJJUrIApaogzWSV%2Bhz1tPyLOViVGSZFFOZzeLJbPqTRZvTdD4bPE791ihfjiCSX4piwzffdgWLfpzdCwB28koO6u7apNvE6uwMW9z0YZ5c8182Y6dtG%2Brqmzm8P9iubzljl%2FRpZ8CtV4s%2F8MKptS68eOUsesAyDitSdrrXj0uoK9%2Bf2jYfgv9yXIIn3Y%2FA9You%2FgI%3D&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=OQxYKmiPz%2F7L7HF8GGazPHfnUd5jYutrx4VJ%2F7mL3JWGl9O200sFoeIJmqGpc%2Fm82eWH1kvXFcuzixxgQRsSn%2Bvv0qNR40zZmMBb70h%2FL01QsFcNNzI0MIVOTN0gla3um0qFgNHNKy%2BevHNwBdbQuGG0hk%2FomgnrL%2BG0%2FaCK8RmlsbeWJTNuPgRfD4uAqZFpriI46vziJ%2FW05tXPKyjQm82jSPzApjkbjOzwSuaqhR481R5ts%2B3CPEkAETKfUwBmbONiikLhMg9XM6RivbJOe0WvfRrbyL%2FU1yMl49s9fwy3uhkRYLSElduXutsE8GRIZaEmeMxVzMZ1lXpgM5DEzg%3D%3D')
driver.get('https://www.tudelft.nl/x/aanbod/x-abonnement')

wait = WebDriverWait(driver, 20)  # Set the maximum wait time for 20 seconds

# Scroll down the webpage by a specific amount, e.g., 500 pixels
# Some monitors resolution cannot fit the button onload
driver.execute_script("window.scrollBy(0,500)")

# Wait for the button to be clickable and then click
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn:nth-child(3)"))).click()

# Switch to the new tab/window
driver.switch_to.window(driver.window_handles[1])

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-lg:nth-child(1)"))).click()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.remaining:nth-child(1) > div:nth-child(1) > div:nth-child(2)"))).click()

username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
username_field.send_keys(args.username)
password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
password_field.send_keys(args.password)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit_button"))).click()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.nav-item:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2)"))).click()

search_field = wait.until(EC.presence_of_element_located((By.ID, 'tag-searchfield')))
search_field.send_keys(args.course_name)
time.sleep(2)
search_field.send_keys(Keys.ENTER)  # Press enter on the keyboard

while True:
    try:
        sleep_duration = random.uniform(6, 8)  # Random sleep time between 7 to 10 seconds
        time.sleep(sleep_duration)
        course_element = driver.find_element(By.XPATH, f"//*[contains(text(), '{args.instructor_name}')]")

        # Check if the correct parent container of "Salil" does not have "disabled opacity-50" attributes
        if "disabled opacity-50" not in course_element.find_element(By.XPATH, "./ancestor::div[6]").get_attribute("class"):
            # Locate the button inside the container of the "Salil" class and click it
            course_button = course_element.find_element(By.XPATH, "./ancestor::div[6]//button[contains(@data-test-id, 'bookable-slot')]")
            course_button.click()
            time.sleep(5)
            # Find the "Book" button by its data-test-id attribute and click it
            book_button = driver.find_element(By.XPATH, "//button[@data-test-id='details-book-button']")
            book_button.click()
            time.sleep(600)
            driver.quit()

    except NoSuchElementException:  # Element not found
        driver.refresh()
        refresh_duration = random.uniform(0, 1)  # Random refresh time between 5 to 8 seconds
        time.sleep(refresh_duration)
        continue  # Skip the rest of the loop and start from the beginning
    
    driver.refresh()

