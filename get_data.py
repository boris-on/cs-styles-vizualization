import requests
from bs4 import BeautifulSoup
import csv
import time
from configure import fieldnames
headers = {
    "User-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
}



def get_data(link, session):

    metricks = {}
    id, nick = link.split("/")[3:]
    metricks["id"] = id
    metricks["nick"] = nick

    link1 = "https://www.hltv.org/stats/players/{}/{}".format(id, nick)
    link2 = "https://www.hltv.org/stats/players/individual/{}/{}".format(id, nick)
    link3 = "https://www.hltv.org/stats/players/weapon/{}/{}".format(id, nick)
    links = [link1, link2, link3]
    
    for link in links:  
        data = session.get(link, headers=headers)
        data = BeautifulSoup(data.text, "html.parser")
        stats = data.find_all("div", {"class": "stats-row"})
        t=0
        while len(stats) == 0:
            data = session.get(link, headers=headers)
            data = BeautifulSoup(data.text, "html.parser")
            stats = data.find_all("div", {"class": "stats-row"})
            print("access denied", t, "seconds for", nick, end="\r")
            t+=5
            time.sleep(5)

        for attr in stats:
            attr = [text for text in attr.stripped_strings]
            if "weapon" in link:
                if "knife" in attr[1] or attr[1] in ['elite', 'bayonet', 'inferno']:
                    metricks["knife"] = attr[2]
                else:
                    metricks[attr[1]] = attr[2]
            else:    
                metricks[attr[0]] = attr[1]

    return metricks