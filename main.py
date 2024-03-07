import requests
import selectorlib
from datetime import datetime


URL = 'http://programmer100.pythonanywhere.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['temp']
    return value


def read(data):
    with open('data.txt', 'r') as file:
        return file.read()


def store(extracted):
    now = datetime.now()
    with open('data.txt', 'a') as file:
        file.write(f'{now.strftime("%d-%m-%y-%H-%M-%S")},' + extracted + "\n")


if __name__ == '__main__':
    scraped_data = scrape(URL)
    extracted_data = extract(scraped_data)
    #content = read(extracted_data)
    store(extracted_data)
