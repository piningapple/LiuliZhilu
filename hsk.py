import re
import os.path
import pandas as pd
from pinyin import get_seg_text
from database_dict import get_word_level

def read_lines_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        pattern = r'^(\d+)?\s*(\S+)\s+(\[.+\])\s+(.+)$'
        replacements = {']/[': ', ','[': '',']': '','|': ', ',' и ': ', ','//': ' ','·': ''}

        lines = file.readlines() 
        lines = lines[1:]            
    
        for i in range(0,len(lines)):
            match = re.match(pattern, lines[i])
            if not match:
                print(f"Строка не соответствует формату: {lines[i]}")
                return None
            
            char = re.sub(r'[（(].*?[）)]', '', match.group(2))
            pinyin = match.group(3)
            for old, new in replacements.items():
                pinyin = pinyin.replace(old, new)
            translation = match.group(4)
            
            #if ';' in translation:
            #   translation = translation.replace('; ',";").split(';')
        
            lines[i] =[char,pinyin, translation]     

    return lines

def text_to_csv():
    for i in range(1,7):
        if not  os.path.exists(f'./data/hsk/csv/hsk{i}_words.csv'):
            lines = read_lines_to_list(f'./data/hsk/txt/hsk{i}_words.txt')
            print(lines[0])
            lines = pd.DataFrame(lines, columns=['character','pinyin','definitions'])
            lines.to_csv(f'./data/hsk/csv/hsk{i}_words.csv', index=False)
            print(f'{i}: ok')

def analyze_text(text):
    chars = get_seg_text(text)
    print(chars)
    levels = []

    for char in chars:
        levels.append([char,get_word_level(char)])
        
    print(levels)

analyze_text('我喜欢西兰花')

