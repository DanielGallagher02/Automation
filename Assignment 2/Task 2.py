# Task 2
# By: Daniel Gallagher

# Importing the libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function that can get to each different web page to extract the information 
def extract(page):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36' }
	url = f'https://ie.indeed.com/jobs?q=python%20developer&l=dublin&start={page}'
	r = requests.get(url, headers)
	soup = BeautifulSoup(r.content, 'html.parser')
	return soup

# Function where i am passing soup values and using HTML code parameters
def transform(soup):
    # Using the div variable which is representing the job container of all the searched jobs
	divs = soup.find_all('div', class_ = 'slider_container css-11g4k3a eu4oa1w0')
	for item in divs:
		title = item.find('a').text
		company = item.find('span', class_ = 'companyName').text
        # The salary is not given for all the job cards or search results
        # and if we add the salary tag it will give us errors so we need to make
        # try catch to handle errors
		try: 
			salary = item.find('span', class_ = 'metadata salary-snippet-container').text
		except:
			salary = ''
		summary = item.find('div', {'class' : 'job-snippet'}).text.replace('\n', '')


		job = {
			'title': title,
			'company': company,
			'salary': salary,
			'summary': summary
		}
		joblist.append(job)
	return	

joblist = []

# using a for loop beacuse its a dynamic page and dont want
# to separate code for each different page
# uses 4 pages 0, 10, 20 and 30 
for i in range(0,40,10):
	print(f'Getting page, {i}')
    # extracting the information from the webpage using the function
	c = extract(0)
	transform(c)

# saving my dictionary to a CSV file
df = pd.DataFrame(joblist)
print(df.head())

# called jobs.csv
df.to_csv('jobs.csv')
