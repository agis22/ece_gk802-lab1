import requests  # εισαγωγή της βιβλιοθήκης

def print_item(iter):
    for key,value in iter:
        print(f"{key}")

url = input("Give URL: ")  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    headers = response.headers
    cookies = response.cookies
    print(f"\nHeaders:")  
    print_item(headers.items())     # τυπώνει όλες τις κεφαλίδες
    print(f"\nServer: {headers['server']}\n")  # τυπώνει το λογισμικό του server
    
    #if cookies != None:
    print(headers['set-cookie']['expires'])
    #print_item(cookies.items())  # τυπώνει το λογισμικό του server
