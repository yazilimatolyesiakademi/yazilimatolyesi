from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
tarayici.get("https://www.google.com.tr")
tarayici.maximize_window()

tarayici.find_element_by_name('q').send_keys("yazilim atölyesi akademi",Keys.ENTER)
tarayici.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a').click()

sleep(2)
tarayici.back()
tarayici.back()

tarayici.quit()