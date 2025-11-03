import re

def total_words_html():
    path = "html_dabkrs_bruks/dabkrs.html"
    pattern = r"\[\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\]"

    total = 0
    skipped = 0

    chars_set = []

    with open(path, 'r', encoding='utf-8') as file:
        for i in range(3665907):
            try:
                line = file.readline()

                #if i < 8515:
                if i<8907:
                    continue

                processed_line = line.strip()
                if re.match(pattern, processed_line):
                    total += 1
                    chars_set.append(processed_line)

            except Exception as e:
                print(f'skipped {i} line | {e}')
                skipped += 1
                continue

            if i % 500000 == 0:
                print('line', i, 'passed \t|\t found:', total, ' \t|\t skipped:', skipped)

    print('-------------------------')
    print(f'total elements: {total}')

    for i in range(5):
        print(chars_set[i])

def get_parsed_html():
    path = "html_dabkrs_bruks/dabkrs.html"
    pattern = r"\[\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\]"

    total = 0
    skipped = 0

    chars_set = []

    with open(path, 'r', encoding='utf-8') as file:
        for i in range(3665907):
            try:
                line = file.readline()

                if i<8906:
                    continue

                processed_line = line.strip()
                if re.match(pattern, processed_line):
                    total += 1
                    chars_set.append(processed_line)

            except Exception as e:
                print(f'skipped {i} line | {e}')
                skipped += 1
                continue

            if i % 500000 == 0:
                print('line', i, 'passed \t|\t found:', total, ' \t|\t skipped:', skipped)

    print('-------------------------')
    print(f'total elements: {total}')

    for i in range(len(chars_set)):
        cs = chars_set[i].replace("['","")
        cs = cs.replace("'],","")
        cs = cs.split("','")
        chars_set[i]=cs

        defs = re.split(r'(?=\n?\d+\))', chars_set[i][2])

        result = []
        for defin in defs:
            if defin.strip():
                lines = [line.strip() for line in defin.split('\\n') if line.strip()]
                if lines:
                    result.append(lines)

        chars_set[i][2] = result

    #print(chars_set[31])


    return chars_set


