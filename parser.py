import requests
from datetime import datetime
import os

# URL of the JSON data
url = "https://allowlists.grafana.com/synthetics"

# Directory to save output files
output_dir = "output_files"

def format_value(value):
    """Formats the value for writing as plain text."""
    if isinstance(value, dict):
        # Convert dictionary to plain text (key: value)
        return "\n".join([f"{k}: {v}" for k, v in value.items()])
    elif isinstance(value, list):
        # Convert list to plain text (one item per line)
        return "\n".join(map(str, value))
    else:
        # If it's a simple type (e.g., string, int), return it as is
        return str(value)

def save_plaintext_to_file(file_path, value):
    """Saves the value as plain text to a file at the given file path."""
    # Get the current datetime
    last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the current datetime and formatted value to a file
    with open(file_path, 'w') as file:
        # Write the current datetime as a comment
        file.write(f"# Last-Modified: {last_modified}\n\n")

        # Format the value as plain text and write to the file
        formatted_value = format_value(value)
        file.write(formatted_value)

    print(f"Plaintext data has been written to {file_path}.")

def parse_and_save_json(data, parent_key=""):
    """Recursively parses the JSON and saves each key-value pair as plain text."""
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through each key-value pair
    for key, value in data.items():
        # Construct a new key path based on the parent key
        new_key = f"{parent_key}_{key}" if parent_key else key

        # If the value is a dictionary, recursively parse it
        if isinstance(value, dict):
            parse_and_save_json(value, new_key)
        else:
            # Create a file name based on the key path
            output_file = os.path.join(output_dir, f"{new_key}.txt")

            # Save the value as plain text
            save_plaintext_to_file(output_file, value)

def main():
    # Fetch the JSON data from the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Start parsing and saving the JSON data
        parse_and_save_json(data)
    else:
        print(f"Failed to fetch data. HTTP Status code: {response.status_code}")

if __name__ == "__main__":
    main()
