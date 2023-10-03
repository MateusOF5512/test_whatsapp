from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import streamlit as st
import urllib
from tqdm import tqdm

import pandas as pd

st.set_page_config(page_title="Automação do WhatsApp Web")
st.markdown(""" <style>
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)


# Aplicativo Streamlit
st.title("Automação do WhatsApp Web")

uploaded_file = st.file_uploader("Escolha um arquivo", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file is not None:
        # Lógica para criar DataFrame com base no tipo de arquivo
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file, engine='openpyxl')  # 'openpyxl' é um engine para ler arquivos xlsx

        # Mostrar o DataFrame
        st.write("DataFrame Criado a partir do Arquivo:")

        df = df.astype('str')

        df = df[['telefone','nome', 'mensagem']]
        st.dataframe(df)

        enviar = st.button("Enviar Mensagem")

    if enviar:

        options = Options()

        def get_driver():
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        navegador = get_driver()
        navegador.get("https://web.whatsapp.com/")

        # Barra de progresso
        progress_text = "Enviando mensagens..."
        my_bar = st.progress(0, text=progress_text)

        for linha in tqdm(df.index, desc="Progresso", leave=False):
            # enviar uma mensagem para a pessoa
            nome = df.loc[linha, "nome"]
            mensagem = df.loc[linha, "mensagem"]
            telefone = df.loc[linha, "telefone"]

            texto = mensagem.replace("fulano", nome)
            texto = urllib.parse.quote(texto)

            try:
                link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"

                navegador.get(link)

                while len(navegador.find_elements(By.ID,'side')) < 1:
                    time.sleep(1)
                time.sleep(2)

                if len(navegador.find_elements(
                        By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]')) != 0:
                    navegador.find_element(
                        By.XPATH,
                        '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()
                    time.sleep(2)

                    # Atualize a barra de progresso
                progress_percent = (linha + 1) / len(df.index)

                progress_percent_text = round(progress_percent * 100, 2)
                my_bar.progress(progress_percent, text=str(progress_percent_text)+'%')
                st.info('Mensagem enviada: ' + nome + ' | ' + telefone, icon='📩')

            except:
                st.error('Erro em enviar a mensagem', icon='🚨')
            time.sleep(1)

        navegador.quit()
        my_bar.progress(100, text='100%')
        st.success('Todas as mensagem enviada com sucesso!', icon='✅')







