import requests
import argparse

def request(url):
    try:
        get_response = requests.get("http://" + url)
        return get_response
    except requests.exceptions.ConnectionError:
        pass


url = "google.com"

with open('subdomain.txt', 'r') as wordlist:
    for subdomain in wordlist:
        target_url = subdomain.strip('\n') + "." + url
        response = request(target_url)
        if response:
            print("[+] Subdomain Discovered --> ", target_url)