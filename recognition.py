import easyocr
import re

reader = easyocr.Reader(['ch_sim'], gpu=False) # this needs to run only once to load the model into memory
results = reader.readtext('recognize_data/text.jpg', detail = 0)

results = "".join(results)
#results = filter(lambda el: el!='' ,re.split(r'(?<=[！？。])', result))

print(results)
