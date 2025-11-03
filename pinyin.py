import jieba
import dragonmapper
from dragonmapper import hanzi
import re


def getSegmentation(sentence):    
    seg_list = jieba.cut(sentence, HMM=True) # с использованием скрытой марковской модели для анализа любых нестандартных фраз и текстов.
    #seg_list = jieba.cut(sentence, cut_all = False) # наиболее вероятная сегментация
    #seg_list = jieba.cut(sentence, cut_all = True) # все варианты сегментации
    
    return " ".join(seg_list)



def getPinyin(sentence):
    pin = dragonmapper.hanzi.to_pinyin(sentence)
    
    return pin


def getSegmentationWithPinyin(sentence):
    seg = getSegmentation(sentence)
    pin = getPinyin(seg)

    return [seg, pin]

def getSegAndPinText(text):
    strs =  filter(lambda el: el!='' ,re.split(r'(?<=[！？。])', re.sub(r'\n','', text)))
    sents = {
        'chrs': [],   
        'pinyin': []  
    }

    for sent in strs:
        seg = getSegmentationWithPinyin(sent)
        sents['chrs'].append(seg[0])
        sents['pinyin'].append(seg[1])

    return sents

#print(getSegAndPinText('哈喽，请进！我找娜娜，他在吗？ 他现在不在，但是马上就回来，请等一会儿！'))
