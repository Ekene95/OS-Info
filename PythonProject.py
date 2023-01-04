#!/usr/bin/python3

import os

while (True):
    
    print("\n[1] Linux OS Version")
    print("[2] Private IP address")
    print("[3] Public IP address")
    print("[4] Gateway IP address")
    print("[5] Hard Disk size, free and used space")
    print("[6] Top 5 directories and their sizes")
    print("[7] CPU usage with a 10 seconds refresh")
    print("[8] Exit")
    choice = int(input("Enter a number: "))

    if choice == 1:
        os.system('uname -a')
    elif choice == 2:
        os.system("ifconfig | grep inet | awk '{print $2}' | sed -n 1p")
    elif choice == 3:
        os.system("curl ifconfig.me")
    elif choice == 4:
        os.system("route -n | sed -n 3p | awk '{print $2}'")
    elif choice == 5:
        os.system('df -H')
    elif choice == 6:
        os.system('cd / && du -sh * 2>/dev/null | sort -rh | head -5')
    elif choice == 7:
        os.system('sar -u 10 5')
    elif choice == 8:
        break
    else:
        print('Your choice is invalid')