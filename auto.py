import os, sys, time, random, requests

# Colors
green = '\033[1;32m'
white = '\033[1;37m'
red = '\033[1;31m'
yellow = '\033[1;33m'
cyan = '\033[1;36m'
reset = '\033[0m'

def banner():
    os.system('clear')
    print(f"""{red}
  ██████╗██╗  ██╗███████╗██████╗ ██████╗ ██╗   ██╗
 ██╔════╝██║  ██║██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
 ╚█████╗ ███████║█████╗  ██████╔╝██████╔╝ ╚████╔╝ 
  ╚═══██╗██╔══██║██╔══╝  ██╔══██╗██╔══██╗  ╚██╔╝  
 ██████╔╝██║  ██║███████╗██║  ██║██║  ██║   ██║   
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   {reset}""")
    print(f"{cyan}=================================================={reset}")
    print(f"{white} -> OWNER    :  MR SHARIYAN")
    print(f"{white} -> TEAM     :  GANGSTER 69")
    print(f"{white} -> METHOD   :  FB RANDOM CLONING")
    print(f"{cyan}=================================================={reset}")

def menu():
    banner()
    print(f"{green}[1] Random Cloning (Pakistan)")
    print(f"{green}[2] Random Cloning (India)")
    print(f"{red}[0] Exit")
    print(f"{cyan}=================================================={reset}")
    choice = input(f"{yellow}[+] Select Option: {reset}")
    if choice == '1':
        clone_logic("92300") # Pakistan code
    elif choice == '2':
        clone_logic("91700") # India code
    else:
        sys.exit()

def clone_logic(code):
    banner()
    limit = int(input(f"{yellow}[+] Input Limit (e.g 5000): {reset}"))
    print(f"{cyan}=================================================={reset}")
    print(f"{green}[+] Cloning Started... Use Airplane Mode{reset}")
    print(f"{cyan}=================================================={reset}")
    
    ok = 0
    cp = 0
    
    for i in range(limit):
        uid = code + str(random.randint(1111111, 9999999))
        # Yahan aap apna cloning method (requests) add kar sakte hain
        # Filhal ye demo ids dikhayega
        if i % 100 == 0:
            print(f"{green}[SHARIYAN-OK] {uid} | 123456{reset}")
            ok += 1
        
    print(f"{cyan}=================================================={reset}")
    print(f"{green}[√] Cloning Complete. OK IDz: {ok}")
    print(f"{cyan}=================================================={reset}")

if __name__ == "__main__":
    menu()
  
