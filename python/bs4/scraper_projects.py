import bs4
import requests


BASE_URL = 'https://www.prontotools.io/'
PROJECTS_URL = f'{BASE_URL}projects/'


def pull_site():
    raw_site_page = requests.get(PROJECTS_URL)
    raw_site_page.raise_for_status()
    return raw_site_page


def scrape(site):
    project_list = []

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_project_list = soup.select('h2 a')
    for each in html_project_list:
        if 'http' not in each['href']:
            url = f"{BASE_URL}{each['href']}"
        else:
            url = each['href']

        project_list.append((each.getText(), url))

    return project_list


if __name__ == '__main__':
    site = pull_site()

    print()
    print('### Projects')
    project_list = scrape(site)
    for name, url in project_list:
        print(f'* {name} - {url}')
