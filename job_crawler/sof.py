import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def extract_sof_pages():

  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  
  last_page = int(pages[-2].find("span").string)
  
  return last_page



def extract_job(html):

  title = html.find("a",{"class":"s-link"})["title"]

  
  company, location = html.find("h3", {"class":"fc-black-700"}).find_all("span", recursive=False)
  
  if company.string != None:
    company = company.string.strip()
  if location.string != None:
    location = location.string.strip()

  job_id = html["data-jobid"]

  return {
    "title": title,
    "company": company,
    "location": location,
    "apply_link": f"https://stackoverflow.com/jobs/{job_id}"
    }



def extract_sof_jobs(last_page):
  jobs = []

  
  for page in range(last_page):
    print(f"scraping sof page {page+1}")
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    #print(results)
    for result in results:
      job = extract_job(result)
      
      jobs.append(job)


  for result in results:
    job = extract_job(result)
    jobs.append(job)

  return jobs


def get_sof_jobs():
  last_page = extract_sof_pages()

  jobs = extract_sof_jobs(last_page)

  return jobs