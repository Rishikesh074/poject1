# Multiplication

# num = int(input("Enter your number: "))
# i =1
# mul =1
# while i<=10:
   
#     mul =num*i
#     print(num,"*",i," =",mul)
#     i+=1

# Sum of a n numbers

# num = int(input("Enter your number: "))
# i=1
# sum=0
# while i<=num:
#     sum +=i
#     i+=1
# print(" Total Sum is : ",sum)
    
# Break and continue in while loop 
# variable =10, when reached by 3 break
# a=10
# i=0
# while i<=a:
    
#     if i==3:
#         break
   
#     print(i)
#     i+=1

# Continue

# a=10
# i=0
# while i<=a:
#     i+=1
#     if i==3:
#          continue
   
#     print(i)


# While else

# a=10
# i=1
# while i<a:
#     print(i)
#     i+=1
# else:
#     print("Finished writing")


# largest of an array

# arr= [1,2,3,4,5,6,7]
# for i in range(0,len(arr)):
#     if arr[i]> arr[i+1]:
#         max = arr[i]
#     else:
#         max=arr[i+1]
# print(max)


# largest of numbers

# arr= [1,2,3,4,5,6,7]
# max=arr[0]
# for i in range(0,len(arr)):
#     if arr[i]> max:
#         max = arr[i]
# print(str(max))



# format 
# a = "my name is {}"
# print(a.format(b))

# 2nd example of format

# a= "My name is {0}.... My age is {1}..... My height is {2}...."
# b="Rishi"
# c="23"
# d="170"
# print(a.format(b,c,d))


# 3 rd type

# a = "My name is {b}.... My age is {c}..... My height is {d}...."
# print(a.format(b="Rishi",c=23, d= 170))


# example
# a= 11000
# b= 4600
# c= 2700
# print(a+b+c)


# Format of strings, integers & Float

# Int = 78
# Float = 44.34
# String = "Hello"
# print("The value is %d....the value is %f...the value is %s"%(Int,Float,String))

# Answer correct removing vowels from string
# def rem_vowel(string):
#     vowels=['a','e','i','o','u']
#     result=[letter for letter in string if letter.lower() not in vowels]
#     result= ''. join(result)
#     print(result)
# string=" animals and birds"
# rem_vowel(string)
# string="love python lol"
# rem_vowel(string)