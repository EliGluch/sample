def half_range(n):
    return map(lambda x: x / 2.0, range(2 * n + 1))


# print(half_range(5))

def intersection(listA, listB):
    return list(set([item for item in listA if item in listB]))


# a = [1,2,3,3]
# b = [1,3,2,2,5]
# print(intersection(a,b))

def char_set(my_string):
    return set([char for char in my_string])


# print(char_set("this is a test"))

def char_count(my_string):
    return {char: my_string.count(char) for char in char_set(my_string)}


# print(char_count("this is a test"))

def equal_dicts(dict1, dict2):
    for key in dict1.keys():
        if not key in dict2.keys() or dict1[key] != dict2[key]:
            return False
    for key in dict2.keys():
        if not key in dict1.keys() or dict1[key] != dict2[key]:
            return False
    return True

d1 = {1:"a", 2:"b" , 3:"c"}
d2 = {2:"b" , 3:"c" , 1:"a"}

print(equal_dicts(d1,d2))