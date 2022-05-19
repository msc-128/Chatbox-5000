from bs4 import BeautifulSoup
import requests
def wiki():
  base_url = "https://en.wikipedia.org/wiki/"
  topic = input("Search a topic on wikipedia (Use '_' for spacing): ")
  ending = topic
  url = base_url + ending
  r = requests.get(url)
  print("URL: ",url)
  soup = BeautifulSoup(r.content, 'html.parser')
  tag = soup.find('p').find_next('p')
  tag_text = tag.text
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for x in alphabet:
      target = '['+x+']'
      tag_text = tag_text.replace(target,'')
  for i in range(50):
      target1 = '['+str(i)+']'
      tag_text = tag_text.replace(target1,'')
  tag_text = tag_text.replace('(listen)','')
  print(tag_text)
