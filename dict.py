import re
import ast
from dsl_dict_analyser.analyser import analyser
from dsl_dict_analyser.models.dictionary import Dictionary

def read(file_path: str) -> Dictionary:
    with open(file_path,"r",encoding='utf-16') as file:
        lines = []
        for line in file.readlines():
            lines.append(line)
    return analyser(lines)

def read_dict():
    path = "dsl_dabkrs_250920/dabkrs_1.dsl"

    dsl_dict = read(path)

    print(dsl_dict.name)
    print(len(dsl_dict.cards))

    for i in range(50):
        print('----------', (i+1), '----------')
        card = dsl_dict.cards[i]
        print('word:', card.word)
        print('definitions:', card.definitions)
        print()

# 3.434.227
def total_words_dicts():
    paths = [
        "dsl_dabkrs_250920/dabkrs_1.dsl",
        "dsl_dabkrs_250920/dabkrs_2.dsl",
        "dsl_dabkrs_250920/dabkrs_3.dsl"
    ]

    total = 0

    for path in paths:
        dsl_dict = read(path)
        print(f'{path}: \t {len(dsl_dict.cards)} elements')
        total += len(dsl_dict.cards)

    print('-------------------------')
    print(f'total elements: {total}')

# substr:               3.653.689   # if(processed_line[:2] == "['"):
# regex:                3.398.071   # r"\[\s*'([^']*)'\s*,\s*'([^']*)'\s*,\s*'([^']*)'\s*\]"
# regex 2:              3.399.569   # r"\[\s*'([^']*)'\s*,\s*'([^']*)'\s*,\s*'([^']*)'\s*\]*"
# regex 3:              3.399.620   # r"\[\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\]"
# regex 3 with skip:    3.399.298   # Это правильно!
def total_words_html():
    path = "html_dabkrs_bruks/dabkrs.html"
    pattern = r"\[\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\]"

    total = 0
    skipped = 0

    chars_set = list()

    with open(path, 'r', encoding='utf-8') as file:
        for i in range(3665907):
            try:
                line = file.readline()
                
                #if(i < 8515):
                if (i<8907):
                    continue

                processed_line = line.strip()
                if(re.match(pattern, processed_line)):
                    total += 1
                    chars_set.append(processed_line)

            except Exception as e:
                print(f'skipped {i} line | {e}')
                skipped += 1
                continue

            if(i % 500000 == 0):
                print('line', i, 'passed \t|\t found:', total, ' \t|\t skipped:', skipped)
    
    print('-------------------------')
    print(f'total elements: {total}')

    for i in range(5):
        print(chars_set[i])

# diff: 37524
def html_and_dict_diff():
    # set from html
    path_html = "html_dabkrs_bruks/dabkrs_dabruks.html"
    pattern = r"\[\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\]"

    chars_set = set()

    print("Читаю html")
    with open(path_html, 'r', encoding='utf-8') as file:
        for i in range(3665907):
            line = file.readline()
                
            if(i < 8515):
                continue

            processed_line = line.strip()
            if(re.match(pattern, processed_line)):
                a = ast.literal_eval(processed_line)[0]
                chars_set.append(a[0])
    print(f"Считал из html: {len(chars_set)} иероглифов")



    # Dicts
    
    print("Читаю словари")
    dict_paths = [
        "dsl_dabkrs_250920/dabkrs_1.dsl",
        "dsl_dabkrs_250920/dabkrs_2.dsl",
        "dsl_dabkrs_250920/dabkrs_3.dsl"
    ]

    diff = 0

    for path in dict_paths:
        dsl_dict = read(path)
        print(f"Считал словарь {path}")

        for card in dsl_dict.cards:
            if(card.word not in chars_set):
                print(f"Нету слова {card.word} | {card.definitions}")
                diff += 1
    
    print("---------------------")
    print(f"Итого не найдено: {diff}")

# diff: 2781
def dict_and_html_diff():
    # Set from dicts
    chars_set = set()

    print("Читаю словари")
    dict_paths = [
        "dsl_dabkrs_250920/dabkrs_1.dsl",
        "dsl_dabkrs_250920/dabkrs_2.dsl",
        "dsl_dabkrs_250920/dabkrs_3.dsl"
    ]

    for path in dict_paths:
        dsl_dict = read(path)
        print(f"Считал словарь {path}")

        for card in dsl_dict.cards:
            chars_set.add(card.word)

    # Reading html
    path_html = "html_dabkrs_bruks/dabkrs_dabruks.html"
    pattern = r"\[\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\]"

    diff = 0

    print("Читаю html")
    with open(path_html, 'r', encoding='utf-8') as file:
        for i in range(3665907):
            line = file.readline()
                
            if(i < 8515):
                continue

            processed_line = line.strip()
            if(re.match(pattern, processed_line)):
                a = ast.literal_eval(processed_line)[0]
                if(a[0] not in chars_set):
                    print(f"Нету слова {a[0]} | {a}")
                    diff += 1

    print("---------------------")
    print(f"Итого не найдено: {diff}")


def normalize_dict():
# set from html
    path_html = "html_dabkrs_bruks/dabkrs_dabruks.html"
    pattern = r"\[\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\]"

    chars_set_html = set()

    print("Читаю html")
    with open(path_html, 'r', encoding='utf-8') as file:
        for i in range(3665907):
            line = file.readline()
                
            if(i < 8515):
                continue

            processed_line = line.strip()
            if(re.match(pattern, processed_line)):
                a = ast.literal_eval(processed_line)[0]
                chars_set_html.add(a[0])
    print(f"Считал из html: {len(chars_set_html)} иероглифов")

    # Dicts
    
    # Set from dicts
    chars_set_dicts = set()

    print("Читаю словари")
    dict_paths = [
        "dsl_dabkrs_250920/dabkrs_1.dsl",
        "dsl_dabkrs_250920/dabkrs_2.dsl",
        "dsl_dabkrs_250920/dabkrs_3.dsl"
    ]

    for path in dict_paths:
        dsl_dict = read(path)
        print(f"Считал словарь {path}")

        for card in dsl_dict.cards:
            chars_set_dicts.add(card.word)

    char_norm_dict = set()

    for word in chars_set_html:
        if word in chars_set_dicts:
            char_norm_dict.add(word)
    
    print("Слов", len(char_norm_dict))

    char_norm_dict_definitions = list()
    
    with open(path_html, 'r', encoding='utf-8') as file:
        for i in range(3665907):
            line = file.readline()
                
            if(i < 8515):
                continue

            processed_line = line.strip()
            if(re.match(pattern, processed_line)):
                a = ast.literal_eval(processed_line)[0]
                if(a[0] in char_norm_dict):
                    char_norm_dict_definitions.append(a)

    print("words", len(char_norm_dict_definitions))
    for i in range(5):
        print(char_norm_dict_definitions[i])

                    
def getParsedHtml():
    path = "html_dabkrs_bruks/dabkrs.html"
    pattern = r"\[\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\]"

    total = 0
    skipped = 0

    chars_set = list()

    with open(path, 'r', encoding='utf-8') as file:
        for i in range(3665907):
            try:
                line = file.readline()

                if (i<8906):
                    continue

                processed_line = line.strip()
                if(re.match(pattern, processed_line)):
                    total += 1
                    chars_set.append(processed_line)

            except Exception as e:
                print(f'skipped {i} line | {e}')
                skipped += 1
                continue

            if(i % 500000 == 0):
                print('line', i, 'passed \t|\t found:', total, ' \t|\t skipped:', skipped)
    
    print('-------------------------')
    print(f'total elements: {total}')

    for i in range(len(chars_set)):
        cs = chars_set[i].replace("['","") 
        cs = cs.replace("'],","")
        cs = cs.split("','")
        chars_set[i]=cs
        
        defs = re.split(r'(?=\n?\d+\))', chars_set[i][2])

        result = list()
        for defin in defs:
            if defin.strip():
                lines = [line.strip() for line in defin.split('\\n') if line.strip()]
                if lines:
                    result.append(lines)

        chars_set[i][2] = result

    #print(chars_set[31])
    
    
    return chars_set


#getParsedHtml()
# read_dict()
# total_words_dicts()
#total_words_html()
# html_and_dict_diff()
#dict_and_html_diff()
#normalize_dict()

