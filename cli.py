# cli.py
from core.scanner import scan_networks
from core.auto_connect import auto_connect

def run_cli():
    print("WiFi Hacker CLI")
    print("1. Scan and Connect")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        networks = scan_networks()
        if networks:
            result = auto_connect(networks)
            print(f"Auto Connect Result: {result}")
        else:
            print("No networks found")
    elif choice == '2':
        print("Exiting...")
    else:
        print("Invalid choice")

if __name__ == '__main__':
    run_cli()
