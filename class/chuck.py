import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
print(response)
joke = response.json()
#print(joke)
print(f"Here's a joke: {joke['value']}")