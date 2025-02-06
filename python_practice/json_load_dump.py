import json

# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)


# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# y = json.dumps(x)

# print(x)
# print(y)

print(json.dumps({"name": "John", "age": 30}))  #dict to object
print(json.dumps(["apple", "bananas"])) # list to array
print(json.dumps(("apple", "bananas"))) # tuple to array
print(json.dumps("hello")) # string to string
print(json.dumps(42)) # int to number
print(json.dumps(31.76)) # float to number
print(json.dumps(True)) #True to true
print(json.dumps(False)) #False to false
print(json.dumps(None)) # None to null