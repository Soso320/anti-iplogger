from fake_useragent import UserAgent
from proxy_requests import ProxyRequests
import time

points = 0
ua = UserAgent()

url = input("\nEnter url\n>")
ref = input("\nEnter referer (Press enter for none\n>")

while True:
    agen = input("\nEnter UserAgent\n>")
    start_time = time.time()
    agent = agen
    headers = {
        'User-agent': f'{agent}',
        'referer': f'{ref}'
    }
    r = ProxyRequests(url)
    r.set_headers(headers)
    r.get_with_headers()
    points += 1
    print(f"\nRequest #{points} with useragent {agent} Sent [{(time.time() - start_time)} Seconds]")
