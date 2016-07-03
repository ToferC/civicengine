import json

import json
from pprint import pprint

with open('flare.py') as data_file:    
    data = json.load(data_file)

pprint(data['children'][0]['children'][0]['children'][0]['size'])
