import requests


def main():
    response = requests.get('http://youtube.com')
    print(response.status_code)
    print(response.headers['content-type'])
    print(response.text)
    print(len(response.text))

if __name__ == '__main__':
    main()
