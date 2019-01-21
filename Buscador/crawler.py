import requests
from bs4 import BeautifulSoup
import re
import itertools as ils


def main():
    url = input("Enter the endress site:\n>> ")
    keyword = input("Enter the keyword:\n>> ")
    deth = int(input("Enter the deth search:\n>> "))

    if deth <= 0:
        search(keyword, url)
    else:
        list_links = get_links(url)
        print("ANTES:")
        print_list(list_links)
        index = 0
        for i in range(deth):
            for j in range(index, len(list_links)):
                search(keyword, list_links[j])
            list_links += list(ils.chain(*[get_links(list_links[a]) for a in range(index, len(list_links))]))
            index = len(list_links)
            print("\nVOLTA %d:" % i)
            print_list(list_links)


def search(keyword, url):
    response = requests.get(url)
    page_no_tags = BeautifulSoup(response.text, 'html.parser')
    results = re.findall(r'..........' + keyword + '..........', page_no_tags.text)

    print("\nResultados encontrados em %s:" % url)
    if len(results) > 0:
        for result in results:
            print(result)
    else:
        print("Nenhum resultado encontrado.")


def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='lxml')
    links_raw = soup.findAll('a', attrs={'href': re.compile("^http://")})
    list_links = [str(i.get('href')) for i in links_raw]
    return list_links


def print_list(lista):
    for item in lista:
        print(item)


if __name__ == '__main__':
    main()
