# # if 结构
# score1 = int(input("请输入一个人0~100的整数："))
#
# if score1<60:
#     print("不合格")
#
# if (score1>=60) and (score1<80):
#     print("仍需努力")
#
# if score1>=80:
#     print("优秀")
#
#
# #if-else 结构
# score2 = int(input("请输入一个人0~100的整数："))
# if score2>=60:
#     if score2>=85:
#         print("优秀")
#     else:
#         print("还差点！")
# else:
#     print("不合格")
#
#
# #if-elif-else 结构
# score3 = int(input("请输入一个人0~100的整数："))
# if score3>90:
#     print("A")
# elif score3>80:
#     print("B")
# elif score3>70:
#     print("C")
# else:
#     print("D")


#while循环
i=0
while i*i<100:
    i+=1
    print(str(i)+'*'+str(i) +'=',i*i)
else:
    print("over")

#for循环
for item in "Hell":
    print("item",item)
numbers = [54,66,88,95,10]
for it in numbers:
    print(it)
else:
    print("over")

#跳转语句
# for ite in range(10):
#     if ite ==3:
#         break
#     print(ite)
# else:
#     print("ove")

for ite in range(10):
    if ite ==3:
        continue
    print(ite)
else:
    print("over11")