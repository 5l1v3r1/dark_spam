# this tool created by abdulrahman almajayda since 17-06-2021
# https://github.com/itsDARKSAMA

from colorama import Fore
from time import sleep
from pyautogui import typewrite,press

def banner():
    print( f"""
    {Fore.YELLOW}
    8888888b.           8888888b.  888    d8P        .d8888b.  8888888b.     d8888 888b     d888 
    888  "Y88b          888   Y88b 888   d8P        d88P  Y88b 888   Y88b   d88888 8888b   d8888 
    888    888          888    888 888  d8P         Y88b.      888    888  d88P888 88888b.d88888 
    888    888  8888b.  888   d88P 888d88K           "Y888b.   888   d88P d88P 888 888Y88888P888 
    888    888     "88b 8888888P"  8888888b             "Y88b. 8888888P" d88P  888 888 Y888P 888 
    888    888 .d888888 888 T88b   888  Y88b  888888      "888 888      d88P   888 888  Y8P  888 
    888  .d88P 888  888 888  T88b  888   Y88b       Y88b  d88P 888     d8888888888 888   "   888 
    8888888P"  "Y888888 888   T88b 888    Y88b       "Y8888P"  888    d88P     888 888       888 
                                                                                                
                    {Fore.WHITE} [{Fore.LIGHTBLUE_EX} Telegram {Fore.WHITE}-{Fore.CYAN} Twitter {Fore.WHITE}-{Fore.BLUE} Facebook {Fore.WHITE}-{Fore.RED} Instagram {Fore.WHITE}- .. etc   ]                                                                                                                
                           {Fore.GREEN}      Created by : {Fore.WHITE}github/itsDaRKSAMA  

    """)

def spammer():
    try:
        spam_limit = int(input("Please Enter Messages Limit :\n>>> "))
        spam_massage = input("Please Enter Message\n>>> ")
        count = 0
        print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Spam will start after 10s ...")
        sleep(2)
        print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Please open the chat you want to send, and keep waiting ...")
        sleep(2)
        print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Please {Fore.RED}don't do anything {Fore.WHITE}while script is sending")
        sleep(5)
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Script is {Fore.GREEN}Start{Fore.WHITE}")
        sleep(1)
        while(count < spam_limit):
            typewrite(spam_massage)
            press("enter")
            count +=1
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.YELLOW} {count} {Fore.WHITE} Messages From {Fore.YELLOW} {spam_limit} {Fore.WHITE} Has been sent")
        print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}]{Fore.GREEN} Done ...")
    except :
        pass

banner()
spammer()
