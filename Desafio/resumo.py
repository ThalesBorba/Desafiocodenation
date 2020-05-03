import requests
import json
import hashlib

with open("answer.json", 'r') as f:
    data = json.load(f)
    encoding = f.encoding

resumo = hashlib.sha1(data["decifrado"].encode(encoding)).hexdigest()

with open("answer.json", "r") as f:
    json_data = json.load(f)
    json_data["resumo_criptografico"] = resumo

with open("answer.json", "w") as f:
    f.write(json.dumps(json_data))