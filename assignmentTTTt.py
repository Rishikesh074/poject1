# 1. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# 2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# 3. Write a Python program to remove duplicates from a list.
# 4. Write a Python program to get the Fibonacci series between 0 to 50
# 5. Write a Python program to calculate a dog's age in dog's years. Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output: Input a dog's age in human years: 15 The dog's age in dog's years is 73
# 6. Write a Python program to construct the following pattern, using a nested loop number.
# Expected Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 7. Find the largest among three numbers.
# 8. Write a program to read a word from console and display the correct spelling if there is a mistake.
# 9. Write a Python program to read first n lines of a file.


#  1
a=[1,2,5,8,10,23,21]
print(max(a))
print(min(a))

# # 2
# def count(a):
#     cnt=0
#     for i in a:
#         if len(a)>=2



# rows=int(input("Enter the rows :"))
# for i in range(1,rows+1):
#     for j in range (1,i+1):
#         print(i , end="")
#     print()


# rows=int(input("Enter the rows :"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(i , end=" ")
#     print()


# rows=int(input("Enter the rows :"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j , end=" ")
#     print()

# rows=int(input("Enter the rows :"))
# for i in range(1,rows+1): 
#     for j in range(rows):
#         print(i , end=" ")
#     rows=rows-1
#     print()

# rows=int(input("Enter the rows :"))
# for i in range(1,rows+1): 
#     for j in range(rows):
#         print( 5 , end=" ")
#     rows=rows-1  
#     print()


# rows=int(input("Enter the rows :"))
# for i in range(rows+1): 
#     for j in range(rows+1):
#         print( j , end=" ")
#     rows=rows-1
#     print()


# def isPalin(s):
#     return s==s[::-1]
# s="malayalm"
# ans=isPalin(s)
# if ans:
#     print("yes")
# else:
#     print("NO")

# def fact(n):
#     if n<0:
#         return 0
#     elif n==0 or n==1:
#         return 1
#     else:
#         fact=1
#         while n>1:
#             fact*=n
#             n-=1
#             return fact
# num=5
# print("factorial of num ",num, " is :", fact(num))
