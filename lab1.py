import requests  # εισαγωγή της βιβλιοθήκης
import datetime as dt   # για εύρεση χρόνου εγκυρότητας cookie 

def print_item(iter):
    for key,value in iter:
        print(f"{key}: {value}")

url = input("Give URL: ")  # προσδιορισμός του url
# Ενδεικτικά παραθέτω: 1) http://python.org
#                      2) https://github.com

# Αίτημα http request
with requests.get(url) as response:  # το αντικείμενο response
    
    headers = response.headers
    cookies = response.cookies
    
    print("\nHeaders:\n")
    print_item(headers.items())     # τυπώνει όλες τις κεφαλίδες

    try:
        print(f"\nServer software: {headers['server']}\n")  # τυπώνει το λογισμικό του server
    except:                                                 # αν υπάρχει
        print("No server software info")
    
    # εντοπισμός ύπαρξης cookies και τυπώνει τις ζητούμενες πληροφορίες 
    if "set-cookie" in headers.keys():
        print("The site uses cookies")
        print()
        for cookie in cookies:
            if cookie.expires is not None:
                print(f"Name: {cookie.name}\nValid for: {dt.datetime.fromtimestamp(float(cookie.expires)) - dt.datetime.now()}")
                print()
            else:
                print(f"Name: {cookie.name}\nValid for: Always valid")
                print()
    else:
        print("No cookies used")
