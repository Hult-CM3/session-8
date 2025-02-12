import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
joke = response.json()
print(f"Here's a joke: {joke['value']}")