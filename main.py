from dotenv import load_dotenv
import os
def main():
    load_dotenv()
    remitente_email = os.getenv("smp")
    print(remitente_email)
if __name__=='__main__':
    main()