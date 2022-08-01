import requests
from bs4 import BeautifulSoup
import random
from time import sleep
import sys
import smtplib, ssl
import re

def scrape(KeyWord, Email):
    word = KeyWord
    keyword = ('"{}"').format(word)
    n_pages = 4
    result = []
    html_result = []
    descriptions = []
    q = ['"@gmail.com" site:facebook.com','"@gmail.com" site:twitter.com','"@gmail.com" site:linkedin.com','"@gmail.com" site:instagram.com']

    queries = []

    for value in q:
        queries.append(keyword + ' ' + str(value))

    user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]
    for _ in user_agent_list:
        user_agent = random.choice(user_agent_list)

    headers = {'User-Agent': user_agent,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


    def serp_data():
        for query in queries:
            for page in range(1, n_pages):
                url = "https://www.google.com/search?q=" + \
                    query + "&start=" + str((page - 1) * 10) + "&num=100"
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')
                texts = soup.findAll(text=True)
                description=soup.find_all('div', class_="VwiC3b")
                result.append(texts)
                html_result.append(soup)
                print("Scraping Query: ", query,"page number: ", page)
                for d in description:
                    descriptions.append(d.text)
                print("---------------------------->",len(descriptions))
                if len(descriptions) == 0:
                    sys.exit()
                sleep(3)
            
    serp_data()

    data = str(descriptions)
    content = data.lower()

    result = re.findall("([\w.-]+@[\w.-]+[.]\w{2,3})", content)

    # Removing Duplicate Emails
    # Initialising the Variables Needed
    email_list = result
    final_list = []
    duplicates = []

    # Creating a loop to check duplicates
    for x in email_list:
        if x not in final_list:
            final_list.append(x)
        else:
            duplicates.append(x)
  
    regex = '^[a-z 0-9]+[\._]?[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

    valid_emails=[]
    invalid_emails=[]

    # Validate Emails
    def validate(email):
        if (re.fullmatch(regex, email)):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)

    # Validate the Scraped Email Ids
    for x in final_list:
        validate(x)

    msg = '\n'.join(valid_emails)

    te = len(email_list)
    de = len(duplicates)
    ve = len(valid_emails)

    scrape_details = f"Scape Details :\n\nTotal Emails Found : {te}\nDuplicate Emails : {de}\nValid Emails : {ve}"

    def send_email(keyword, body, receiver):
        sender = 'xagent.amber@gmail.com'
        passwd = 'jpiupfucjtflepsd'

        context = ssl.create_default_context()

        server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context)
        server.login(sender, passwd)
        message = f'Subject: Scraped Emails & Validated for {keyword} - emscraper\n\n{scrape_details}\n\n{body}\n\n Follow us on:\n\n Instagram : https://instagram.com/zanx.coders \n GitHub : https://github.com/zandora-space \n\nThankyou for choosing Emscraper, an tool of Zandora Space! '
        try:
            server.sendmail(sender, receiver, message)
            print("Mail has send Successfully, Check your inbox!")
        except IndexError:
            print("Mail has not send due to unexpected issue. Please try again!")
        server.quit()

    send_email(keyword=KeyWord, body=msg, receiver=Email)