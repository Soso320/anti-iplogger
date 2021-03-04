from proxy_requests import ProxyRequests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareEngine
import time

points = 0

url = input("\nEnter url\n>")
ref = input("\nEnter referer (Press enter for none\n>")
numb = int(input("\nEnter number of request(s)\n>"))

def getagent():
    software_engines = [SoftwareEngine.WEBKIT.value, SoftwareEngine.GECKO.value, SoftwareEngine.BLINK.value]
    user_agent_rotator = UserAgent(software_engines=software_engines, limit=5000)
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent

print(f"\nProcessing {numb} request(s) for {url}")
start_time = time.time()
for i in range(numb):
    start_time = time.time()
    agent = getagent()
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
print(f"\n-------- Execution time --------\n--- {time.time() - start_time} seconds ---")
