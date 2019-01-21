import requests


def main():
    url = input("Digite o endereco:\n>> ")
    r = requests.get(url, stream=True)
    with open('img1.jpg', 'wb') as im:
        for item in r.iter_content():
            im.write(item)


if __name__ == '__main__':
    main()
