import requests

url = "https://simple.wikipedia.org/wiki/Median"
response = requests.get(url)
page_content = response.content


# Parsing the Page with Beautiful Soup:

# Parse the fetched content using Beautiful Soup.

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_content, 'html.parser')


# Extracting Text Content:

# The .text attribute of a Beautiful Soup object will return the text inside that object (and its children). 
# To get the text content of the entire page:

text_content = soup.text

# However, this might still contain some extra whitespace and unwanted text. 
# To get a cleaner text representation, you can extract text from specific tags (like <p>, <h1>, etc.) and then join them.

paragraphs = soup.find_all('p')
text_content = "\n".join([p.text for p in paragraphs])

# Sometimes, you might still have extra whitespace or newline characters. To clean it up:
clean_text = " ".join(text_content.split())


# Saving to output.txt
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(clean_text)

print("Text saved to output.txt")