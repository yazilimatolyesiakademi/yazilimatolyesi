from selenium import webdriver
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")

try:
    tarayici.get("https://www.yazilimatolyesiakademi.com/")
    tarayici.maximize_window()
except:
    print("Belirtilen url açılamıyor!")

try:
    print("Sayfa başlığı: " + tarayici.title)

except:
    print("Sayfa başlığı alınamadı!")

try:
    print("Sayfa URL: {}".format(tarayici.current_url))

except:
    print("Sayfa URL alınamadı!")

sleep(2)
tarayici.quit()

