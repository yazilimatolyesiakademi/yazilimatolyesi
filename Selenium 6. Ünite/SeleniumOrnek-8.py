from selenium import webdriver
from selenium.webdriver.common import By
from selenium.webdriver.common.keys import Keys
from time import sleep

tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
tarayici.get("https://www.yemeksepeti.com/kktc")
#tarayici.get("https://twitter.com/login")
#tarayici.get("https://www.google.com.tr/")
#tarayici.get("http://canilgu.com")
#tarayici.get("https://selenium-python.readthedocs.io/locating-elements.html")



tarayici.maximize_window()

element = tarayici.find_element(By.NAME, 'session[username_or_email]')
# element = tarayici.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
# element = tarayici.find_element(By.LINK_TEXT, 'English')
# element = tarayici.find_element(By.PARTIAL_LINK_TEXT, 'Engli')



sleep(2)
element.send_keys("canilgu@gmail.com")
#element.click()

#try:
#   element = tarayici.find_element(By.TAG_NAME, 'h1')
    # element = tarayici.find_elements(By.CLASS_NAME, 'about-me')
    # element = tarayici.find_elements(By.CSS_SELECTOR, 'ul.simple')

    #print("Element Bulundu!")
    #print(element[0].text)
    #tarayici.quit()
#except:
#    print("Hata!")
#    tarayici.quit()


sleep(3)
tarayici.quit()

