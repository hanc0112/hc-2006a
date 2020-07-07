# # a = 75
# # if a <= 59:
# #     print("不及格")
# # if a in range(60,70):
# #     print("及格")
# # if a in range(71,80) :
# #     print("良好")
# # if a in range(81,100):
# #     print("优秀")
# #
# # sc = 85
# # if (sc > 0 and sc < 60):
# #     print("不及格")
# # if (sc >= 60 and sc <= 70):
# #     print("及格")
# # if (sc > 70 and sc <= 80):
# #     print("良好")
# # if (sc > 80 and sc <= 100):
# #     print("优秀")
# #
# #
# # sc = 8
# # if (sc > 0 and sc < 60):
# #     print("不及格")
# # elif (sc >= 60 and sc <= 70):
# #     print("及格")
# # elif (sc > 70 and sc <= 80):
# #     print("良好")
# # elif (sc > 80 and sc <= 100):
# #     print("优秀")
# #
# # sc_1 = [15,48,58,69,63,85,81,92]
# # for sc in sc_1:
# #  if (sc > 0 and sc < 60):
# #     print("不及格")
# #  elif (sc >= 60 and sc <= 70):
# #     print("及格")
# #  elif (sc > 70 and sc <= 80):
# #     print("良好")
# #  elif (sc > 80 and sc <= 100):
# #     print("优秀")
# #
# #
# #
# # ...
# # s = 1
# # for i in range(10,0,-1):
# #     # print(i)
# #     s *= i
# #     print(s)
#
#
# #
# #
# # flag = True
# # a = 82
# # while flag:
# #     b = int(input("请输入数字"))
# #     if b > a :
# #         print("大了")
# #     elif(b < a):
# #         print("小了")
# #     else:
# #         print("恭喜你，奖金10000000")
# #         flag = False
# # 找出100以内可以被3整除的数字
# for i in range(1,100):
#     if i % 3 == 0:
#         continue
#     print(i)
#
# for i in range(1,100):
#     if i % 3 != 0:
#      print(i)
#      break
#
#
# #定义一个求两个数商和余数的方法
#
# # a = 20
# # b = 30
# def shang_yu(a,b):
#     if(b == 0):
#         return None
#     else:
#         return(a//b,a%b)
#
# res = shang_yu(20,4)#按照位置传参
#
# if res is None:
#     print("参数错误")
# else:
#     print("商为:",res[0],"余数为:",res[1])
#
# def shang_yu(a,b):
#     if(b == 0):
#         return None
#     else:
#         return(a//b,a%b)
#
# res = shang_yu(a=20,b=4) #按照关键字传参
#
# if res is None:
#     print("参数错误")
# else:
#     print("商为:",res[0],"余数为:",res[1])
#
# def sm(a,b=2):#定义关键字形参 给参数b设置默认值
#     return  a+b
#
# print(sm(3,3))
#

# c = 1,2,3,4
# a,*b = (1,2,3,4)
# print(b)

# def sum1(*b):
#     print(b)
#     s = 0
#     for i in b:
#         s+=i
#     return s
# print(sum1(1,2,3,4,5,6,7,8,9))
#
# def sum1(name,**kwargs):#*arge接受动态位置参数，**kwarge 接受动态关键字参数
#     print(name)
#     print(kwargs)
#     # s = 0
#     # for i in arge:
#     #     s+=i
#     # return s
# # print(sum1(1,2,3,4,5,6,7,8,9))
# print(sum1(name="薛小磊", age = 18))

# class calc():
#     a =None
#     b =None
#     res =None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res =self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc() #类的实例化  c 对象
#
# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()


# class calc():
#     # a =None
#     # b =None
#     res =None
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res =self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc(29,39) #类的实例化  c 对象
#
# c.sum()
# c.get_result()
# c.div()
# c.get_result()


for i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,"=",i*j,end="\t")
    print()

# l =[25,6,4,8,2,1,3,5,6,564,94,98,6,648,946,468,46,48,46,31,56,484,6]
#
# length = len(l)
# print(length)
# for i in range(length-1,0,-1): # 外层循环确定排好序的数据下标
#     for j in range(i):# 遍历未排好序的列表
#         if (l[j] > l[j+1]): # 判断相邻两个数据，前边的如果大于后边的，则交换两个数据的位置
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)
#
#
# class Parent():
#     money = 10000000
#     house = 1000
#     __lifetime = "2"
#     _car = "玛莎"
#
#     def skll(self):
#         print("点石成金")
#
# p = Parent(123)
# print(p)
#
# class child(Parent):
#     hobby = "花钱"
#     pass
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#
#     #super().__init__(a)
#
#     def skll(self):
#         super().skll()
#         print("挖掘机")
#
# c = child(123)
#
# print(c.money)
# print(c.house)
# print(c.hobby)
# print(c.skll())
# print(c._car)
