import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=66b7eed582eedd6e38547a910d4f8b1950be14ca"
files = {'answer' : ('answer.json', open('answer.json', 'rb'))}

r = requests.post(url, files=files)

print(r.text)