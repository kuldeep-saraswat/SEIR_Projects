import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Enter website link")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url, timeout=10)
except:
    print("Unable to open the website")
    sys.exit(1)

soup = BeautifulSoup(response.text, "html.parser")

print("\nTitle:")
if soup.title:
    print(soup.title.text.strip())   
else:
    print("No Title")

print("\nBody Content:")
if soup.body:
    body_text = soup.body.get_text(separator="\n", strip=True)
    print(body_text)
else:
    print("No Body")

print("\nLinks:")
for tag in soup.find_all("a"):
    link = tag.get("href")
    if link:
        print(link)