# Q.1 What will be the output of the following code?
init_tuple = ()
print(init_tuple.__len__())
# A.none
# B. 1
# C. 0
# D. Exception

# Q.2 What will be the output of the following code?
init_tuple_a = 'a' , 'b'
init_tuple_b = ('a' , 'b')
print(init_tuple_a == init_tuple_b)
# A. 0
# B. 1
# C. True
# D. False

# Q.3 What will be the output of the following code?
init_tuple_a = '1' , '2'
init_tuple_b = ('3' , '4')
print(init_tuple_a + init_tuple_b)
# A. (1,2,3,4)
# B. ('1', '2', '3', '4')
# C. ['1', '2', '3', '4']
# D. none

# Q.4 What will be the output of the following code?
l = [1,2,3]
init_tuple =  ('Python',) * (l.__len__() - l[::1][0])
print(init_tuple)
# a. ()
# b. ('Python')
# c. ('Python', 'Python')
# d. runtime error

# Q.5 What will be the output of the following code?
init_tuple = ('Python') * 3
print(type(init_tuple))
# a. <class 'tuple'>
# b. <class 'str'>
# c. <class 'list'>
# d. <class 'function'>

# Q.6 What will be the output of the following code?
init_tuple = (1,) * 3
init_tuple [0] = 2
print(init_tuple)
# a. (1, 1, 1)
# b. (2, 1, 1)
# c. (2, 2, 2)
# d. TypeError: 'tuple' object does not support item assignment

# Q.7 What will be the output of the following code?
init_tuple = ((1,2),)*7
print(len(init_tuple[3:8]))
# a. exception
# b. 5
# c. 4
# d. none

