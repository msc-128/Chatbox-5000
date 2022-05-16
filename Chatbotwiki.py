from bs4 import BeautifulSoup
import requests
base_url = "https://en.wikipedia.org/wiki/"
topic = input("Search a topic on wikipedia (Use '_' for spacing): ")
ending = topic
url = base_url + ending
r = requests.get(url)
print("URL: ",url)
soup = BeautifulSoup(r.content, 'html.parser')
tag = soup.find('p').find_next('p')
print(tag.text)
