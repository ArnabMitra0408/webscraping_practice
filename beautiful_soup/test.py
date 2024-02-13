import bs4
import requests
#getting times jobs python data
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup=bs4.BeautifulSoup(html_text,'lxml')
jobs=soup.find_all("li",{"class":"clearfix job-bx wht-shd-bx"})
for job in jobs:
    cmp=job.find('h3',{"class":"joblist-comp-name"}).text.replace(' ','')
    skill=job.find('span',{'class':'srp-skills'}).text
    posted_when=job.find('span',{'class':'sim-posted'}).text
    print(cmp)
    print(skill)
    print(posted_when)
#print('no error')