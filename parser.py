import requests
import json
from datetime import datetime

# URL of the JSON data
url = "https://allowlists.grafana.com/synthetics"

# Output file name
output_file = "ipv4_sections.txt"

def extract_ipv4_sections(data):
    """Extracts all IPv4 sections from the JSON data."""
    ipv4_sections = []
    
    # Navigate through the JSON structure to find IPv4 addresses
    for entry in data.get('allowlist', []):
        if 'ipv4' in entry:
            ipv4_sections.append(entry['ipv4'])

    return ipv4_sections

def main():
    # Fetch the JSON data from the URL
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract IPv4 sections
        ipv4_sections = data['all']['ipv4']
        
        # Get the current datetime
        last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write current datetime and IPv4 sections to a file
        with open(output_file, 'w') as file:
            # Write the current datetime as a comment
            file.write(f"# Last-Update: {last_modified}\n")
            
            # Write each IPv4 section on a new line
            for section in ipv4_sections:
                file.write(section + '\n')
        
        print(f"IPv4 sections and current Last-Modified header have been written to {output_file}.")
    else:
        print(f"Failed to fetch data. HTTP Status code: {response.status_code}")

if __name__ == "__main__":
    main()
