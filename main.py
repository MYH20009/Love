import lo
import colorama
from colorama import Fore, Back, Style

print(Fore.BLUE + lo.one)
print(Fore.GREEN + lo.letter)
    
def love():
    for i in range(1,ran):
        print(Fore.BLUE, i , let)
    
def deb():
    for i in range(1,bt):
        print(Fore.RED, i , de)
                
while True:
    type = input("Choose A type :: ")
    if type in ("1","2"):
        if type == "1":
            print(Fore.GREEN + lo.four)
            let = input(Fore.RED + "Enter letter you want to out  :: ")
            ran = int(input(Fore.RED + "Enter range ; (100 or 1000 etc..) ; "))
            love()
        elif type == "2":
            print(Fore.BLUE + lo.two)
            de = input(Fore.RED + "Enter letter you want to debate ;; ")
            bt = int(input(Fore.RED + "Enter range (100 or 1000 etc.. ) ; "))
            deb()
        cho = input("Do you want to next time again?? ( no  /  yes);; ")
        if cho == "yes":
            pass
        else:
            print(Fore.RED + lo.thr)
            break
    else:
        ("invaild number")