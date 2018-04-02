import json

minsk_subway_station = """{
"city":"Minsk",
"number_of_lines":2,
"lines":[
    {
        "number":1,
        "colour":"blue"
    },
    {
        "number":2,
        "colour":"red"
    }
]
}"""

parsed_string = json.loads(minsk_subway_station)
print(parsed_string["city"])
