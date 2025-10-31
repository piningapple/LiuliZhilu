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

print(getSegmentationWithPinyin("是不是"))