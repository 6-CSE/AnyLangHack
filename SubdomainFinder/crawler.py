import requests
import argparse

# get response of url if it exists or not
def request(url):
    try:
        get_response = requests.get("http://" + url)
        return get_response
    except requests.exceptions.ConnectionError:
        pass


# change this url to crawl and find subdomains 
url = "google.com"

# from the list of subdomains find which one exists for the given url
with open('subdomain.txt', 'r') as wordlist:
    for subdomain in wordlist:
        target_url = subdomain.strip('\n') + "." + url

        # get response
        response = request(target_url)

        # if response is 200 OK, then print subdomain discovered
        if response:
            print("[+] Subdomain Discovered --> ", target_url)