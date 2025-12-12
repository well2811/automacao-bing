import os
import time
import random
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = os.getenv("BING_EMAIL")
SENHA = os.getenv("BING_PASSWORD")

# Palavra da pesquisa
if len(sys.argv) < 2:
    print("Nenhuma palavra recebida.")
    exit()

palavra = sys.argv[1]
print(f"Iniciando pesquisa: {palavra}")

# Chrome configs
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 20)

def digitar_humano(el, texto):
    for letra in texto:
        el.send_keys(letra)
        time.sleep(random.uniform(0.04, 0.12))

# 1) LOGIN DIRETO
LOGIN_URL = "https://login.live.com/login.srf?wa=wsignin1.0&wreply=https://www.bing.com/"
driver.get(LOGIN_URL)

# CAMPO EMAIL
campo_email = wait.until(EC.presence_of_element_located((By.NAME, "loginfmt")))
digitar_humano(campo_email, EMAIL)
campo_email.send_keys(Keys.ENTER)
time.sleep(3)

# CAMPO SENHA
campo_senha = wait.until(EC.presence_of_element_located((By.NAME, "passwd")))
digitar_humano(campo_senha, SENHA)
campo_senha.send_keys(Keys.ENTER)
time.sleep(4)

# BOTÃO "Sim" para manter login
try:
    botao_sim = wait.until(EC.element_to_be_clickable((By.ID, "idBtn_Back")))
    botao_sim.click()
except:
    pass

time.sleep(5)

# 2) FAZER PESQUISA
driver.get("https://www.bing.com")
time.sleep(3)

try:
    caixa = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    caixa.clear()
    digitar_humano(caixa, palavra)
    caixa.send_keys(Keys.ENTER)
    print(f"Pesquisa concluída: {palavra}")
except Exception as e:
    print("Erro na pesquisa:", e)

driver.quit()
