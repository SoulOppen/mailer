from dotenv import load_dotenv
import os
def main():
    load_dotenv()
    remitente_email = os.getenv("sender_mail")
    print(remitente_email)
if __name__=='__main__':
    main()