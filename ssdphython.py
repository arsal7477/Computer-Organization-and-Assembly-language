import os
def read_file():
    filename = input("Enter the filename to read: ")
    # Insecure: No validation of filename, allowing path traversal attacks
    with open(filename, "r") as file:
        print(file.read())
def delete_file():
    filename = input("Enter filename to delete: ")
    # Insecure: Directly deleting without checking if it's safe
    os.remove(filename)
    print(f"{filename} deleted successfully!")
def execute_command():
    command = input("Enter shell command: ")   
    # 🚨 Insecure: Allows arbitrary command execution
    os.system(command)
if __name__ == "__main__":
    print("Options: 1) Read File  2) Delete File  3) Execute Command")
    choice = input("Enter option (1/2/3): ")  
    if choice == "1":
        read_file()
    elif choice == "2":
        delete_file()
    elif choice == "3":
        execute_command()
    else:
        print("Invalid choice")
