import json

def is_Bundesliga(response):
    reqLeague = 78  #Bundesliga = 78
    my_teams = ["Borrussia Dortmund", "Bayer Leverkusen", "Bayern Munich", "Eintracht Frankfurt"]

    if response["league"]["id"] == reqLeague:
        if (response["teams"]["home"]["name"] in my_teams) or (response["teams"]["away"]["name"] in my_teams):
            return True
    else:
        return False

def is_Premier_League_England(response):
    reqLeague = 39  #Premier League England = 39
    my_teams = ["Manchester United", "Arsenal", "Manchester City", "Liverpool", "Chelsea", "Tottenham"]

    if response["league"]["id"] == reqLeague:
        if (response["teams"]["home"]["name"] in my_teams) or (response["teams"]["away"]["name"] in my_teams):
            return True
    else:
        return False


with open("data.json", "r") as d:
    data = json.load(d)

response = data["response"]

premierLeague = filter(is_Premier_League_England, response)
print("Premier League:")
for p in premierLeague:
    print(f"\t{p['teams']['home']['name']} - {p['teams']['away']['name']}")

print(" ")

bundesliga = filter(is_Bundesliga, response)
print("Bundesliga")
for b in bundesliga:
    print(f"\t{b['teams']['home']['name']} - {b['teams']['away']['name']}")