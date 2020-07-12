import requests as r
from bs4 import BeautifulSoup

class preper:

    def __init__(self, tUrl, pgCnt):
        self.urls = self.tableOContents(tUrl, pgCnt)

    def tableOContents(self, tUrl, pgCnt):
        urls = []

        tSite = r.get(tUrl).text
        tSoup = BeautifulSoup(tSite, features="lxml").find("article",{"id":"post-40"})
        rawLinks = tSoup.find_all("a")

        if pgCnt == 0 or pgCnt == "":
            pgCnt = len(rawLinks)


        for link in range(pgCnt):
            if "http" in str(rawLinks[link].get("href")):
                urls.append(rawLinks[link].get("href"))
            elif str(rawLinks[link].get("href")) != "4031384495743822299":
                urls.append("https://" + str(rawLinks[link].get("href")))
            else:
                urls.append("https://pactwebserial.wordpress.com/2015/01/08/possession-15-2/")

        print(urls)
        return urls

class pages:
    def __init__(self, site):
        self.html = r.get(site).text
        self.soup = BeautifulSoup(self.html, features="lxml")

    def title(self):
        return self.soup.find("h1",{"class":"entry-title"}).text

    def mainText(self):
        return "<html><body>" + f"<h1>{self.title()}</h1><br>" + str(self.soup.find("div",{"class":"entry-content"})) + "</body></html>"
