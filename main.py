import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from condition import valid_domain,valid_mail
from read_and_write import readTxt,writeTxt
import pandas as pd
def main():
    load_dotenv(dotenv_path="/mnt/c/Users/ariel/Documentos/quickMail/.env")
    invalid_mail=readTxt("./invalid_mail.txt")
    invalid_domains=readTxt("./invalid_domain.txt")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    df= pd.read_excel("/mnt/c/Users/ariel/Documentos/T_Jose/Mailing/Prototipo.xlsm", sheet_name=None)
    to = df["mail"]["mail"].dropna().tolist()
    subject = df["adjuntos"].at[0, "subject"]
    body=""
    for col in ["Intro", "Noticia", "Bajada"]:
        for texto in df["Texto"][col].dropna().tolist():
            body += f"<p>{texto}</p>\n"
   
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(user, password)
        
        for t in to:
            if(!valid_mail(t)){
               invalid_mail.add(t)
            }
            if(!valid_domain(t)){
               invalid_domains.add(t.split("@")[1])
            }
            msg = MIMEText(body,"html")
            msg['From'] = user
            msg['Subject'] = subject           
            msg['To'] = t
            server.sendmail(user,t,  msg.as_string())
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