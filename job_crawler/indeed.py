import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():

  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})
  links = pagination.find_all('a')
  
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))

  last_page = pages[-1]

  return last_page



def extract_job(html):

  title = html.find("h2", {"class":"title"}).find("a")["title"]  
  
  company = html.find("span", {"class":"company"})
  if company.find("a") != None:
    company = company.find("a")
  company = company.string.strip()

  location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
  
  job_id = html["data-jk"]

  return {
    "title": title,
    "company": company,
    "location": location,
    "link": f"https://www.indeed.com/viewjob?jk={job_id}"
    }



def extract_indeed_jobs(last_page):
  jobs = []

  
  for page in range(last_page):
    print(f"scraping indeed page {page+1}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})

    for result in results:
      job = extract_job(result)
      jobs.append(job)
  

  for result in results:
    job = extract_job(result)
    jobs.append(job)

  return jobs


def get_indeed_jobs():
  last_page = extract_indeed_pages()

  jobs = extract_indeed_jobs(last_page)

  return jobs
