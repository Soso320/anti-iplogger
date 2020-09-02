from fake_useragent import UserAgent
from proxy_requests import ProxyRequests
import time

points = 0
ua = UserAgent()

url = input("\nEnter url\n>")
ref = input("\nEnter referer (Press enter for none\n>")
numb = int(input("\nEnter number of request(s)\n>"))

print(f"\nProcessing {numb} request(s) for {url}")
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

print(f"\nSuccessfully spammed {url} {numb} time(s)!\n")

print("\n-------- Execution time --------\n--- %s seconds ---" % (time.time() - start_time))
