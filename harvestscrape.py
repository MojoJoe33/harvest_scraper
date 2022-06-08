from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.halfbakedharvest.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('harvest_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'link'])

for article in soup.find_all('article'):

    # print(article.prettify())

    headline = article.h3.a.text
    print(headline)

    #summary = article.div.find('p', class_='block-featured-latest__first-post-excerpt').text
    #print(summary)

#    try:
#        summary = article.div.find('p', class_='block-featured-latest__first-post-excerpt').text
#    except Exception as e:
#        summary = None

#    print(summary)

    link = article.find('a', href=True)['href']
    print(link)

    # vid_src = article.find('iframe', class_='youtube-player')['src']
    # print(vid_src)

    # vid_id = vid_src.split('/')[4]
    # vid_id = vid_id.split('?')[0]
    # print(vid_id)

    # yt_link = f'https://youtube.com/watch?v={vid_id}'
    # print(yt_link)

    print()
    csv_writer.writerow([headline, link])

csv_file.close()
