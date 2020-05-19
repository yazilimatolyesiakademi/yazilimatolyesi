from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
tarayici.get("https://www.facebook.com/")
tarayici.maximize_window()

try:
    element = tarayici.find_element_by_name("email")
    element.send_keys("canilgu@hotmail.com", Keys.PAGE_DOWN)

    sleep(3)
    element.send_keys(Keys.PAGE_UP)
    sleep(3)
    element.clear()

except:
    print("Email girilemedi!")

tarayici.quit()
