import logging
import os
import time
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials and URLs from environment variables
LOGIN_URL = os.getenv('LOGIN_URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
SUCCESS_URL = os.getenv('SUCCESS_URL')

# Ensure all required environment variables are set
if not all([LOGIN_URL, USERNAME, PASSWORD, SUCCESS_URL]):
    raise ValueError("One or more environment variables are not set")

# Set up logging
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/login_script.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def login_to_website():
    logging.info('Initializing Chrome WebDriver.')

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")

    # Path to ChromeDriver
    chrome_driver_path = '/usr/bin/chromedriver'
    service = Service(executable_path=chrome_driver_path)

    # Initialize the WebDriver (for Chrome)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        logging.info('Navigating to the login page.')
        driver.get(LOGIN_URL)
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))

        # Find all input elements with the class name 'form-control'
        form_elements = driver.find_elements(By.CLASS_NAME, 'form-control')

        # Filter elements by input type
        username_field = None
        password_field = None
        for element in form_elements:
            input_type = element.get_attribute('type')
            if input_type == 'text':
                username_field = element
            elif input_type == 'password':
                password_field = element

        # Ensure both fields were found
        if not username_field or not password_field:
            raise Exception("Username or password field not found")

        # Fill the username and password fields
        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait to ensure the login is processed
        WebDriverWait(driver, 10).until(EC.url_changes(LOGIN_URL))
        
        # Check for successful login
        current_url = driver.current_url
        if current_url == SUCCESS_URL:
            logging.info('Login successful.')
        else:
            logging.warning(f'Login failed or redirected to an unexpected URL: {current_url}')

    except Exception as e:
        logging.error(f'An error occurred: {e}', exc_info=True)

    finally:
        # Close the browser
        logging.info('Closing the browser.')
        driver.quit()

# Schedule the login task to run every 24 hours
schedule.every(24).hours.do(login_to_website)

# Initial call to log in immediately
login_to_website()

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
