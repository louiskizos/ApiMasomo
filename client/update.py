import requests

id = int(input("Saisir ID a modifier : \n"))
endpoint = f"http://127.0.0.1:8000/Update/{id}/"
response = requests.put(endpoint, data={"typesEcole": "EP KYESHERO","degree": "Primaire"})
print(response.json())
print(response.status_code)