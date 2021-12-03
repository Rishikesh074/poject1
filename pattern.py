# rows = int(input(" Enter the number of rows :"))
# for i in range(rows+1):
#     for j in range(i):
#         print(j+1,end =" ")
#     print()


# rows = int(input(" Enter the number of rows :"))
# for i in range(1,rows+1):
#     for j in range(rows):
#         print(i,end =" ")
#     rows=rows-1
#     print()


# rows = int(input(" Enter the number of rows :"))
# for i in range(1,rows+1):
#     for j in range(rows):
#         print('5',end =" ")
#     rows=rows-1
#     print()


# rows = int(input(" Enter the number of rows :"))
# in_num=int(input(" Enter the pattern no to be printed :"))
# for i in range(1,rows+1):
#     for j in range(rows):
#         print(in_num,end =" ")
#     rows=rows-1
#     print()

# rows = int(input(" Enter the number of rows :"))
# for i in range(1,rows+1):
#     for j in range (i):
#         print('*',end=" ")
#     print()

# rows = int(input(" Enter the number of rows :"))
# for i in range(1,rows+1):
#     for j in range (i-1):
#         print(end=" ")
#     for k in range(rows+1-i):
#         print("*",end=" ")
#     print()


# rows = int(input(" Enter the number of rows :"))
# for i in range(1,rows+1):
#     for j in range(rows,0,-1):
#         if j>i:
#             print(' ',end =" ")
#         else:
#             print("*",end=" ")
#     print()


# rows =6
# for i in range(1,rows+1):
#     for j in range(rows,0,-1):
#         print(j)

# rows = int(input(" Enter the number of rows :"))
# for i in range(1,rows+1):
#     for j in range(rows,0,-1):
#         if j>i:
#             print(' ',end =" ")
#             print("*",end=" ")
        
        

# rows = 5
# for j in range(rows,0,-1):
#     print(j)

# rows = int(input("Enter the no of rows : "))
# for i in range(0,rows):
#     for j in range(0,rows-1-i):
#         print(end= " ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# rows = int(input("Enter the no of rows : "))
# for i in range(0,rows):
#     for j in range(0,rows-i-1):
#         print(end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# rows = int(input(" Enter the number of rows :"))
# for i in range(0,rows+1):
#     a=rows-i
#     for j in range(a):
#         print(" ",end =" ")
#         a=a-1
#     for j in range(i):
#         print("*",end=" ")
#     print()

# rows = int(input(" Enter the number of rows :"))
# for i in range(0,rows+1):
#     a=rows
#     for j in range(i):
#         print(" ",end =" ")
#     for j in range(a-i):
#         print("*",end=" ")
#         a=a-1
#     print()


# #inverse equilateral triangle
# rows = int(input(" Enter the number of rows :"))
# for i in range(0,rows+1):
#     a=rows+1
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(a-i):
#         print(" * ", end=" ")
#     print()



# rows = int(input(" Enter the number of rows :"))
# for i in range(0,rows+1):
#     a=rows+1
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(a-i):
#         print(" * ", end=" ")
#     print()
#     # # while printed 
#     # for k in range(a-i):
#     #     print("*",end=" ")
#     # print()


# rows=int(input("Enter the rows :"))
# def pyramid(rows):
#     for i in range(rows):
#         print(' '*(rows-i-1)+'* '*(i+1))
#     for j in range(rows-1,0,-1):
#         print(' '*(rows-j)+"* "*(j))
# pyramid(rows)


# rows=int(input("Enter the rows :"))
# def pyramid(rows):
#     for i in range(rows,0,-1):
#         print(' '*(rows-i)+"* "*(i))
    
#     for j in range(rows):
#         print(' '*(rows-j-1)+'* '*(j+1))
    
# pyramid(rows)


