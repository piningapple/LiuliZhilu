import pytest
from database_dict import get_translation_with_examples


def test_translate_pinyin():
    tr = get_translation_with_examples('中国')
    assert tr['pinyin'] == 'zhōngguó'

def test_translate_definition():
    tr = get_translation_with_examples('中国')
    
    assert 'definitions' in tr
    assert len(tr['definitions']) > 0
    
    keys = list(tr['definitions'].keys())
    assert 'Китай' in keys[0]

def test_translate_examples():
    tr = get_translation_with_examples('中国')
    
    assert 'definitions' in tr
    definitions = tr['definitions']
    
    keys = list(definitions.keys())
    examples = definitions[keys[0]]
    
    assert len(examples) > 0
    
    assert '中国' in examples[0] 
    
    
