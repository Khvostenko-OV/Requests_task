import requests


url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'  # or 'https://akabab.github.io/superhero-api/api'
heros = requests.get(url + '/all.json').json()
heros_names = ['Hulk', 'Captain America', 'Thanos']

print(max([(hero['name'], hero['powerstats']['intelligence']) for hero in heros if hero['name'] in heros_names], key=lambda a: a[1]))

# print('Самый умный - ', max([(hero['name'], hero['powerstats']['intelligence']) for hero in heros], key=lambda a: a[1]))
# print('Самый тупой - ', min([(hero['name'], hero['powerstats']['intelligence']) for hero in heros], key=lambda a: a[1]))
