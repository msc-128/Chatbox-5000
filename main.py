import requests
from bs4 import BeautifulSoup
import random
from Titles import printTitle
print("Welcome to")
printTitle()
print("------------------------\nMenu:\n1 - Wikipedia Lookup\n2 - Favorite Sites\n3 - Stop")
firstInput = input("> ")


def wikiSearch():
    print("What would you like to search for?")
    wikiInput = input("> ")

def favSites():
  print("")