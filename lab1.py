import requests  # εισαγωγή της βιβλιοθήκης

url = input("Give URL:")  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    headers = response.headers
    print(headers)