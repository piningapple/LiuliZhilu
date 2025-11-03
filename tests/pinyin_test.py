from pinyin import get_pinyin, get_segmentation, get_seg_and_pin_text, get_segmentation_with_pinyin

from fastapi.testclient import TestClient
from server import app
import pytest

client = TestClient(app)


def test_get_pinyin():
    assert get_pinyin('他在吗') == 'tāzàima'
     
def test_get_segmentation():
    seg = get_segmentation('今天下午小王给我打电话').split(" ")
    
    assert len(seg) == 5
    assert seg == ['今天下午', '小王', '给', '我', '打电话']
    

def test_getSegmentationWithPinyin():
    sents = get_segmentation_with_pinyin('我找娜娜，他在吗？')
    
    chrs = sents[0].split(" ")
    pins = sents[1].split(" ")
    
    assert len(chrs) == len(pins)
    assert chrs[1] == '找'
    assert pins[1] ==  'zhǎo' 
    
def test_getSegAndPinText():
    sents = get_seg_and_pin_text('哈喽，请进！我找娜娜，他在吗？他现在不在，但是马上就回来，请等一会儿！')
    
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

    
    
