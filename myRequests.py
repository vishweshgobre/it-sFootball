import requests

url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

querystring = {"season":"2020"}

headers = {
	"X-RapidAPI-Key": "06081b91aemsh2d57173bcdadb99p1e4577jsnc26ef96b9a3a",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
