import requests
from bs4 import BeautifulSoup
import re
import csv
import os

#What Needs To Be Set:
# Step 1 - competitor name, search term, number of pages (2 places)

#Step 1 - copy the first 10 page to a txt file called search_results.txt
def scrape_google_search(search_term, num_pages):
    base_url = "https://www.google.com/search?q=" + search_term
    page_number = 1
    html_content = []

    while page_number <= num_pages:
        url = f"{base_url}&start={10 * (page_number - 1)}"  # Adjust start parameter for pagination
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Append the entire HTML content to the list
        html_content.append(str(soup))

        page_number += 1

    return html_content

#Set the variables for the search term and the number of pages
competitor = 'Greenhouse'
search_term = '“job-boards.greenhouse.io/" site:greenhouse.io'
num_pages = 30  # Number of pages to scrape
html_content = scrape_google_search(search_term, num_pages)

# Write the HTML content to a text file
with open('search_results.txt', 'w', encoding='utf-8') as f:
    for page_html in html_content:
        f.write(page_html + '\n')

#Step 2 - Extract the URLs from the search_results.txt file and write them to a csv called extracted_urls.csv
def extract_urls(html_content):
    urls = []
    for line in html_content.splitlines():
        while True:  # Infinite loop, break when no more URLs
            match = re.search(r'› [^ ]* ›', line)
            if not match:
                break  # No match found, break the loop for this line
            urls.append(match.group())
            line = line[match.end():]  # Update line for next URL search
    return urls

# stores file data into a variable for use
def read_html_file(filename):
    with open(filename, 'r') as f:
        html_content = f.read()
    return html_content

filename = 'search_results.txt'
html_content = read_html_file(filename)
urls = extract_urls(html_content)

# Write the extracted URLs to a CSV file
with open('extracted_urls.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Competitor'])
    for url in urls:
        writer.writerow([url])

#Step 3 - Remove Duplicate listings
def remove_duplicates(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write header row
        header = next(reader)
        writer.writerow(header)

        # Use a set to store unique URLs
        seen_urls = set()

        for row in reader:
            url = row[0]
            if url not in seen_urls: #compare the url to the set of seen urls. if it isn't in the set, write it to the new file and add it to the set
                writer.writerow(row)
                seen_urls.add(url)

input_file = 'extracted_urls.csv'
output_file = f'{competitor}_client_list.csv'

remove_duplicates(input_file, output_file)
