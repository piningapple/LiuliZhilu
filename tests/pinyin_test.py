import pytest
from pinyin import getPinyin, getSegmentation, getSegAndPinText, getSegmentationWithPinyin

from fastapi.testclient import TestClient
from server import app
import pytest

client = TestClient(app)


def test_get_pinyin():
    assert getPinyin('他在吗') == 'tāzàima'
     
def test_get_segmentation():
    seg = getSegmentation('今天下午小王给我打电话').split(" ")
    
    assert len(seg) == 5
    assert seg == ['今天下午', '小王', '给', '我', '打电话']
    

def test_getSegmentationWithPinyin():
    sents = getSegmentationWithPinyin('我找娜娜，他在吗？')
    
    chrs = sents[0].split(" ")
    pins = sents[1].split(" ")
    
    assert len(chrs) == len(pins)
    assert chrs[1] == '找'
    assert pins[1] ==  'zhǎo' 
    
def test_getSegAndPinText():
    sents = getSegAndPinText('哈喽，请进！我找娜娜，他在吗？他现在不在，但是马上就回来，请等一会儿！')
    
    assert 'chrs' in sents.keys()
    assert 'pinyin' in sents.keys()
    
    assert len(sents['chrs']) == len(sents['pinyin']) 
    assert len(sents['chrs']) == 3
    
    
    
def test_seg_pin_api():
        
    text = {'text': '哈喽，请进！我找娜娜，他在吗？他现在不在，但是马上就回来，请等一会儿！'}
    response = client.post("/api/pinyin/", json=text)
    assert response.status_code == 200
    
    sents = response.json()
    
    assert sents != ""
    assert 'chrs' in sents.keys()
    assert 'pinyin' in sents.keys()
    
    assert len(sents['chrs']) > 0
    assert len(sents['pinyin']) > 0
    assert len(sents['chrs']) == len(sents['pinyin'])

    
    
