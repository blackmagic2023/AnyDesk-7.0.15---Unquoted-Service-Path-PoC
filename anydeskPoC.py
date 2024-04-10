import os
import subprocess

def display_menu():
    print("Select an option:")
    print("1. Check AnyDesk service configuration")
    print("2. View system information")
    print("3. Run custom command (if service path is correct)")
    print("4. Exit")

def check_service_configuration():
    try:
        output = os.popen('sc qc anydesk').read()
        print(output)
    except Exception as e:
        print("Error checking service configuration:", e)

def view_system_information():
    try:
        output = os.popen('systeminfo').read()
        print(output)
    except Exception as e:
        print("Error viewing system information:", e)

def run_custom_command():
    try:
        service_info = os.popen('sc qc anydesk').read()
        if '"C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"' in service_info:
            print("Service path is correctly quoted.")
            custom_command = input("Enter the custom command to run: ")
            print("Running custom command...")
            subprocess.run(custom_command, shell=True)
        else:
            print("Service path is not correctly quoted. Unable to run custom command.")
    except subprocess.CalledProcessError as e:
        print("Error running custom command:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            check_service_configuration()
        elif choice == '2':
            view_system_information()
        elif choice == '3':
            run_custom_command()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
