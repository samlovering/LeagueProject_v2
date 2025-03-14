'''
Oracle Elixir Scraper
Sam Lovering
This scrapes data from the oracle elixir google drive for matches.
'''
import requests


def downloadFromGoogleDrive():
    file_id = '1v6LRphp2kYciU4SXp0PCjEMuev1bDejc'
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    response = requests.get(url)
    with open('scraper/match_scraper/match_data.csv', 'wb') as f:
        f.write(response.content)
    file_path ='scraper/match_scraper/match_data.csv'
    print("Oracles Elixer Data downloaded located at:{}".format(file_path))
    return file_path

if __name__ == "__main__":
    downloadFromGoogleDrive()