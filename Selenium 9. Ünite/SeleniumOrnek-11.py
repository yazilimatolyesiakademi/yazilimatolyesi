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

    def AramaYap(self):
        print("Arama yapıyorum")
        try:
            print("İnput etiketleri aranıyor.")
            sleep(2)
            input_etiketleri = self.tarayici.find_elements_by_tag_name('input')
            input_etiketleri[1].send_keys("@Y4zilimAtolyesi")


        except:
            print("Arama yapılamadı!")

    def SayfaGir(self):
        print("Sayfaya tıklıyorum..")
        try:
            sayfaya_tikla = WebDriverWait(self.tarayici,10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                              '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div[3]/div/div/div/div/article/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/a')))

            sayfaya_tikla.click()

        except:
            print("Sayfaya Tıklayamadım!")

    def TwitBegen(self):
        print("Twitt beğenme işlemi başlıyor..")
        try:
            print("Aşağıya kaydırıyorum..")
            sleep(1.5)
            self.tarayici.execute_script("window.scrollTo(0,550)")

        except:
            print("Hata!")

        try:
            print("Beğenme işlemi başarılı.")
            begenme_butonu = WebDriverWait(self.tarayici,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/div/div[1]')))
            begenme_butonu.click()

        except:
            print("Beğenme işlemi başarısız oldu.")


twitt = Twitter(kullanici_adi, sifre)
twitt.TwitterGiris()
twitt.AramaYap()
twitt.SayfaGir()
twitt.TwitBegen()

