# Data Structures -  Why ? How ?
# List

environments = ["dev","prod","stg","test"]

print(environments[0])

print(len(environments)) # Length of the string (total-1) # 4 (0,1,2,3)

environments.append("bastion") # Append item to list

print(environments) # Bastion server added into list

#print(dir(environments))

print(environments.insert.__doc__) # Document of insert 


# Disctionary

device_info = {
    "NAME" : "Apple Macbook Pro",
    "RAM" : "16GB",
    "CPU" : 8,
    "Is New" : False
}


print(device_info.get("NAME")) #Prints the value of NAME : Apple Macbook Pro

device_info.update({"ENVIRONMENTS":environments })

print(device_info) # {'NAME': 'Apple Macbook Pro', 'RAM': '16GB', 'CPU': 8, 'Is New': False, 'ENVIRONMENTS': ['dev', 'prod', 'stg', 'test', 'bastion']}

### Sets

#device_ids = {1}
#print(type(device_ids))  # <class 'dict'> If nothing in the  {} , If put {1} <class 'set'>

# device_ids = {} # Dictionary
# device_ids = {1} # Sets


device_ids = {1,2,3,4,4,4,5,6,7,8,9,9,9,10} # Total 14

print(len(device_ids)) # Print 10 as sets does not alllow duplicate values

print(device_ids) #  Removes Duplicate - {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

new_device_ids = {11,12,13}

print(device_ids.union(new_device_ids)) # Prints {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

new_inter_device_ids = {1,2,11,12,13}

print(device_ids.intersection(new_inter_device_ids)) # Prints {1, 2}

### Tuples - Things cant be changed stors in Tuples

days_of_week = ("Sunday","Monday")

#### Array
