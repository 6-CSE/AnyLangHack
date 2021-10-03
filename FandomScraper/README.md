# Fandom Scraper 
This script can scrape all the data you need \
This was originally made for Fandom Wiki which has information about any topic , transcripts etc. \
With a few adjustments you can potentially scrape any website

**How to setup:** \
1.Open a page you want to scrape , note down its URL , class of elements which actually have useful data (Use inspect element) \
2.Open fandom_scraper.py in your favourite editor (My recommendation is VS Code) \
3.Change the URL , Target Keyword , Class of elements to search and base

Now Run the script as shown below 

**Usage :** (Assuming you have python and pip set up already) 

`$pip install -r requirements.txt ` \
`$python fandom_scraper.py > output.txt`

As a example I have setup the script to scrape the Call of Duty Fandom for Transcripts \
This gives me every word spoken in every COD ever.

Future Improvements : \
Multiple Keywords support and faster scraper with async requests 