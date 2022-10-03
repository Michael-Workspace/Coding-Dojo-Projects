# 1. Update Values in Dictionaries and Lists
print("Answer 1:")
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
print(x)
print(students)
print(sports_directory)
print(z)

# 1-1. Change the value 10 in x to 15. Once you're done, x should no be [[5,2,3],[15,8,9]]
print("Answer 1-1:")
x[1][0]=15
print(x)

# 1-2. Change the last_name of the first student from 'Jordan' to 'Bryant'
print("Answer 1-2:")
students[0]['last_name']='Bryant'
print(students[0])

# 1-3. In the sports_directory, change 'Messi' to 'Andres'
print("Answer 1-3:")
sports_directory['soccer'][0]='Andres'
print(sports_directory['soccer'])

# 1-4. Change the value 20 in z to 30
print("Answer 1-4:")
z[0]['y']=30
print(z)

# 2. Iterate Through a List of Dictionaries
print('------------------------------------')
print('Answer 2:')
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(list):
    for student in range(0, len(list)):
        output = ""
        for key,value in list[student].items():
            output += f"{key} - {value},"
        print(output)

iterateDictionary(students)

# 3. Get Values From a List of Dictionaries
print('------------------------------------')
print('Answer 3:')

def iterateDictionary2(key_name,list):
    for student in range(0,len(list)):
        for key,value in list[student].items():
            if key == key_name:
                print(value)

print('First Name:')
iterateDictionary2('first_name',students)
print('Last Name:')
iterateDictionary2('last_name',students)

# 4. Iterate Through a Dictionary with List Values
print('------------------------------------')
print('Answer 4:')
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key,val in dict.items():
        print(f"{len(val)} {key.upper()}")
        for i in range(0,len(val)):
            print(val[i])

printInfo(dojo)