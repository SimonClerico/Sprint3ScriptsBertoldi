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


linkMARCAS = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]")
linkMARCAS.click()
time.sleep(2)


#Imagen logo "ALFAPARF"
logoALFAPARF= driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div[1]/div/div/div/div[1]").is_displayed()
if logoALFAPARF == True:
	print ("El logo de la marca ALFAPARF se visualiza correctamente")
else:
	print ("No se visualiza el logo de la marca ALFAPARF")



#Imagen logo "BonmetiQue"
logoBonmetiQue= driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div[1]/div/div/div/div[2]").is_displayed()
if logoBonmetiQue == True:
	print ("El logo de la marca BonmetiQue se visualiza correctamente")
else:
	print ("No se visualiza el logo de la marca BonmetiQue")


#Imagen logo "LOREAL"
logoLOREAL= driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div[1]/div/div/div/div[3]").is_displayed()
if logoLOREAL == True:
	print ("El logo de la marca LOREAL se visualiza correctamente")
else:
	print ("No se visualiza el logo de la marca LOREAL")



#Imagen logo "REMINGTON"
logoREMINGTON= driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div[1]/div/div/div/div[4]").is_displayed()
if logoREMINGTON == True:
	print ("El logo de la marca REMINGTON se visualiza correctamente")
else:
	print ("No se visualiza el logo de la marca REMINGTON")

#HOME
driver.get(website)
time.sleep(2)