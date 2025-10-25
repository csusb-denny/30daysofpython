empty_tuple = () #syntax
empty_tuple = tuple() #

#syntax 
tpl = ('item1', 'item2', 'item3')
#yntax
len(tpl) #gives length

#note accessing tuples is similar to list in terms of indexing

fruits = ('apple', 'banana', 'cherry')
first_fruit = fruits[0]  # 'apple'
last_fruit = fruits[-1]  # 'cherry'
second_fruit = fruits[1]  # 'banana'
#last_index 
last_index = len(fruits) - 1
last_fruit = fruits[last_index]  # 'cherry'


#item exists
'item2' in tpl #returns true

print('apple' in fruits)  # True
print('orange' in fruits)  # False


#joining two tuples
tpl1 =  ('a', 'b', 'c')
tpl2 =  (1, 2, 3)
combined_tpl = tpl1 + tpl2  # ('a', 'b', 'c', 1, 2, 3)