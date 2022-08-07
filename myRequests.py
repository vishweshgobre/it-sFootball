import requests
import json

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

querystring = {"date": "2022-08-05"}

headers = {
	"X-RapidAPI-Key": "06081b91aemsh2d57173bcdadb99p1e4577jsnc26ef96b9a3a",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


if response.status_code == 200:
	with open("data.json", "w") as d:
		data = response.json()
		json.dump(data, d) 
	
else:
	print("An error occurred")
