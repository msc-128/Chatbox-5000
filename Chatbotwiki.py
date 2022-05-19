from bs4 import BeautifulSoup
import requests
def wiki():
  base_url = "https://en.wikipedia.org/wiki/"
  while True:
      topic = input("Search a topic on wikipedia (Use '_' for spacing and 'exit' to exit): ")
      if topic == 'exit':
          break
      ending = topic
      url = base_url + ending
      r = requests.get(url)
      print("URL: ",url)
      soup = BeautifulSoup(r.content, 'html.parser')
      tags = soup.find_all('p')
      topic2 = topic.replace("_", " ")
      for tag in tags:
          if topic2 in tag.text:
              #print(tag.text)
              break
      txt = tag.text
      alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
      roman = ['I','II','III','IV','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
      for x in alphabet:
          target = '['+x+']'
          txt = txt.replace(target,'')
      for y in roman:
          target2 = '['+y+']'
          txt = txt.replace(target2,'')
      for i in range(50):
          target1 = '['+str(i)+']'
          txt = txt.replace(target1,'')
      txt = txt.replace('(listen)','')
      txt = txt.replace('[update]','')
      print(txt)
