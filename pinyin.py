"""модуль для работы с сегментацией и пиньинем"""
import re
import jieba
import dragonmapper
from dragonmapper import hanzi

def get_segmentation(sentence):
    """сегментация предложения"""
    seg_list = jieba.cut(sentence, HMM=True) # с использованием скрытой марковской модели
                                             # для анализа любых нестандартных фраз и текстов.
    #seg_list = jieba.cut(sentence, cut_all = False) # наиболее вероятная сегментация
    #seg_list = jieba.cut(sentence, cut_all = True) # все варианты сегментации

    return " ".join(seg_list)

def get_pinyin(sentence):
    """получение пиньина для предложения"""
    pin = dragonmapper.hanzi.to_pinyin(sentence)

    return pin

def get_segmentation_with_pinyin(sentence):
    """сегменатция предложения и добавление пиньина предложения"""
    seg = get_segmentation(sentence)
    pin = get_pinyin(seg)

    return [seg, pin]

def get_seg_and_pin_text(text):
    """сегменатция предложения и добавление пиньина текста"""
    strs =  filter(lambda el: el!='' ,re.split(r'(?<=[！？。])', re.sub(r'\n','', text)))
    sents = {
        'chrs': [],
        'pinyin': []
    }

    for sent in strs:
        seg = get_segmentation_with_pinyin(sent)
        sents['chrs'].append(seg[0])
        sents['pinyin'].append(seg[1])

    return sents

#print(getSegAndPinText('哈喽，请进！我找娜娜，他在吗？ 他现在不在，但是马上就回来，请等一会儿！'))
