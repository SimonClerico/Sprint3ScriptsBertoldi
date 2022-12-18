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


linkGiftCard = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[3]")
linkGiftCard.click()
time.sleep(2)


#SCROLL
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(2)


#FILTROS

#FILTROLISTA
filtroLista = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[1]")
filtroLista.click()
time.sleep(2)

ValidacionLista= driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[1]").is_enabled();
if ValidacionLista == True:
	print ("El filtro de lista funciona correctamente")
else:
	print ("El filtro no funciona correctamente")


#FILTROGRID2
filtroGrid2 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[2]")
filtroGrid2.click()
time.sleep(2)

ValidacionGrid2= driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[2]").is_enabled();
if ValidacionGrid2 == True:
	print ("El filtro Grid de 2 funciona correctamente")
else:
	print ("El filtro no funciona correctamente")

#FILTROGRID3
filtroGrid3 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[3]")
filtroGrid3.click()
time.sleep(2)

ValidacionGrid3= driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[3]").is_enabled();
if ValidacionGrid3 == True:
	print ("El filtro Grid de 3 funciona correctamente")
else:
	print ("El filtro no funciona correctamente")

#FILTROGRID4
filtroGrid4 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[4]")
filtroGrid4.click()
time.sleep(2)

ValidacionGrid4= driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[4]").is_enabled();
if ValidacionGrid4 == True:
	print ("El filtro Grid de 3 funciona correctamente")
else:
	print ("El filtro no funciona correctamente")

#FILTROGRID5
filtroGrid5 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[5]")
filtroGrid5.click()
time.sleep(2)

ValidacionGrid5= driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[5]").is_enabled();
if ValidacionGrid5 == True:
	print ("El filtro Grid de 5 funciona correctamente")
else:
	print ("El filtro no funciona correctamente")


#HOME
driver.get(website)
time.sleep(2)

