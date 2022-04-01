from bs4 import BeautifulSoup
import requests
from time import sleep
from playsound import playsound

people = 0
time = ""
while True:
    html_text = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vT_D5o86cDxQ5giuqzusqf-SoDYGvs-0iQjLJHOk08xPpJagce2AU_NDld_sttngTnJMbdSJQ-8wXsk/pubhtml").text
    soup = BeautifulSoup(html_text, 'lxml')
    listings = soup.findAll('tr', style = "height: 20px")
    for listing in listings:
        entry =  listing.find('td', class_ = "s4", dir = "ltr")
        if  not entry == None:
            place = listing.find('td', class_ = "s4", dir = "ltr").text
        else:
            continue
        if ("dublin" in place.lower()):
                lineinfo = listing.find('td', class_ = "s9", dir = "ltr")
                time = lineinfo.text
                people = int(lineinfo.findNext().findNext().text)
    print(time + " CDT")
    print(people)
    if people > 40:
        playsound("alarm.wav")
    sleep(60)