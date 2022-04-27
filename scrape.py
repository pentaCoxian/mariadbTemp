from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pandas as pd

import login_config #import credentials


# Chrome settings
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito") #don't want cache

service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service, options= chrome_options)
url = "https://campus.icu.ac.jp/icumap/ehb/SearchCO.aspx"

# Open site (will be sent to SSO login)
driver.get(url)
driver.implicitly_wait(3)

# Login to ICU SSO
driver.find_element(By.ID,"username_input").send_keys(login_config.username)
driver.find_element(By.ID,"password_input").send_keys(login_config.password)
driver.find_element(By.ID,"login_button").click()
driver.implicitly_wait(3)

select_element = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_ddlPageSize")
select_object = Select(select_element)
select_object.select_by_visible_text("ALL")