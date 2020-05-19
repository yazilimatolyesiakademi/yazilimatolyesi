from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
tarayici.get("http://canilgu.com")
tarayici.maximize_window()

try:
    tarayici.find_element_by_xpath("//*[@id='work']/div/a[2]").click()
    sleep(3)

except:
    print("Tıklama işlemi başarısız oldu!")

try:
    sleep(2)
    print("İlk sekmeye geçiyorum..")
    tarayici.window_handles
    tarayici.switch_to_window(tarayici.window_handles[0])

except:
    print("Hata!")

sleep(3)
tarayici.quit()