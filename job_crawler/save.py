import csv


def save_to_csv(jobs):
  file = open("jobs.csv", "w")
  writer = csv.writer(file)

  writer.writerow(["title","company","location","link"])

  for job in jobs:
    writer.writerow(job.values())