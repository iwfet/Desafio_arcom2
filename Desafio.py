#instalar biblbioteca 
"""
pip install selenium webdriver
pip install pandas
pip install smtplib

"""
#Se der algum erro na parte do envio de email abra o google click em conta, em seguida va em segurança e dessa ate aparecer um bloco com o nome de "Acesso a app menos seguros e clique em ativar"
from selenium  import  webdriver
import time 
from datetime  import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

# preencha os campos
user = ''#colocar o email de quem ira enviar 
password = ''#senha da pessoa q ira enviar
destino =''##colocar email para quem sera enviado
caminho = ''#passar o caminho onde estara o arquivo de vendas explo C:/Users/j13vv/Downloads/Vendas.xls

#Iniciando o chrome e navegando
link_planilha = 'https://drive.google.com/file/d/1AL-hSW082hpJUh5B4WRRlCLLQ63QOXfY/view?usp=sharing'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(link_planilha)
driver.set_window_size(500,150)
time.sleep(15)

#abrindo e fazendo o dowlond arquivo 
porcura_arquivo = caminho
baixar = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/div[2]/div[2]/div[3]')
baixar.click()
time.sleep(5)
print("Download feito com sucesso")
driver.close()

#lendo a planilha e salvando os dados
arquivo = pd.read_excel(porcura_arquivo)
faturamento = arquivo['Valor Final'].sum()
produtos_quantidade = arquivo['Quantidade'].sum()

#corpo da mensagem do email

message = f'''
Prezados,bom dia

O faturamento de ontem foi de: R${faturamento}
A quantidade de produto foi de:{produtos_quantidade}

Luiz Fernando'''
# Configuração
host = 'smtp.gmail.com'
port = 587


# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem

print('Criando mensagem...')
msg = MIMEMultipart()
msg['From'] = user
msg['To'] = destino
msg['Subject'] = 'Relatorio de vendas do dia anteriros'
print('Adicionando texto...')
msg.attach(MIMEText(message, 'plain'))

# Enviando mensagem
print('Enviando mensagem...')
server.sendmail(msg['From'], msg['To'], msg.as_string())
print('Mensagem enviada!')
server.quit()

os.remove(caminho)

print("Finalizado Sistema")