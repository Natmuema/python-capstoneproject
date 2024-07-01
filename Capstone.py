import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = 'https://www.myjobmag.co.ke/'


def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def parse_html(content):
    return BeautifulSoup(content, 'lxml')


def extract_job_links(soup):
    job_links = []
    job_list = soup.find_all('ul', class_='job-list')
    for item in job_list:
        for link in item.find_all('a', href=True):
            job_links.append(BASE_URL + link['href'])
    return job_links


def extract_job_details(soup):
    title = soup.find('h2').text.strip() if soup.find('h2') else None
    job_industry = soup.find('li', class_='job-industry').text.strip() if soup.find('li',
                                                                                    class_='job-industry') else None
    date_posted = soup.find('div', class_='read-date-sec-li').text.strip() if soup.find('div',
                                                                                        class_='read-date-sec-li') else None
    job_description = soup.find('li', class_='job-description').text.strip() if soup.find('li',
                                                                                          class_='job-description') else None
    job_keyInfo = soup.find('ul', class_='job-key-info').text.strip() if soup.find('ul',
                                                                                   class_='job-key-info') else None

    return {
        'title': title,
        'job_industry': job_industry,
        'date_posted': date_posted,
        'job_description': job_description,
        'job_keyInfo': job_keyInfo
    }


def save_to_csv(job_data, filename='jobs.csv'):
    keys = job_data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(job_data)


def main():
    search_url = 'https://www.myjobmag.co.ke/search/jobs?q=software+engineer&location='
    search_content = fetch_page(search_url)
    search_soup = parse_html(search_content)

    job_links = extract_job_links(search_soup)

    job_data = []
    for link in job_links:
        job_content = fetch_page(link)
        job_soup = parse_html(job_content)
        job_details = extract_job_details(job_soup)
        job_data.append(job_details)

    save_to_csv(job_data)


if __name__ == '__main__':
    main()
















