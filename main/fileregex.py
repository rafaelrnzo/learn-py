import json
import re

def create_country_json(input_file, output_file, search_term):
    """
    Creates a new JSON file containing data for the specified country.

    Args:
        input_file: Path to the input JSON file.
        output_file: Path to the output JSON file.
        search_term: The name of the country to search for.
    """

    with open(input_file, 'r') as f:
        data = json.load(f)

    pattern = re.compile(search_term, re.IGNORECASE)
    filtered_data = [country for country in data if pattern.search(country['name'])]

    with open(output_file, 'w') as f:
        json.dump(filtered_data, f, indent=4)

# Contoh penggunaan
input_file = "data.json"
output_file = "indonesia.json"
search_term = "indonesia"

create_country_json(input_file, output_file, search_term)
