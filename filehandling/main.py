import os 

def create_file(file):
    try:
        with open(file, "w") as f:
            f.write('Hello world\n')
        print(f"Successfully created file {file}")
    except IOError as e:
        print(e)

def read_file(file):
    try:
        with open(file, "r") as f:
            print(f"Reading file: {file}")
            content = f.read()
            print(content)
        
    except IOError as e:
        yesno = input("can't find your file, do you want to make this file? (y/n) > ")
        if yesno == "y":
            create_file(file)
        else : 
            print(e)

def append_file(file, text):
    try:
        with open(file, "a") as f:
            f.write(text)
        print(f"Successfully appended to file {file}")
    except IOError as e:
        print(e)

def rename_file(file, new_name):
    try:
        os.rename(file, new_name)
        print(f"File {file} renamed to {new_name} successfully")
    except IOError as e:
        print(e)

def delete_file(file):
    try:
        os.remove(file)
        print(f"Successfully deleted file {file}")
    except IOError as e:
        print(e)

def create_folder(directory):
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Successfully created directory {directory}")
    except OSError as e:
        print(e)

def header():
    text = "File Handling"
    center = text.center(50)
    print("=" * 50)
    print(center)
    print("=" * 50)
    print("Choose what you want to do:")
    print(" 1. Create File")
    print(" 2. Create Folder")
    print(" 3. Read File")
    print(" 4. Append Text")
    print(" 5. Delete File")
    print(" 6. Rename File ")
    print("=" * 50)

def choose(user_choice):
    if user_choice == "1":
        file = input("Input your file name (if u want to create a file in folder just typing folder/file): ")
        create_file(file)
    elif user_choice == "2":
        directory = input("Input the directory name to create: ")
        create_folder(directory)
    elif user_choice == "3":
        file = input("Input the file name to read : ")
        read_file(file)
    elif user_choice == "4":
        file = input("Input the file name to append text : ")
        text = input("Input your text to append: ")
        append_file(file, text)
    elif user_choice == "5":
        file = input("Input the file name to delete : ")
        delete_file(file)
    elif user_choice == "6":
        file = input("Input your current file name : ")
        new_name = input("Input your new file name : ")
        rename_file(file, new_name)
    elif user_choice.lower() == "exit":
        print("Exiting the program.")
        return
    else:
        print("Invalid choice, please try again.")

if __name__ == "__main__":
    while True:
        header()
        user_choice = input("Choose your function: ")
        if user_choice.lower() == "exit":
            break
        choose(user_choice)
