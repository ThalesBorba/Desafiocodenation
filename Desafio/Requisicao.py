import requests
r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=66b7eed582eedd6e38547a910d4f8b1950be14ca')
print(r.json())