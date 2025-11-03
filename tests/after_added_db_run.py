from server import app
from fastapi.testclient import TestClient
from database_dict import get_translation_with_examples

client = TestClient(app)

def test_translate_pinyin():
    """ тестирование получения пиньина при переводе """
    tr = get_translation_with_examples('中国')
    assert tr['pinyin'] == 'zhōngguó'

def test_translate_definition():
    """ тестирование получения определения при переводе """

    tr = get_translation_with_examples('中国')

    assert 'definitions' in tr
    assert len(tr['definitions']) > 0

    keys = list(tr['definitions'].keys())
    assert 'Китай' in keys[0]

def test_translate_examples():
    """ тестирование получения примеров при переводе """

    tr = get_translation_with_examples('中国')

    assert 'definitions' in tr
    definitions = tr['definitions']

    keys = list(definitions.keys())
    examples = definitions[keys[0]]

    assert len(examples) > 0
    assert '中国' in examples[0]


def test_translate_api():
    """ тестирование api получения перевода """

    char = '中国'
    response = client.get("/api/translate/?ch="+char)
    assert response.status_code == 200

    data = response.json()

    assert data != ""
    assert 'character' in data
    assert 'pinyin' in data
    assert 'definitions' in data
    assert len(data['definitions']) > 0

    keys = list(data['definitions'].keys())
    assert len(data['definitions'][keys[0]]) > 0

