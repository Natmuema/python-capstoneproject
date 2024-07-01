import requests
from bs4 import BeautifulSoup
from collections import Counter


def get_fuzu_jobs():
    url = "https://www.fuzu.com/jobs/software-engineering"  # Example URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for job_card in soup.find_all('div', class_='job-details-card'):
        title = job_card.find('h2', class_='job-title').text.strip()
        company = job_card.find('div', class_='company-name').text.strip()
        link = job_card.find('a', class_='job-title-link')['href']
        jobs.append({
            'title': title,
            'company': company,
            'link': f"https://www.fuzu.com{link}"
        })

    return jobs


def get_myjobmag_jobs():
    url = "https://www.myjobmag.co.ke/jobs-by-field/software-engineering"  # Example URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for job_card in soup.find_all('div', class_='job-title-text'):
        title = job_card.find('h2').text.strip()
        company = job_card.find('span', class_='job-company').text.strip()
        link = job_card.find('a')['href']
        jobs.append({
            'title': title,
            'company': company,
            'link': f"https://www.myjobmag.co.ke{link}"
        })

    return jobs


def extract_skills(job_url):
    response = requests.get(job_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example selector, this needs to be adjusted based on the actual HTML structure of the job page
    job_description = soup.find('div', class_='job-description').text

    # Simple keyword matching for skills (this can be enhanced)
    skills = ['Python', 'Java', 'SQL', 'Machine Learning', 'Data Analysis', 'R', 'C++', 'JavaScript', 'Django', 'Flask',
              'TensorFlow', 'Keras']
    found_skills = [skill for skill in skills if skill.lower() in job_description.lower()]

    return found_skills


def aggregate_skills(job_listings):
    all_skills = Counter()
    for job in job_listings:
        skills = extract_skills(job['link'])
        all_skills.update(skills)
    return all_skills


# Get jobs from both sites
fuzu_jobs = get_fuzu_jobs()
myjobmag_jobs = get_myjobmag_jobs()

# Aggregate skills from both job lists
all_jobs = fuzu_jobs + myjobmag_jobs
top_skills = aggregate_skills(all_jobs)

# Print the top skills
print("Top skills:")
for skill, count in top_skills.most_common():
    print(f"{skill}: {count}")

# Example of printing job details and extracted skills for verification
for job in fuzu_jobs[:2]:  # Limit to first 2 jobs for brevity
    skills = extract_skills(job['link'])
    print(f"Job Title: {job['title']}")
    print(f"Company: {job['company']}")
    print(f"Skills: {skills}")
    print(f"Link: {job['link']}")
    print()

for job in myjobmag_jobs[:2]:  # Limit to first 2 jobs for brevity
    skills = extract_skills(job['link'])
    print(f"Job Title: {job['title']}")
    print(f"Company: {job['company']}")
    print(f"Skills: {skills}")
    print(f"Link: {job['link']}")
    print()
