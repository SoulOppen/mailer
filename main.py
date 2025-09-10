import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from read_and_write import readTxt,writeTxt
def main():
    load_dotenv(dotenv_path="/mnt/c/Users/ariel/Documentos/quickMail/.env")
    invalid_mail=readTxt("./invalid_mail.txt")
    invalid_domains=readTxt("./invalid_domain.txt")
    smtp_server = os.getenv("SMTP_SERVER")
    print(smtp_server)
    smtp_port = int(os.getenv("SMTP_PORT"))
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    print("user",user)
    to = "arieloppenheimer@outlook.cl"
    subject = "hola9"
    body = "Hola!\nEste es un correo de prueba enviado solo con smtplib."
    msg = MIMEText(body)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(user, password)
        server.sendmail(user,to,  msg.as_string())
        print("✅ Correo enviado correctamente")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        server.quit()
    if len(invalid_domains)>0:
        writeTxt("./invalid_domain.txt",invalid_domains,"Invalid Domains Found")
    if len(invalid_mail)>0:
        writeTxt("./invalid_mail.txt",invalid_domains,"Invalid Domains Found")
if __name__=='__main__':
    main()