from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


my_email = "YOUR EMAIL"
my_password = "YOUR PASSWORD"

service = Service("D:\softwares\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)
url = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"
driver.get(url)

username = driver.find_element(By.ID, "username")
username.send_keys(my_email)

password = driver.find_element(By.ID, "password")
password.send_keys(my_password)

submit_btn = driver.find_element(By.TAG_NAME, "div button")
submit_btn.send_keys(Keys.ENTER)

search_bar = driver.find_element(By.TAG_NAME, "div input")
search_bar.send_keys("Remote python jobs")
search_bar.send_keys(Keys.ENTER)


