# Some basic set operations are covered here for practicing purpose
a = {} # dict but not set
a = {'a', 'b', 'c', 'd', 'mango', 'banana'} # correct set
b = {'a', 'b', 'mango'}


# basic set operations
union = a|b # union
intrs = a&b
compl = a-b
subset = a>b

print(f"union: {union}\nintersection: {intrs}\ncompliment: {compl}\nsubset: {subset}")

# converting a list with repeated values into an unrepeated value list -> using set
list1 = [1,2,4,5,6,7,8,9,2,4,1,44,5,6,6]
# the hard way
unique_list = []
for num in list1:
    if num not in unique_list:
        unique_list.append(num)
print(f"Using the hard way: {unique_list}, type {type(unique_list)}")

# the easy way
unique_list = list(set(list1))  # 'list' is a built-in type, rename the variable to avoid conflict
print(f"Using the easy way: {unique_list}, type {type(unique_list)}")



