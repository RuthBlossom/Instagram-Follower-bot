from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Instagram account to follow its followers
SIMILAR_ACCOUNT = "cutestcats"

# Your Instagram username and password
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"


class InstaFollower:
    def __init__(self):
        # Configure Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        # Path to ChromeDriver executable
        chrome_driver_path = "C:\\chromedriver.exe"  # double backslashes for Windows file path

        # Create and configure the Chrome webdriver with the specified path to ChromeDriver
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    def login(self):
        # Open Instagram login page
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4)

        # Dismiss the cookie warning if present
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Accept']").click()
        except:
            pass

        # Find and fill the username and password fields
        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        # Press Enter to submit the login form
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        # Wait for the page to load
        time.sleep(5)

        # Open the followers page of the specified Instagram account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(5)

    def follow(self):
        # Scroll down the followers list to load more followers
        for _ in range(5):
            self.driver.execute_script("window.scrollBy(0, 1000)")
            time.sleep(2)

        # Find all "Follow" buttons on the page and click them
        follow_buttons = self.driver.find_elements(By.XPATH, "//button[text()='Follow']")
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(2)
            # Handle the case when clicking a button is intercepted by another element
            except ElementClickInterceptedException:
                # Click "Cancel" if the "Follow" button is intercepted
                self.driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
                time.sleep(1)


# Create an instance of the InstaFollower class
bot = InstaFollower()

# Login to Instagram
bot.login()

# Find the followers of the specified Instagram account
bot.find_followers()

# Follow the followers of the specified Instagram account
bot.follow()

