
import os



def banner():
    print("                                                                                 ") #banner
    print("           ______________________________ ____________________________           ") #banner        
    print(" ----     /        /       /   /     /   /  /       /     /   /      /    ------ ") #banner
    print("          \__  ___/    ___/   /     /   /  /    ___/     /   /   ___/            ") #banner
    print("     ---    / /   /   / ____ /  /  /      /       /  /  /   /      /   ------    ") #banner
    print("       /\__/ /__ /   /     \   /  /      /___    /  /  /   /__  __/        ----- ") #banner
    print(" ---- /         /   /      /     /  /   /       /     /      /   /               ") #banner
    print("      \________/___/\_____/_____/__/___/_______/ ____/______/___/   ------       ") #banner
    print("")
    print("Author:Coded by Z")
    print("\n")

banner() #print banner in terminal



flag = True
while flag == True:

    print("1.Run command ping") # infinte loop (menue =)
    print("2.Run command nmap")
    print("3.Run command ipconfig")
    print("4.End program")

    option= int(input("run command number:"))

    if option == 1:

        print ("Type the command to ping:")
        ipurl=input("Enter an ip address or a web URL address: ")
        os.system("ping %s "%ipurl) # run commands and print out result              
        flag = False
        exit

    if option == 2:

        print ("Type the command to nmap:")
        ipurl=input("Enter an ip address or a web URL address: ")
        os.system("nmap %s "%ipurl) # run commands and print out results
        flag = False
        exit

    if option == 3:

        print ("Click enter to run ipconfig on current host:")
        ipurl=input("Click enter to run")
        os.system("ipconfig %s "%ipurl) # run commands and print out results
        flag = False
        exit

    if option == 4:
        flag = False
        exit
