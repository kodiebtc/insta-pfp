import requests
from bs4 import BeautifulSoup

username = input("Enter Instagram username: ")
url = "https://www.instagram.com/{}/".format(username)

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
image_url = soup.find("meta", property="og:image")["content"]

image_data = requests.get(image_url).content
with open("{}.jpg".format(username), "wb") as handler:
    handler.write(image_data)

print("Profile picture downloaded successfully!")
