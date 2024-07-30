import re

data_list = [
    "I went to him at 11 A.M. on 4th July 1886",
    "Aye, said Mr. Gibenson Stark",
    "The quick brown fox jumps over the lazy dog.",
    "hello world",
    "test world",
]

def search_with_regex(data_list, pattern):
    result = [item for item in data_list if pattern.search(item)]
    return result

while True:
    search = input("search > ")
    pattern = re.compile(search)
    
    search_result = search_with_regex(data_list, pattern)
    
    if search_result:
        print(search_result)
    else:
        print("not found, again?")
        choice = input("search again (y/n) > ").lower()
        if choice == 'n':
            break
