from Titles import printTitle
from Chatbotwiki import wiki
from Calculator import calc
print("Welcome to")
printTitle()
print("┌────────────────────────────────────┐")
print("│{:^36}│".format("Menu:"))
print("├────────────────────────────────────┤")
print("│{:^36}│".format("1 - Wikipedia Lookup"))
print("│{:^36}│".format("2 - Favorite Sites"))
print("│{:^36}│".format("3 - Calculator"))
print("│{:^36}│".format("4 - Stop"))
print("└────────────────────────────────────┘")
while True:
  menu = input("type the number correlated with your desired request: ")
  if menu == "1":
    wiki()
    continue
  if menu == "2":
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
  elif menu == "3":
    calc()
  elif menu == "4":
    break
  else:
    continue
