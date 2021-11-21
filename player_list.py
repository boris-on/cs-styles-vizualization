import json
from bs4 import BeautifulSoup

with open("mainpage.txt", "r") as f:
    data = f.read()

data = BeautifulSoup(data, "html.parser")
players = data.find_all("td", {"class": "playerCol"})
line = ""
for player in players:
    player = player.a["href"]
    line += "{}\n".format(player)
with open("player_list.txt", "w") as f:
    f.write(line)