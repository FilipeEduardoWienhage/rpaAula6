from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("file://C:/Users/filip/Documents/GitHub/rpaAula6/index.html")

time.sleep(2)

campo_usuario = driver.find.element(By.ID, "usuario")
campo_senha = driver.find.element(By.ID, "senha")
campo_login = driver.find.element(By.XPATH, "//*[@id='loginForm']/button")


campo_usuario.send_keys("ALUNOS")
campo_senha.send_