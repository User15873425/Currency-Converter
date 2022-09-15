import requests

rates = requests.get(f'http://www.floatrates.com/daily/{input().lower()}.json').json()
cache = {'USD': 0, 'EUR': 0}
while code := input().upper():
    check = ('Sorry, but it is not', 'Oh! It is')[code in cache]
    cache[code] = round(float(input()) * rates[code.lower()]['rate'], 2)
    print(f'Checking the cache...\n{check} in the cache!\nYou received {cache[code]} {code}.')
