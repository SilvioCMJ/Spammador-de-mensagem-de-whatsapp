from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Abra o navegador Google Chrome
driver = webdriver.Chrome()

# Abra o WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("Por favor, escaneie o código QR e pressione Enter")
input()

# Selecione o contato para enviar mensagem
contato = driver.find_element_by_xpath("NOME DO CONTATO")
contato.click()

# Espere 2 segundos para que a conversa seja carregada
time.sleep(2)

# Selecione a caixa de texto e envie a mensagem
contador = 0
repeticoes = 23423423

while contador < repeticoes:
    contador += 1
    caixa_de_texto = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"][@data-tab="1"]')
    caixa_de_texto.click()
    caixa_de_texto.send_keys("MENSAGEM DE TESTE")
    caixa_de_texto.send_keys


# Feche o navegador
driver.close()