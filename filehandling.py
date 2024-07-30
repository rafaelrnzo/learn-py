import os 

def create_file(file):
    try:
        with open(file + ".txt", "w") as f:
            f.write('Hello world\n')
            print("succesfully create file" + file)
    except IOError as e:
        print(e)

def read_file(file):
    try:
        with open(file, "r") as f:
            print(file)
            file = f.read()
    except IOError as e:
        print(e)
    
def append_file(file, text):
    try:
        with open(file, "a") as f:
            f.write(text)
            print(f)
    except IOError as e:
        print(e)

def rename_file(file, new_name):
    try:
        os.rename(file, new_name)
        print("file " + file + " renamed to " + new_name + " succesfully ")       
    except IOError as e:
        print(e)

def delete_file(file):
    try:
        os.remove(file)
        print("succesfully delete", file)
    except IOError as e:
        print(e)

def header():
    text = "file handling"
    center = text.center(50)
    print(50*"=")
    print(center)
    print(50*"=")
    print("choose you want to do : ")
    print(" 1.Create File")
    print(" 2.Read File")
    print(" 3.Rename File")
    print(" 4.Append Text")
    print(" 5.Delete File")
    print(50*"=")

def choose(userChoose):
    file = input("input your file name : ")
    if userChoose == "1":
        create_file(file)
    elif userChoose == "2":
        read_file(file)
    elif userChoose == "3":
        new_name = input("input your new file name : ")
        rename_file(file, new_name)
    elif userChoose == "4":
        text = input("input your text : ")
        append_file(file, text)
    elif userChoose == "5":
        delete_file(file)


if __name__ == "__main__":
    header()
    userChoose = input("choose your func : ")
    choose(userChoose)