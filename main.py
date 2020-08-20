import os
import requests

from fake_useragent import UserAgent

points = 0
ua = UserAgent()
print("\nWARNING: Run with a VPN to avoid your real ip getting logged!\n")
print("Enter the ip logger url:")
url = input()

r = requests.get(url)
if r.status_code != 404:
    print("Valid url")
elif r.status_code in {404}:
    print("404 not found")
    os.exit()
else:
    print(r.status_code)
    os.exit()

print("\nHow many requests?")
numb = int(input())

print(f"\nProcessing {numb} requests for {url}")

for i in range(numb):
    agent = (ua.random)
    headers = {
        'User-agent': f'{agent}'
    }
    r = requests.get(url, headers=headers)
    points += 1
    print(f"Request #{points} with useragent {agent}")

print(f"\n\nSuccessfully spammed {url}!")
