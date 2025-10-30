import requests
from bs4 import BeautifulSoup
from database_dict import get_translation_with_examples

def get_translate_from_site(char):
    url = f"https://bkrs.info/slovo.php?ch={char}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        first_tr = soup.find(class_="m2")
        
        if first_tr:
            text = first_tr.get_text(strip=True)  
            return text
        else:
            raise Exception("Не найден на странице")
    else:
        raise Exception(f"Ошибка запроса: {response.status_code}")

def get_translate_from_db(char):
    translation = get_translation_with_examples(char)

    # print(translation['character'])
    # print(translation['pinyin'])
    # for key in translation['definitions']:
    #     print(key)
    #     for ex in translation['definitions'][key]:
    #         print(ex)

    
    

get_translate_from_db('我')