from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
tarayici.get("https://demoga.com/iframe-practice-page/")
tarayici.maximize_window()

try:
    print("Frame ekranına geçiyorum..")
    element = tarayici.find_element_by_name("iframe1")
    tarayici.find_element_by_xpath("//*[@id='primary-menu']/li[2]/ul/li[1]/a").click()

except:
    print("Tıklama işlemi başarısız oldu!!")

try:
    print("Ana sayfaya geçiyorum..")
    tarayici.switch_to_default_content()

except:
    print("Hata!")

sleep(3)
tarayici.quit()