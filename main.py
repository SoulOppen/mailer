from dotenv import load_dotenv
from read_and_write import readTxt,writeTxt
def main():
    load_dotenv()
    invalid_mail=readTxt("./invalid_mail.txt")
    invalid_domains=readTxt("./invalid_domain.txt")
    if len(invalid_domains)>0:
        writeTxt("./invalid_domain.txt",invalid_domains,"Invalid Domains Found")
    if len(invalid_mail)>0:
        writeTxt("./invalid_mail.txt",invalid_domains,"Invalid Domains Found")
if __name__=='__main__':
    main()