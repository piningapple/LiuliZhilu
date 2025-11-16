'''Модуль для распознавания текста с изображения'''
import re
import easyocr

def get_image_recognition():
    '''функция получения текст с изображения'''
    text = {
        'text': []
    }
    reader = easyocr.Reader(['ch_sim'], gpu=False) # this needs to run only once to load the model into memory
    results = reader.readtext('recognize_data/text.jpg', detail = 0)

    result = "".join(results)
    results = filter(lambda el: el!='' ,re.split(r'(?<=[！？。])', result))
    text['text'] = "".join(results)

    #print(result)

    return text

#print(get_image_recognition())
