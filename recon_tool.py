import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re


target_url=input("Enter an URL: ")

print(f"Scanning : {target_url}...")
#must do header manupilation because don't have permission to access to site (403)
headers_param={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

response=requests.get(target_url,headers=headers_param) #to surf internet with fake id

print(f"State code: {response.status_code}")

if response.status_code==200: #if received correctly the packet
    soup=BeautifulSoup(response.text, 'html.parser') #write in text 

    emails=r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
    found_emails=re.findall(emails,response.text)
    print(f"Total email found: {len(found_emails)}")
    uniq_emails=set(found_emails)

    all_links= soup.find_all('a') #to find <a> label(link)
    print(f"Total tags found: {len(all_links)}")
    time=datetime.now()

    with open ("recon_report.txt","w",encoding="utf-8") as f:
        f.write(f"Target url: {target_url}\n")
        f.write(f"Scanning time: {time}")
        f.write("\n"+f"-"*30+"\n")
        
        f.write(f"[EMAILS FOUND]({len(uniq_emails)})\n")
        if len(uniq_emails)>0:
            for email in uniq_emails:
                f.write(email+"\n")
        else:
            f.write("No emails found on this page. \n")
        f.write("\n"+f"-"*30+"\n")
        for link in all_links:
            href=link.get('href') #to take addresses  (diffrernt from req... .get)
            if href and href.startswith('http'):
                f.write(href+"\n")
        print(f"-"*30+"\n")
        print(f"Report saved...")

