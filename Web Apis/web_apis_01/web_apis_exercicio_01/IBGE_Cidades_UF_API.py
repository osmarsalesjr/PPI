import requests


def main():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/22/municipios"

    response = requests.get(url).json()

    print("Cidades do Estado do %s:" % response[0]["microrregiao"]["mesorregiao"]["UF"]["nome"])
    for cidade in response:
        print("\n%s" % cidade["nome"])


if __name__ == '__main__':
    main()
