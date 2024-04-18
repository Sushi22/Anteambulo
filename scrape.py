from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up Selenium
options = Options()
options.add_argument("--headless")  # Run headless browser
driver = webdriver.Chrome(options=options)  # Make sure you have chromedriver installed and in your PATH
driver.get("https://cikibana.myntra.com/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(columns:!(),filters:!(),index:pimservice,interval:auto,query:(language:kuery,query:''),sort:!(!('@timestamp',desc)))")

# Wait for the page to load
time.sleep(5)  # You may need to adjust this depending on your internet speed

# Get the page source
page_source = driver.page_source

element_xpath = "/html/body/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div/button/span/span"
element = driver.find_element_by_xpath(element_xpath)

# Click on the element
element.click()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Now you can extract the data you need from the BeautifulSoup object
# For example, you can find elements by their class or tag and extract text

# Close the browser
driver.quit()