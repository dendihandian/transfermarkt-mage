from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import get
from datetime import datetime
import json

transfermarkt_url = 'https://www.transfermarkt.com'
request_headers = {'user-agent': 'transfermarkt-mage'}

def parse_transfers(html_soup, transfers_date):
    # parse to get list of transfers
    transfers_soups = html_soup.find('div', class_='responsive-table').find('div', id="yw1", class_='grid-view').find('table', class_='items').find('tbody')

    # filter only bs4.element.Tag types
    transfers_soups = list(filter(lambda soup: type(soup) is Tag, transfers_soups))

    transfers = []
    for transfer_soup in transfers_soups:
        # column 1
        player_id = transfer_soup.find_all('td', recursive=False)[0].find('table', class_='inline-table').find_all('tr')[0].find_all('td', recursive=False)[1].find('a')['href'].split('/')[-1]
        name = transfer_soup.find_all('td', recursive=False)[0].find('table', class_='inline-table').find_all('tr')[0].find_all('td', recursive=False)[1].find('a').string
        portrait_url = transfer_soup.find_all('td', recursive=False)[0].find('table', class_='inline-table').find_all('tr')[0].find_all('td', recursive=False)[0].find('img')['data-src']
        position = transfer_soup.find_all('td', recursive=False)[0].find('table', class_='inline-table').find_all('tr')[1].find_all('td', recursive=False)[0].string

        # column 2
        age = transfer_soup.find_all('td', recursive=False)[1].string

        # column 3
        nationalities = []
        for img in transfer_soup.find_all('td', recursive=False)[2].find_all('img', recursive=False):
            nationalities.append({'name': img['title'], 'url': img['src']})

        # wrap transfer into dict and enlist
        transfers.append({
            'portrait_url': portrait_url,
            'name': str(name),
            'player_id': player_id,
            'position': str(position),
            'age': age,
            'nationalities': nationalities,
            'transfer_date': transfers_date,
        })

    return transfers

def get_transfers_by_date(date=datetime.now().strftime("%Y-%m-%d"), page_start=1):

    path = f'/transfers/transfertagedetail/statistik/top/land_id_zu/0/land_id_ab/0/leihe//datum/{date}/sort//plus/1/page/{page_start}'
    next_page = True

    transfers = []
    while next_page:
        url = transfermarkt_url + path
        r = get(url, headers=request_headers)

        html_soup = BeautifulSoup(r.text, 'html.parser')
        if html_soup:
            transfers = transfers + parse_transfers(html_soup, date)

        next_page_soup = html_soup.find('li', class_='tm-pagination__list-item tm-pagination__list-item--icon-next-page')
        if (next_page_soup):
            path = next_page_soup.find('a', class_='tm-pagination__link')['href']
        else:
            next_page = False

    with open(f'{date}.json', 'w') as outfile:
        outfile.write(json.dumps(transfers, indent=4, ensure_ascii=False))

if True:
    get_transfers_by_date('2023-02-03')

