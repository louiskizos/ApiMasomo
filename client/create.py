import requests


endpoint = "http://127.0.0.1:8000/Test_post/"
response = requests.post(endpoint, data={
"typesEcole": "EP KARISIMBI","degree": "Primaire"})
print(response.json())
print(response.status_code)