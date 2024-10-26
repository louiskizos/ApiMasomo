import requests

id = int(input("Saisir ID a chercher : \n"))
endpoint = f"http://127.0.0.1:8000/Test_details/{id}/"
response = requests.get(endpoint)
print(response.json())
print(response.status_code)