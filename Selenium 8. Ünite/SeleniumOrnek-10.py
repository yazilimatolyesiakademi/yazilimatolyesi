from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

kullanici_adi = "kullanici_adi"  # input("Lütfen twitter kullanici adinizi giriniz: ")
sifre = "kullanici_sifre"  # input("Şifrenizi giriniz: ")


class Twitter:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
        self.tarayici.maximize_window()
        self.tarayici.get("https://twitter.com/login")

    def TwitterGiris(self):
        try:
            print("Kullanıcı adı giriliyor.")
            kullaniciadiGir = WebDriverWait(self.tarayici, 10).until(
                EC.visibility_of_element_located((By.NAME, 'session[username_or_email]')))
            kullaniciadiGir.send_keys(self.kullanici_adi)

            print("Şifre giriliyor.")
            sifreGir = WebDriverWait(self.tarayici, 10).until(
                EC.visibility_of_element_located((By.NAME, 'session[password]')))
            sifreGir.send_keys(self.sifre)

            print("Enter tuşuna basıyorum.")
            sifreGir.send_keys(Keys.ENTER)

        except:
            print("Kullanıcı Adı Girilemedi!")
