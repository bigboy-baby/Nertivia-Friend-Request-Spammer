#Code by bigboybigboi#0001 skid if ur homosexual (ew)
import httpx, random, string
import aiohttp
from aiohttp.client import ClientSession
import asyncio

count = 0

async def addFriend(token, username, iden, am):
  global count
  r = httpx.post("https://nertivia.net/api/user/relationship", json={"username":username,"tag":iden}, headers={"authorization": token})
  res = r.json()
  count+=1
  if res["status"] == True:
    print(f"Sent Friend Request [{count}/{am}]")
  else:
    print(f"Failed to Send Friend Request [{count}/{am}]")

async def loadtokens(tag):
  split = tag.split(":")
  username = split[0]
  iden = split[1]

  token_file = open('tokens.txt', 'r')
  tokens = token_file.read()
  tokenlist = tokens.split("\n")
  am = len(tokenlist)
  print(f"{am} Accounts Loaded")

  for token in tokenlist:
    await addFriend(token, username, iden, am)


tag = input("User's Tag: ")
asyncio.run(loadtokens(tag))
