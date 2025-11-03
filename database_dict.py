""" модуль для работы с базой данных """
import uuid
from peewee import SqliteDatabase, Model, TextField, ForeignKeyField
from dict import get_parsed_html

# соединение с базой данных
conn = SqliteDatabase('Dict_Sqlite.sqlite')

# КОД МОДЕЛЕЙ
class BaseModel(Model):
    """Базовая модель от которой будут наследоваться остальные"""

    class Meta:
        database = conn

class Word(BaseModel):
    """Модель слов"""

    word_id = TextField(column_name='WordId')
    character = TextField(column_name='Character', null=False)
    pinyin =  TextField(column_name='Pinin', null=True)

    class Meta:

        table_name = 'Words'

class Definition(BaseModel):
    """Модель определений"""

    definition_id = TextField(column_name='DefinitionId')
    word_id  = ForeignKeyField(Word, backref="definitions", column_name='Word')
    definition =  TextField(column_name='Definition', null=False)


    class Meta:
        table_name = 'Definitions'

class Example(BaseModel):
    """Модель примеров"""

    example_id = TextField(column_name='ExampleId')
    definition_id  = ForeignKeyField(Definition, backref="examples", column_name='Definition')
    example =  TextField(column_name='Example', null=False)


    class Meta:
        table_name = 'Examples'

# cоздаем курсор
cursor = conn.cursor()

# КОД РАБОТЫ С БАЗОЙ ДАННЫХ
def recreate_db():
    """функция для пересоздания базы данных"""

    conn.drop_tables([Word, Definition, Example])

    Word.create_table()
    Definition.create_table()
    Example.create_table()

def add_data():
    """функция для добавление данных"""

    data = get_parsed_html()
    word_count = 0
    words = []
    definitions = []
    examples = []

    for w in data:
        word = {'word_id' : str(uuid.uuid4()), 'character' : w[0], 'pinyin' : w[1]}
        words.append(word)
        #print("save word ", w[0])
        for d in w[2]:
            definition  = { 'definition_id': str(uuid.uuid4()),
                            'word_id' : word.get('word_id'),
                            'definition' : d[0]}
            #print("save definition ", d[0])
            definitions.append(definition)
            for e in range(1,len(d)):
                example = { 'example_id': str(uuid.uuid4()),
                            'definition_id' : definition.get('definition_id'),
                            'example' :d[e]}
                examples.append(example)
                #print("save example ",d[e])

        word_count+=1
        if word_count % 1000 == 0:
            Word.insert_many(words).execute()
            Definition.insert_many(definitions).execute()
            Example.insert_many(examples).execute()

            words = []
            definitions = []
            examples = []

        if word_count % 50000 == 0:
            print("save ", word_count , " words" )


    Word.insert_many(words).execute()
    Definition.insert_many(definitions).execute()
    Example.insert_many(examples).execute()

#recreateDB()
#addData()

def get_translation_with_examples(char):
    """функция для получения из базы данных определения с примерами"""

    query = (Word
         .select(Word)
         .where(Word.character == char))

    translation = {}

    for w in query:
       #print(w.character)
        translation['character'] = w.character
        translation['pinyin'] = w.pinyin
        query2 = (Definition
            .select(Definition)
            .where(Definition.word_id == w.word_id))
        translation['definitions'] = {}
        for d in query2:
            #print(d.definition)
            translation['definitions'][d.definition] = []
            query3 = (Example
                .select(Example)
                .where(d.definition_id == Example.definition_id))
            for e in query3:
                #print(e.example)
                translation['definitions'][d.definition].append(e.example)

    return translation
#    print(translation['character'])
#    print(translation['pinyin'])
#    for key in translation['definitions']:
#        print(key)
#        for ex in translation['definitions'][key]:
#            print(ex)

#get_translation_with_examples('妈')

# закрыть соединение с базой данных
conn.close()
