from fake_useragent import UserAgent
from proxy_requests import ProxyRequests
import time

points = 0
ua = UserAgent()

print("\nEnter url:")
url = input()

print("\nEnter referer (Press enter for none)")
ref = input()

print("\nEnter number of requests")
numb = int(input())

print(f"\nProcessing {numb} requests for {url}")
start_time = time.time()
for i in range(numb):
    start_time = time.time()
    agent = (ua.random)
    headers = {
        'User-agent': f'{agent}',
        'referer': f'{ref}'
    }
    r = ProxyRequests(url)
    r.set_headers(headers)
    r.get_with_headers()
    points += 1
    print(f"\nRequest #{points} with useragent {agent} Sent [{(time.time() - start_time)} Seconds]")

print(f"\n\nSuccessfully spammed {url} {numb} times!")

print("-------- Execution time --------\n--- %s seconds ---" % (time.time() - start_time))
