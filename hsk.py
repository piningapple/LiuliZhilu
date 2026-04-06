import re
import csv
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

def str_split(filename):

    hsk = {
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: []
            }
    
    word_in_count = 0
    
    for i in range(1,7):
        with open(f'{filename}hsk{i}_raw.txt', 'r', encoding='utf-8') as file:
            word_count, raw_words = file.readlines()  
            raw_words = f' {raw_words.split(' ',1)[1]}'
            

            words = []

            for j in range(word_in_count+2,word_in_count+int(word_count)+1):
                word, raw_words = raw_words.split(str(j), 1)
                words.append(word[1:])

            words.append(raw_words[1:])


            print(f"hsk {i}: {len(words)}/{word_count}")
            word_in_count += len(words)
        

            for w in words:
                parts = w.split()
                parts[1] = re.sub(r'\d+', '', parts[1])

                if '（' in parts[0]:
                    number = re.findall(r'（([^）]+)）', parts[0])
                    fu = re.findall(r'（([^）]+)）', parts[3])
                    hsk[i].append(f'{parts[0][0]} {parts[1]} {parts[2]} {parts[3].split('、')[0]}')
                    for k in range (0,len(number)):
                        if number[k]!="7-9": 
                            hsk[int(number[k])].append(f"{number[k]} {parts[1]} {parts[2]} {fu[k]}")
                else:
                    hsk[i].append(f"{parts[0]} {parts[1]} {parts[2]} {parts[3] if len(parts) > 3 else ''}")

    
    
    for i in range(1,7):  
        uncleaned_hsk = hsk[i]
        hsk[i] = list(filter(None, uncleaned_hsk))
        for w in hsk[i]:
            hsk[i] = w.split()                 

        with open(f'./data/hsk/hsk{i}_w.csv', "w", newline="",encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["№","Иероглиф", "Пиньинь", "Часть речи"])
            writer.writerows(hsk[i])



        




                

str_split('./data/hsk/')

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
    levels = []

    for char in chars:
        levels.append([char,get_word_level(char)])
        

    return levels

#analyze_text('我哈喽，请进！我找娜娜，他在吗？他现在不在，但是马上就回来，请等一会儿！谢谢！不客气，哦，已经回来了！志刚你来得真巧！今天下午小王给我打电话，说他明天可以带我们去参观东方明珠。')

