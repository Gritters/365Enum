import os
import requests
import argparse

#TO DO:
# Add args for cmd line. Have a domain enum mode and is user valid mode.
#Read usernames from file and validate
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

    print("--------")
    print(f"Domain Auth URL is - {responseDict.get('AuthURL')}")
    print("--------")
    return
def userEnum(username):
    #Add Userenumeration here    
    return

parser = argparse.ArgumentParser()

#Add args
parser.add_argument('--d', type=str, required=False, help='The domain you would like to enumerate')
parser.add_argument('--u', type=str, required=False, help='The user you would like to validate')
parser.add_argument('--uL', type=str, required=False, help='The users in a list that you would like to validate')

#Parse args
args = parser.parse_args()

url = 'https://login.microsoftonline.com/getuserrealm.srf?login='
fullUrl = url + args.d 

r = requests.get(fullUrl)
printInfo(r)
