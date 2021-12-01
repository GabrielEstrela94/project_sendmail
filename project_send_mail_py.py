

##Como estou usando um colab, criei uma pasta para arquivar o df  e usarmos no nosso envio de e-mail.
!mkdir /content/pastamail
!pip install yagmail

## Importei as bibliotecas que vou utilizar nesse projeto.

import yagmail as yg
import pandas as pd
import time

## informados o e-mail e senha para realizar o login

email_user = 'seuemail@dominio.com'
email_password = 'senha'

usuario = yg.SMTP(user=email_user, password=email_password)

## Busquei o df e testei para verificar se está indo tudo nos conformes.

df = pd.read_csv('/content/segurado.csv', sep=',')

listas = list(df.itertuples(index=False))

print(listas)

## Como são dois tipos de e-mail que vou enviar preciso criar duas variáveis com esse texto

corpo_email1 = '''
texto aqui'''

corpo_email2 = '''
texto aqui'''

## Percorro o df que está em formato de tuplas e vou pegando os dados de interesse para envio do e-mail

emails_enviados = 0
for lista in listas:
  nome, email, analise = lista
  if analise == 'Segurado':
    usuario.send(to=email, subject='Assunto e-mail', contents=corpo_email1)
  else:
    usuario.send(to=email, subject='Assunto e-mail2', contents=corpo_email2)
  emails_enviados = emails_enviados + 1
  time.sleep(5)
  print(' e-mail enviado para {}.'.format(nome))

print('{} e-mails enviados'.format(emails_enviados))

