import json
import random
import re
import os

names = ["Alice", "Bob", "Charlie", "David", "Eva", "Fiona", "George", "Hannah", "Ian", "Jack",
         "Kara", "Liam", "Mona", "Nina", "Oscar", "Paul", "Quincy", "Rita", "Sam", "Tina",
         "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane"]
countries = ["USA", "Canada", "UK", "Germany", "France", "Italy", "Spain", "Australia", "Japan", "China",
             "Brazil", "India", "Mexico", "Russia", "South Africa", "New Zealand", "Argentina", "South Korea",
             "Netherlands", "Sweden", "Norway", "Denmark", "Finland", "Belgium", "Switzerland", "Austria"]
jobs = [
    "Backend Developer",
    "Frontend Developer",
    "UI/UX Designer",
    "Mechatronics",
    "IT Support",
    "System Engineering",
    "Marketing",
    "Finance",
]
ages = range(18, 80)

def header():
    text = "Make data dummy JSON"
    center = text.center(50)
    print("=" * 50)
    print(center)
    print("=" * 50)
    print("Choose what you want to do:")
    print(" 1. Create Dummy Json")
    print(" 2. Filter Json")
    print(" 3. Delete File")
    print(" 4. Exit")
    print("=" * 50)

def create_dummy(filename, num_entries):
    data = []
    for _ in range(num_entries):
        entry = {
            "name": random.choice(names),
            "country": random.choice(countries),
            "age": random.choice(ages),
            "job": random.choice(jobs)
        }
        data.append(entry)
    
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"{num_entries} JSON objects have been generated and saved to {filename}")

def filter_json(input_filename, output_filename, fields, patterns):
    with open(input_filename, "r") as json_file:
        data = json.load(json_file)
    
    filtered_data = []
    compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    
    for entry in data:
        match_found = any(
            any(pattern.search(str(entry.get(field, ''))) for pattern in compiled_patterns) 
            for field in fields
        )
        if match_found:
            filtered_entry = {field: entry.get(field, '') for field in fields}
            filtered_data.append(filtered_entry)
    
    with open(output_filename, "w") as filtered_json_file:
        json.dump(filtered_data, filtered_json_file, indent=4)
    
    print(f"Filtered JSON objects have been saved to {output_filename}")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} has been deleted.")
    else:
        print(f"{filename} does not exist.")

if __name__ == "__main__":
    while True:
        header()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            filename = input("Enter the output file name (e.g., data.json): ")
            num_entries = int(input("Enter the number of entries to generate: "))
            create_dummy(filename, num_entries)
        elif choice == "2":
            input_filename = input("Enter the input file name (e.g., data.json): ")
            output_filename = input("Enter the output file name for filtered data (e.g., filtered_data.json): ")
            fields = input("Enter the fields to include (comma-separated, e.g., name,age): ").split(',')
            fields = [field.strip() for field in fields]  # Clean up whitespace
            patterns_input = input("Enter the regex patterns to match (comma-separated, e.g., Backend,Frontend): ")
            patterns = [pattern.strip() for pattern in patterns_input.split(',')]
            filter_json(input_filename, output_filename, fields, patterns)
        elif choice == "3":
            filename = input("Enter the file name to delete: ")
            delete_file(filename)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
