import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""seteamos el webdriver"""
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains

website = "https://bertoldi.com.ar/"


driver.maximize_window()
time.sleep(2)
driver.get(website)

#linkMARCAS
linkMARCAS = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]")
linkMARCAS.click()
time.sleep(2)


#linkALFAPARF
linkALFAPARF = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div[1]/div/div/div/div[1]")
linkALFAPARF.click()
time.sleep(2)

#Redireccionamiento logo "ALFAPARF"
if driver.current_url == "https://bertoldi.com.ar/collections/evolution-en-alfaparf":
        print("El logo de la marca ALFAPARF redirecciona correctamente")
else:
	print ("El logo de la marca ALFAPARF no redirecciona correctamente")

#HOME
driver.get(website)
time.sleep(2)


#linkMARCAS
linkMARCAS = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]")
linkMARCAS.click()
time.sleep(2)

#linkBonmetiQue
linkBonmetiQue = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div[1]/div/div/div/div[2]")
linkBonmetiQue.click()
time.sleep(2)

#Redireccionamiento logo "BonmetiQue"
if driver.current_url == "https://bertoldi.com.ar/collections/bonmetique-professionnel":
        print("El logo de la marca BonmetiQue redirecciona correctamente")
else:
	print ("El logo de la marca BonmetiQue no redirecciona correctamente")

#HOME
driver.get(website)
time.sleep(2)


#linkMARCAS
linkMARCAS = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]")
linkMARCAS.click()
time.sleep(2)

#linkLoreal
linkLoreal = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div[1]/div/div/div/div[3]")
linkLoreal.click()
time.sleep(2)

#Redireccionamiento logo "Loreal"
if driver.current_url == "https://bertoldi.com.ar/collections/serie-expert":
        print("El logo de la marca Loreal redirecciona correctamente")
else:
	print ("El logo de la marca Loreal no redirecciona correctamente")

#HOME
driver.get(website)
time.sleep(2)


#linkMARCAS
linkMARCAS = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]")
linkMARCAS.click()
time.sleep(2)

#linkRemington
linkRemington = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div[1]/div/div/div/div[4]")
linkRemington.click()
time.sleep(2)

#Redireccionamiento logo "Remington"
if driver.current_url == "https://bertoldi.com.ar/collections/vendors?q=Remington":
        print("El logo de la marca Remington redirecciona correctamente")
else:
	print ("El logo de la marca Remington no redirecciona correctamente")

#HOME
driver.get(website)
time.sleep(2)