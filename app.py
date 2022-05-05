import csv
import requests
from bs4 import BeautifulSoup

start_url_brightest = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page_brightest = requests.get(start_url_brightest)
soup_brightest = BeautifulSoup(page_brightest.content, "html.parser")

start_url_brown_dwarfs = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page_brown_dwarfs = requests.get(start_url_brown_dwarfs)
soup_brown_dwarfs = BeautifulSoup(page_brown_dwarfs.content, "html.parser")

headers = ["Name", "Distance", "Mass", "Radius"]
brightest_star_data = []
brown_dwarf_star_data = []

def scrap_brightest():
    data = soup_brightest.find("div", attrs = { "class", "mw-body-content mw-content-ltr" })
    
    for i in data.find_all("tr"):
        temp_list = []
        try:
            td = i.find_all("td")
            if td[1].text.split("\n")[0] != "Sun":
                temp_list.append(td[1].text.split("\n")[0].split("[")[0])
                temp_list.append(float(td[3].text.split("\n")[0].split("[")[0]))
                temp_list.append(td[5].text.split("\n")[0])
                temp_list.append(td[6].text.split("\n")[0])
            else:
                continue
        except:
            continue
        brightest_star_data.append(temp_list)

def scrap_brown_dwarfs():
    data = soup_brown_dwarfs.find_all("table")

    for i in data[5].find_all("tr"):
        temp_list = []
        try:
            td = i.find_all("td")
            temp_list.append(td[0].text.split("\n")[0])
            temp_list.append(td[5].text.split("\n")[0])
            temp_list.append(float(td[7].text.split("\n")[0]))
            temp_list.append(float(td[8].text.split("\n")[0]))
        except:
            continue
        brown_dwarf_star_data.append(temp_list)

scrap_brightest()
scrap_brown_dwarfs()

with open("brightest.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    for star in brightest_star_data:
        try:
            csv_writer.writerow(star)
        except:
            continue

with open("brown_dwarfs.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    for star in brown_dwarf_star_data:
        try:
            csv_writer.writerow(star)
        except:
            continue