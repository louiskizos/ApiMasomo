import requests

id = int(input("Saisir ID a supprimer : \n"))
endpoint = f"http://127.0.0.1:8000/Delete/{id}/"
response = requests.delete(endpoint)

print(response.status_code, response.status_code == 204)