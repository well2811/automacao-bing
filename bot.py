import os
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# Carregar credenciais
EMAIL = os.getenv("BING_EMAIL")
SENHA = os.getenv("BING_PASSWORD")

# Palavra para pesquisa (recebida como argumento)
import sys
if len(sys.argv) < 2:
    print("Nenhuma palavra de busca recebida.")
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

def digitar_humano(el, texto):
    for letra in texto:
        el.send_keys(letra)
        time.sleep(random.uniform(0.05, 0.15))

# LOGIN
driver.get("https://www.bing.com")
time.sleep(3)

try:
    driver.find_element(By.ID, "id_s").click()
except:
    print("Não achou botão 'Entrar'")
    driver.quit()
    exit()

time.sleep(3)
campo_email = driver.switch_to.active_element
digitar_humano(campo_email, EMAIL)
campo_email.send_keys(Keys.ENTER)

time.sleep(3)
campo_senha = driver.switch_to.active_element
digitar_humano(campo_senha, SENHA)
campo_senha.send_keys(Keys.ENTER)

time.sleep(7)

# PESQUISA
driver.get("https://www.bing.com")
time.sleep(3)

try:
    caixa = driver.find_element(By.NAME, "q")
    caixa.clear()
    digitar_humano(caixa, palavra)
    caixa.send_keys(Keys.ENTER)
except Exception as e:
    print("Erro na pesquisa:", e)

print("Pesquisa concluída:", palavra)

driver.quit()
