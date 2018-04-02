# coding=utf-8
import json

minsk_subway_stations = """{
"city":"Minsk",
"number_of_lines":2,
"lines":[
    {
        "id":1,
        "colour":"blue",
        "data":""
    },
    {
        "id":2,
        "colour":"red",
        "data":""
    }
]
}"""

blue_line_json = """{
    "id":1,
    "stations":[
        {
        
            "name":"Уручье",        
            "id":1
        },
        {
            "name":"Борисовский тракт",
            "id":2
        },
        {
            "name":"Восток",
            "id":3
        },
        {
            "name":"Московская",
            "id":4
        }
        
        
    ],
    "intervals":[
        {
            "from":1,
            "to":2,
            "interval":3
        },
        {
            "from":2,
            "to":3,
            "interval":2
        },
        {
            "from":3,
            "to":4,
            "interval":2
        }
    ]
    
}
"""

# load metadata about city subway
parsed_string = json.loads(minsk_subway_stations)
# load data about blue line
blue_line = json.loads(blue_line_json)
parsed_string["lines"][0]["data"] = blue_line
print(parsed_string)
