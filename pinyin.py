"""модуль для работы с сегментацией и пиньинем"""
import re
import jieba
import jieba.posseg as pseg
import dragonmapper
# pylint: disable=unused-import
from dragonmapper import hanzi
# pylint: enable=unused-import

def get_segmentation(sentence):
    """сегментация предложения"""
    seg_list = jieba.cut(sentence, HMM=True) # с использованием скрытой марковской модели
                                             # для анализа любых нестандартных фраз и текстов.
    #seg_list = jieba.cut(sentence, cut_all = False) # наиболее вероятная сегментация
    #seg_list = jieba.cut(sentence, cut_all = True) # все варианты сегментации

    return " ".join(seg_list)

def get_all_segmentation(sentence):
    """сегментация предложения"""
    #seg_list = jieba.cut(sentence, HMM=True) # с использованием скрытой марковской модели
                                             # для анализа любых нестандартных фраз и текстов.
    #seg_list = jieba.cut(sentence, cut_all = False) # наиболее вероятная сегментация
    seg_list = jieba.cut(sentence, cut_all = True) # все варианты сегментации

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

def get_seg_text(text):
    """сегменатция текста"""
    strs =  filter(lambda el: el!='' ,re.split(r'[！？。]', re.sub(r'\n','', text)))  
    
    chars = []

    for sent in strs:
        seg = get_segmentation(sent)
        seg = filter(lambda el: (el!='，'),seg.split())
        chars.extend(seg)
    

    return chars

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

def get_speech_parts(text):
    words = pseg.cut(text)
    for w in words:
        print(w.word, w.flag)


print(get_speech_parts("地"))
segmets = get_all_segmentation('我的熊猫').split()
print(segmets)
for seg in segmets:
    print(get_speech_parts(seg))
