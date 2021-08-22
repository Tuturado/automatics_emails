# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#Abrir o arquivo com a lista de emails
arquivo = open('exemplo.txt','r')

#iterar sobre a lista de emails e jogar para um vetor auxiliar
lista=[]
for linha in arquivo:
    lista.append(linha)
#print(lista)
#Configurações do email
msg = MIMEMultipart()
message = "Message" #Menssagem que deseja enviar no email

password = ""#Senha do seu email
msg["From"] = ""#email que enviará para os outros
msg["Subject"] = "Newslatter"#Assunto do email
msg['To'] = ", ".join(lista)#Lista .txt com os emails que receberão


msg.attach(MIMEText(message,'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

server.login(msg["From"], password)

server.sendmail(msg["From"], lista, msg.as_string())
server.quit()
print("Emails enviados para a lista fornecida")
arquivo.close()