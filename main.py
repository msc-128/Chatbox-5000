from Titles import printTitle
from Chatbotwiki import wiki
print("Welcome to")
printTitle()
print("------------------------\nMenu:\n1 - Wikipedia Lookup\n2 - Favorite Sites\n3 - Stop")
while True:
  firstInput = input("> ")
  if firstInput == "1":
    wiki()
    continue
  elif firstInput == "2":
    f = open("madLibFile.txt", "r")
    print(f.read())
    print("Do you want to edit your favorite sites?")
    secInput = input("> ")
    if secInput == "yes":
      print("Type the sites you want to add")
      favInput = input("> ")
    else:
      favInput = ""
      print("Done")
    try:
      madFile=open('madLibFile.txt', mode='r', encoding='utf-8')
    except:
      print("Problem opening madLibFile.txt.")
    madFile.close()
    f = open("madLibFile.txt", "a")
    f.write(favInput + "\n")
    f.close()
    f = open("madLibFile.txt", "r")
    print(f.read())

  elif firstInput == "3":
    break
  else:
    continue