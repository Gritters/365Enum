import os
import requests
import argparse

#TO DO:
#Loop through dictionaries for relevant info
#Print stuff to terminal in clean format. Figure out how to use colors?


def printInfo(response):
    
    responseDict = response.json()
    print("--------")
    print("Domain Type")
    print("--------")
    if responseDict.get("NameSpaceType") == "Unknown":
        print("This domain does not exist in M365")
    elif responseDict.get("NameSpaceType") == "Federated":
        print(f"{domain} is a Federated domain")
    elif responseDict.get("NameSpaceType") == "Managed":
        print(f"{domain} is a Managed domain")
    return

domain = input("What is the domain you would like to enumerate? \n")
url = 'https://login.microsoftonline.com/getuserrealm.srf?login='
fullUrl = url + domain 

r = requests.get(fullUrl)
printInfo(r)
