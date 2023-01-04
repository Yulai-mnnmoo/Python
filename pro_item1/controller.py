# score = int(input("请输入一个0-100的整数："))
# if(score>85):
#     print("H")
# if(score<60):
#     print("No")
# if(score<=85 and score>=60):
#     print("can")
#
# if(score>=60):
#     if score>85:
#         print("g")
#     else:
#         print("c")
# else:
#     print("n")

#
# if score>=90:
#     print("A")
# elif score>=85:
#     print("B")
# elif score>=60:
#     print("C")
# else:
#     print("N")


# i=0
#
# while i*i <100:
#     i+=1
#     if i==3:
#         print("b")
#         break
#     print("i=",str(i))
#     print("i*i=",str(i*i))
# else:
#     print("ooo")

#
# for item in "Heeeeeellfdd":
#     print("item",item)
#
# numbers =[25,58,55]
# for it in numbers:
#     print(it)
# else:
#     print("aa")
#
# for its in range(10):
#     if its==3:
#         continue
#     print(its)
# else:
#     print("b")

i=100
a=0
b=0
c=0

# while i<=999:
#     a=i//100
#     b=(i-a*100)//10
#     c=i-a*100-b*10
#     # print(a,b,c)
#     if i==(a**3+b**3+c**3):
#         print("水仙花数有：",i)
#     i+=1


numbers =[]
i=100
while i<1000:
    numbers.append(i)
    i+=1

print(numbers)

for item in numbers:
    a = item // 100
    b=(item-a*100)//10
    c=item-a*100-b*10
    if item==(a**3+b**3+c**3):
        print("sss",item)








