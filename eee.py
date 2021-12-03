# my_list =[10,12,16,19,25,30]
# b=list(filter(lambda x: x%5==0, my_list))
# print(b)



# my_list =[10,12,16,19,25,30]
# b=list(map(lambda x: x*2, my_list))
# print(b)



# reduce()

# from functools import reduce
# li =[1,2,3,4,5,6,7,8,9,10]
# a=reduce(lambda x,y: x+y,li)
# print(a)

# from functools import reduce
# a=reduce(lambda x,y: x+y,range(1,10))
# print(a)

# print even numbers
a=list(filter(lambda x: x%2==0,range(1,10)))
print(a)