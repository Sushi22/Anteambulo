from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--headless")  
driver = webdriver.Chrome(options=options)  
driver.get("https://cikibana.myntra.com/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(columns:!(),filters:!(),index:pimservice,interval:auto,query:(language:kuery,query:''),sort:!(!('@timestamp',desc)))")

time.sleep(5)  

page_source = driver.page_source

element_xpath = "/html/body/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div/button/span/span"

element = driver.find_element_by_xpath(element_xpath)

element.click()

soup = BeautifulSoup(page_source, "html.parser")

driver.quit()