from bs4 import BeautifulSoup
import requests

url = 'https://www.linkedin.com/jobs/search/?currentJobId=3242246532&f_E=1&f_PP=102681496&keywords=software%20engineer%20internship&originalSubdomain=uk&sortBy=R'
page = requests.get(url)
doc = BeautifulSoup(page.text, 'html.parser')
#print(doc.prettify())

#get <a> tag with class 'hidden-nested-link' for company name
tagsWnames = doc.find_all(class_='hidden-nested-link')
companies_list = []
for i in range(len(tagsWnames)):
    company = tagsWnames[i].text.strip()
    companies_list.append(company)
#print(companies_list)

internship_dict = {}
for company in companies_list:
    internship_dict[company] = {}
#print(internship_dict)

#get <h3> tag with class 'base-search-card__title' for post title
tagsWtitle = doc.find_all(class_='base-search-card__title')
titles_list = []
for i in range(len(tagsWtitle)):
    title = tagsWtitle[i].text.strip()
    titles_list.append(title)
#print(titles_list)

for title in titles_list:
    for company in internship_dict:
        internship_dict[company]['title'] = title
#print(internship_dict)

#get <time> tag with class 'job-search-card__listdate' for date posted
tagsWdate = doc.find_all(class_='job-search-card__listdate')
dates_list = []
for i in range(len(tagsWdate)):
    date = tagsWdate[i].text.strip()
    dates_list.append(date)
#print(dates_list)

for date in dates_list:
    for company in internship_dict:
        internship_dict[company]['date posted'] = date
#print(internship_dict)

#get link for post webpage
tagsWlink = doc.find_all(class_='base-card__full-link')
links_list = []
for i  in range(len(tagsWlink)):
    link = tagsWlink[i]['href']
    links_list.append(link)
#print(links_list)

for link in links_list:
    for company in internship_dict:
        internship_dict[company]['link for post'] = link
print(internship_dict)