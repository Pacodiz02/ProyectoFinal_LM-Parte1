import requests
import os
import json

url_base="https://api.shodan.io/"
key=os.environ["api_key"]
puerto=input("Introduce un puerto(ej. port:22): ")

s=input("¿Quieres filtrar el resultado?(s/n): ")

if s == "s":

    filtro=input("Introduce el parámetro para filtrar(ej. org,os): ")
    payload={'key':key,"query":puerto,"facets":filtro}
    url=url_base + "shodan/" + "host/" + "count"
    r=requests.get(url,params=payload)

    if r.status_code == 200:
        datos=r.json()
        for i in datos.get("facets").get("org"):
            print(i)
        print("\n")
        
    else:
        print("Error en la busqueda, " ,r.status_code)

elif s == "n":

    payload={'key':key,"query":puerto}
    url=url_base + "shodan/" + "host/" + "count"
    r=requests.get(url,params=payload)

    if r.status_code == 200:
        datos=r.json()
        print("Total:" ,datos.get("total"))

    else:
        print("Error en la busqueda, " ,r.status_code)
