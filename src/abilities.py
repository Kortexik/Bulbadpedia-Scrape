from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
xp = By.XPATH 

url = 'https://bulbapedia.bulbagarden.net/wiki/Ability'
driver.get(url)

table = driver.find_elements(xp, "//*[@id='mw-content-text']/div[1]/table[9]/tbody/tr/td/table/tbody//tr//td//a[contains(@title, 'Ability')]")

list_of_abilities = []

for i in table:
    list_of_abilities.append(i.get_attribute('innerText'))


