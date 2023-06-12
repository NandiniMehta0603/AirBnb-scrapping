from bs4 import BeautifulSoup
import requests
import pandas as pd

Names=[]
Price=[]
Desc=[]
Reviews=[]

url="https://www.airbnb.co.in/s/New-Delhi--India/homes?adults=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes"

r=requests.get(url)
# print(r)
soup=BeautifulSoup(r.text,"lxml")

# while True:
for i in range(1:17):
    np=soup.find("a",class_="l1ovpqvx c1ytbx3a dir dir-ltr").get("href")
    # print(np)
    cnp= "https://www.airbnb.co.in"+np
    # print(cnp)

    url=cnp
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="gsgwcjk g8ge8f1 g14v8520 dir dir-ltr")
    names=box.find_all("div",class_="t1jojoys dir dir-ltr")
    # print(names)
    for i in names:
        n=i.text
        Names.append(n)

    prices=box.find_all("span",class_="_tyxjp1")
    # print(prices)
    for i in prices:
        n=i.text
        Price.append(n)

    desc=box.find_all("div",class_="fb4nyux s1cjsi4j dir dir-ltr")
    # print(desc)
    for i in desc:
        n=i.text
        Desc.append(n)

    reviews=box.find_all("span",class_="r1dxllyb dir dir-ltr")
    # print(reviews)
    for i in reviews:
        n=i.text
        Reviews.append(n)

    print(len(Names))
    print(len(Price))
    print(len(Desc))
    print(len(Reviews))

df=pd.DataFrame({"Name":Names,"Prices/night":Price,"Description":Desc,"Reviews":Reviews})
# print(df)
df.to_csv("airbnb_delhi_stay.csv")
