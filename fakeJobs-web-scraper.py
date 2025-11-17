import requests
from bs4 import BeautifulSoup

search = input("Enter job title here: ")

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
result = soup.find(id="ResultsContainer")

python_jobs = result.find_all(
    "p", class_="location", string=lambda text: search.lower() in text.lower()
)

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

if python_job_cards:
    for job_card in python_job_cards:
        title_element = job_card.find("h2", class_="title")
        company_element = job_card.find("h3", class_="company")
        location_element = job_card.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        link_url = job_card.find_all("a")[1]["href"]
        print(f"Apply here: {link_url}\n")
else:
    print("No jobs Found 🥺.")
