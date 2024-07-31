import re

data_list = [
    "I went to him at 11 A.M. on 4th July 1886",
    "Aye, said Mr. Gibenson Stark",
    "The quick brown fox jumps over the lazy dog.",
    "hello world",
    "test world",
]

def search(data_list, pattern):
    result = [item for item in data_list if pattern.search(item)]
    return result

def addressChecker(txt):
    check = re.findall("^jl.", txt, re.IGNORECASE)
    if check:
        print("Success: Address contains 'jl.' at the start")
    else:
        print("Error: Address must contain 'jl.' at the start of the line")
    return check

def numTel(tel):
    check = re.match("^\d{7,12}$", tel)
    lenTel = len(tel)
    if check:
        print("Success: Valid telephone number")
    elif lenTel > 12:
        print("Error: Telephone number is too long")
    elif lenTel < 7:
        print("Error: Telephone number is too short")
    return check

def header():
    text = "Python Regex"
    center = text.center(50)
    print("=" * 50)
    print(center)
    print("=" * 50)
    print("Choose the number you want to do:")
    print("1. Search Function")
    print("2. Telp Checker")
    print("3. Address Checker")
    print("=" * 50)

def choose(userChoice):
    if userChoice == "1":
        search_term = input("Enter search term: ")
        pattern = re.compile(search_term, re.IGNORECASE)
        search_result = search(data_list, pattern)
        
        if search_result:
            print("Search results:", search_result)
        else:
            print("No results found. Try again?")
            choice = input("Search again (y/n)? ").lower()
            if choice != 'y':
                return False
    elif userChoice == "2":
        tel = input("Please input telephone number: ")
        numTel(tel)
    elif userChoice == "3":
        address = input("Please input address: ")
        addressChecker(address)
    elif userChoice.lower() == "exit":
        return False
    else:
        print("Invalid choice, please try again.")
    return True

if __name__ == "__main__":
    while True:
        header()
        userChoice = input("Choose your function: ")
        if not choose(userChoice):
            break
    print("Exiting the program.")
