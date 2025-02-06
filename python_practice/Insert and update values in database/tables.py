import json

file_read = open("data.json", "r")
info = json.loads(file_read.read())

while True:
    print("The fields are:")
    for data in info:
        print(data)
    field = input("Enter the field you want to add values in:")
    if field in info:
        dict_list = {}
        print(f"Enter values in {field} section")
        for key in info[field]["schema"]:
            while True:
                datatype = info[field]["schema"][key]["datatype"]
                data = input(f"Enter the value of {key} ({datatype}):")
                if info[field]["schema"][key]["datatype"] == "string":
                    if data.isdigit():
                        print(f"{key} can not be numeric")
                        continue
                    elif data == "":
                        print(f"{key} cannot be empty")
                        continue
                    data = str(data)
                    break
                elif info[field]["schema"][key]["datatype"] == "integer":
                    if not data.isdigit():
                        print(f"Enter valid {key}")
                        continue
                    data = int(data)
                    break
                elif info[field]["schema"][key]["datatype"] == "relation":
                    relation = info[field]["schema"][key]["table"]
                    table = info[relation]["data"]
                    if not data.isdigit():
                        print(f"Enter valid {key}")
                        continue
                    data = int(data)
                    if any(value["id"] == data for value in table):
                        print("Your entered data is correct")
                        break
                    else:
                        print("Please enter correct data")
                    continue
                elif info[field]["schema"][key]["datatype"]== "float":
                    if not data.isdigit():
                        print(f"Enter valid {key}")
                        continue
                    data = float(data)
                    break
            dict_list.update({key: data})
        info[field]["data"].append(dict_list)

    elif field not in info and not field.isdigit():
        print("Enter the valid field to enter data")
        continue

    else:
        print("Exit")
        break

with open("data.json", "w") as file_write:
    file_write.write(json.dumps(info, indent=6))
    file_write.close()