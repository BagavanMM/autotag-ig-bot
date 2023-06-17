from instagrapi import Client
import pandas as pd
import random as random
from time import sleep

# LOGIN INFORMATION
USERNAME = ""
PASSWORD = ""

cl = Client()
cl.login(USERNAME, PASSWORD)

link = input("Input link to instagram post: ")
media_id = cl.media_id(cl.media_pk_from_url(link))
# LOAD USERNAME LIST
users = pd.read_csv("list.csv")

for i in range(len(users.Username)):
    seconds = random.randint(3,7)
    sleep(seconds)
    user = users.Username[i]
    comment = cl.media_comment(media_id, user)

print("Complete")