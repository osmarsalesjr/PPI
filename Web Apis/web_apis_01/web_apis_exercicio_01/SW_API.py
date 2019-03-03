import requests


def main():
    url = "https://swapi.co/api/films"
    response = requests.get(url).json()

    films = response["results"]

    print("Total de Filmes: %d" % response["count"])
    for film in films:
        print("\nReleased date: %s\nTitle: %s" % (film["release_date"], film["title"]))


if __name__ == '__main__':
    main()
