import json
# stddata={
#     "name":"Jaffer",
#     "age":23,
#     "city":"Riyadh",
#     "occupation":"Software Engineer"
# }

# python to json conversion
# json_data1=json.dumps(stddata)
# print(json_data1)
# print(type(json_data1))

# json to python conversion
stddata2='{"name": "Usaid", "age": "25", "city": "Tehran", "occupation": "Data Scientist"}'
json_data2=json.loads(stddata2)
print(json_data2)
print(type(json_data2)) 
