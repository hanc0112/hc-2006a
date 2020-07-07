#
#
# #
# #
# # def name():
# #     print("111")
# #
# # class Test():
# #     name = "222"
# #
# # print(name())
# # print(Test.name)
#
#
# # print(a + int(b))
# #
# # print(str(a) + b)
# b = 1,2,3,6,4
# t = (1,2,3,4,5)
# l = [1,2,2,5,4,8,7,85]
# s = {12,3,15,56,48,4,65}
# #字符串转列表
# print(list(b))
# #元组转列表
# print(list(t))
# #列表转元组
# print(tuple(l))
# #元组转集合
# print(set(t))
# #集合转列表
# print(list(s))

#打开模式：r 读取 w 请空写入 a 追加写入 b 二进制模式
# 新建文件并命名
# f = open("aaa.txt",'w')#打开文件
# f.write("hello kitty")# write 写入内容至打开的文件
# f.close() #关闭文件

# f = open("aaa.txt",'w')#打开文件
# f.write("sdffwefew\gregregrd\thrhtjgf\n")# write 写入内容至打开的文件
# f.writelines(["fdsghrhdg\nfewFEWfew\nNHYJEAQ\n"])#
# print(f.writable())#判断是否可写入
# f.close() #关闭文件

#
# f = open("aaa.txt",'r')
#
# print(f.read())# 默认读取全部数据
# print(f.read(10))#读取指定大小的数据
# print(f.readline())#按行读取，读取一行
# print(f.readlines())#按行读取，读取所有行
# f.close()

# a = "abcdyfghijklmn"
# print(a[0])
# print(a[-1])
# print(a[1:-2])
# print(a[1:-2:2])
# print(a[-1:0:-1])
# print(a[::-1])
# print(a[2:])
# print(a[:-2])
#

#通过占位符格式化
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d x %d = %d"%(j,i,i*j), end="\t")
#     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",i*j,end="\t")
#     print()
#
#
# #.format
# for i in range(1,10):
#     for j in range(1,i + 1):
#         print("{} x {} = {}".format(j,i,i*j), end ="\t")
#     print()
#
# l = [1,2,3,58,54,69,58,87,54]
#
# l[0] = 20
# print(l)
# l[1:3] = 2,3
# print(l)

#新增数据

# l = [1,2,3,6,5,4]
# l.append("嗯嗯")#添加到最后
# l.append("嗯嗯")
# l.extend(('123','456'))
# l.insert(3,"卡卡")
# print(l)

#
# print(l.pop(1))# 根据下标删除
# print(l)

# l.remove(3)#根据数值删除
# print(l)
#
# l = [True,4,5,6,8,7,9]#python True 1 false 0
# l.remove(1)
# print(l)
#
# l.clear()
# print()

# a = [456,498,48979,7,465,4,98,7,976,46,63,16,4,64,89,82]
# a.sort()
# print()
# a.sort(reverse=True)
# print(a)

# d = {"name":"小米","age":18,"sex":"男"}
#
# for key in d:
#     print(d[key])
#
# for k,v in d.items():
#     print(k,v)

# d = {"name":"小米","age":18,"sex":"女"}
# d["addr"] = "上海闵行"
# print(d)
# d["addr"] = "上海浦东"
# print(d)


#字典添加
# d = {"name":"小米","age":18,"sex":"男"}
#
# d.update({"addr":"上海闵行","学历":"本科"}) #更新数据
# print(d)

# try:
#     f = open("bbbb.txt",'r')
#     print(f.read())
#     f.close()
# except:    #try:    except: 报错继续执行
#     print("文件不存在")
#
#
# print("操作完文件")
#
# def div(a,b):
#     try:
#         return a/b
#     except:
#         return
#
# print(div(10,0))
#
class customException(Exception):
    def __int__(self,value ="值不能为0"):
        self.value = value

    def __str__(self):
        return self.value

a = 0
try:
    if a == 0:
        print("a = {}触发异常".format(a))
        raise customException
    print("a = {}未触发异常".format(a))
except customException as e:
    print(e)