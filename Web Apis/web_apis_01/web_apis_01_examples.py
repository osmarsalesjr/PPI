import requests


def main():
    cep = '64005630'
    url = "https://viacep.com.br/ws/%s/json/" % cep

    response = requests.get(url).json()

    for key in response.keys():
        print(response[key])


if __name__ == '__main__':
    main()
