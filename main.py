import requests
from bs4 import BeautifulSoup
from get_data import get_data
import time
import csv
from configure import fieldnames

session = requests.Session()

with open('data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    with open("player_list.txt", "r") as f:
        data = f.read().split("\n")
    k=0

    for player in data:
        k+=1
        try:
            player_data = get_data(player, session)
        except requests.exceptions.ConnectionError:
            time.sleep(30)
            player_data = get_data(player, session)
                    
        writer.writerow(player_data)

        print("{} from 700+=".format(k), end="\r")