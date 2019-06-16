from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.indiatoday.in/news.html")

soup = BeautifulSoup(res.text,'lxml')

topHeadlines = soup.find_all('h3',{'class':'news-page-feature'})


print("Top Headlines :\n")
for n,i in enumerate(topHeadlines):
    news = i.find('a')
    print("{}. {}\n".format(n+1,news.text))


categories = soup.find_all('div',{'class':'col-md-6 col-sm-6 col-xs-12'})
for i in categories:
    title = i.find('span',{'class':'widget-title'}).find('a').text
    print(title.upper() + " :")

    newsList = i.find('div',{'class':'data-holder'}).find('div',{'class':'section-ordering'}).find_all('p')
    for n,j in enumerate(newsList):
        news = j.find('a').text
        print("{}. {}\n".format(n+1,news))


categories = soup.find_all('div',{'col-md-6 col-sm-6 col-xs-12 mt-50'})
for i in categories:
    title = i.find('span',{'class':'widget-title'}).find('a').text
    print(title.upper() + " :")

    newsList = i.find('div',{'class':'data-holder'}).find('div',{'class':'section-ordering'}).find_all('p')
    for n,j in enumerate(newsList):
        news = j.find('a').text
        print("{}. {}\n".format(n+1,news))
