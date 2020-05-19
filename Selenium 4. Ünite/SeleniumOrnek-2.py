from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
tarayici.get("https://www.yazilimatolyesiakademi.com/")
tarayici.maximize_window()


try:
    arama_butonu = tarayici.find_element_by_xpath("//*[@id='vce_main_navigation_menu']/li[8]/a/i")
    arama_butonu.click()

except:
    print("Arama butonu tıklayamadım!")

try:
    arama_metni = tarayici.find_element_by_xpath("//*[@id='ce_main_navigation_menu']/li[8]/ul/li/form/input")
    arama_metni.click()
    arama_metni.send_keys("Python")
    arama_metni.send_keys(Keys.ENTER)

except:
    print("Arama yapılamadı!")

tarayici.quit()
