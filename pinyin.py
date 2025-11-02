import jieba
import dragonmapper
from dragonmapper import hanzi


def segmentation(sentence):    
    seg_list = jieba.cut(sentence, HMM=True) # с использованием скрытой марковской модели для анализа любых нестандартных фраз и текстов.
    #seg_list = jieba.cut(sentence, cut_all = False) # наиболее вероятная сегментация
    #seg_list = jieba.cut(sentence, cut_all = True) # все варианты сегментации

    #print("/ ".join(seg_list))

    return " ".join(seg_list)



def getPinyin(sentence):
    pin = dragonmapper.hanzi.to_pinyin(sentence)
    
    return pin


def getSegmentationWithPinyin(sentence):
    seg = segmentation(sentence)
    pin = getPinyin(seg)

    return [seg, pin]

def getSegAndPinText(text):
    sents = {
        'chrs': [],   # Нужно инициализировать списки
        'pinyin': []  # перед использованием append
    }

    for sent in text:
        seg = getSegmentationWithPinyin(sent)
        sents['chrs'].append(seg[0])
        sents['pinyin'].append(seg[1])

    return sents

#print(getSegAndPinText(['哈喽，请进!', '我找娜娜，他在吗?', '说他明天可以带我们去参观东方明珠.']))