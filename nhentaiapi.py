from bs4 import BeautifulSoup
import requests
import os.path
import os

# Author Dichill
# Please delete the folders on "Image/preview/ when using the same code on getPreviews it will give an error statement
# My lazy ass wont fix it, theres a lot of room for improvement, so please if you have some spare time dont mind snipping my code
# but atleast give some credits c:
# Enjoy.

class nhentai:
    def __init__(self):
        self.source = 'http://nhentai.net/g/'
        self.bad_chars = ["/", ":", "*", "?", '"', "<", ">", "|"]

    def getPreviews(self, code, imglimit):
        result = self.source + code
        api_url = requests.get(result).text

        # Read HTML
        soup = BeautifulSoup(api_url, 'lxml')

        # Get Clean Title
        title = soup.find('span', class_='before').text
        title = title + soup.find('span', class_='pretty').text
        cltitle = title

        for i in self.bad_chars:
            cltitle = cltitle.replace(i, '')

        # Path
        cwd = os.getcwd()  # get the current path
        prevpath = cwd + "\\image\\preview\\"

        try:
            os.mkdir(prevpath + cltitle + "/")
            print("Creating Directory ./.")
        except OSError:
            print("Directory already exist so Folder Creation was skipped!")

        try:
            imagelinks = []
            print("Finding Images..")
            wrappers = soup.findAll("img", {"class":"lazyload"}, limit=imglimit)
            for result in wrappers:
                imagelinks.append(result['data-src'])
            for i, imagelink in enumerate(imagelinks):
                r = requests.get(imagelink)
                print("Downloading Files " + str(i + 1))
                open(prevpath + str(cltitle) + "/" + " " + str(i+1) + ".png", 'wb').write(r.content)
        except:
            print()

    def getTags(self, code):
        result = self.source + code
        api_url = requests.get(result).text

        soup = BeautifulSoup(api_url, 'lxml')

        # Get Tags
        containers = soup.find_all("section", {"id": "tags"})
        print("Finding Containers with Tags")
        for container in containers:
            wrappers = container.find_all('div')
            print("==============================================")
            for x in wrappers:
                tags = x.find('span', class_='tags')
                for l in tags:
                    try:
                        nametag = l.find('span', class_='name')
                        print(nametag.get_text())
                    except:
                        print()  # Get the Error which is no Tags can be found!
            print("==============================================")

    def check(self, code):
        result = self.source + code
        api_url = requests.get(result).text

        # HTML File
        soup = BeautifulSoup(api_url, 'lxml')
        print("Scraping HTML ./.")

        # Get Title
        title = soup.find('span', class_='before').text
        title = title + soup.find('span', class_='pretty').text
        print("Getting Title..")
        cltitle = title

        for i in self.bad_chars:
            cltitle = cltitle.replace(i, '')
        print("Cleaning Title to avoid Illegal Characters")
        # Get Thumbnail
        tburl = soup.find('img', class_='lazyload')
        print("Getting Thumbnail ./.")
        r = requests.get(tburl['data-src'])
        open("./image/" + str(cltitle) + ".png", 'wb').write(r.content)
        print("Thumbnail saved to image Folder")

        # Return
        return print("Title: " + title)