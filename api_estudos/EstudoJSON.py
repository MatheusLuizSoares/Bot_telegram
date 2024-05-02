# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:13:33 2024

@author: mathe
"""

#JSON

import json

json_string='{"first_name": "Guido", "last_name":"Rossum"}'
json_dict=json.loads(json_string)


d={"first_name":  "Guido", 
    "last_name":"Rossum",
    "titles":['BDFC', 'Developer'],
}
d_json=json.dumps(d)