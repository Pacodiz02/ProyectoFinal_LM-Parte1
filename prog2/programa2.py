import requests
import os
import json

url_base="https://api.shodan.io/"
key=os.environ["api_key"]
direccion=input("Introcuce la dirección IP: ")
payload={'key':key}
url=url_base + "shodan/" + "host/" + direccion

r=requests.get(url,params=payload)

if r.status_code == 200:
    datos=r.json()
    print(json.dumps(datos,indent=4,sort_keys=True))
    
else:
    print("Error en la busqueda, " ,r.status_code)
