from dotenv import load_dotenv
from read_and_write import readTxt,writeTxt
def main():
    load_dotenv()
    invalid_domains=readTxt("./invalid.txt")
    if len(invalid_domains)>0:
        writeTxt("./invalid.txt",invalid_domains,"Invalid Domains Found")
if __name__=='__main__':
    main()