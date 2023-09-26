from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import streamlit as st
import urllib




# Aplicativo Streamlit
st.title("Automação do WhatsApp")
contato = st.text_input("Digite o nome do contato:")
telefone = st.text_input("Digite o número do contato:")
mensagem = st.text_area("Digite a mensagem:")
enviar = st.button("Enviar Mensagem")

if enviar:
    navegador = webdriver.Chrome()
    navegador.get("https://web.whatsapp.com")

    # esperar a tela do whatsapp carregar
    while len(navegador.find_elements(By.ID, 'side')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
        time.sleep(1)
    time.sleep(2)  # só uma garantia

    nome = contato
    mensagem = mensagem
    telefone = telefone

    texto = urllib.parse.quote(mensagem)

    link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"

    navegador.get(link)

    while len(navegador.find_elements(By.ID, 'side')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
        time.sleep(1)
    time.sleep(2)  # só uma garantia

    if len(navegador.find_elements(
            By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]')) != 0:
        navegador.find_element(
            By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()
        time.sleep(2)



    navegador.get(link)

    while len(navegador.find_elements(By.ID, 'side')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
        time.sleep(1)
    time.sleep(2)  # só uma garantia

    if len(navegador.find_elements(
            By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]')) != 0:
        navegador.find_element(
            By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()
        time.sleep(2)


    navegador.get(link)

    while len(navegador.find_elements(By.ID, 'side')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
        time.sleep(1)
    time.sleep(2)  # só uma garantia

    if len(navegador.find_elements(
            By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]')) != 0:
        navegador.find_element(
            By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()
        time.sleep(2)
