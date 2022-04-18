# 写一个函数，函数参数是一个路径eg文件夹路径,传输之后可以读取文件夹下所有的文件名,然后把文件名写到文件名称列表.xls并可以更新

import os  # 导入os模块
import xlwt

inputFilePath = input("输入文件夹路径")
datas = os.listdir(inputFilePath)  # os.listdir返回path指定的文件夹包含的文件或文件夹的名字的列表
a = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
s = a.add_sheet('sheet表名', cell_overwrite_ok=True)  # 创建工作表sheet
i = 0
for x in datas:
    s.write(i, 0, x)  # 从第0行开始往表中写内容
    i = i+1

n = 0
while os.path.exists(inputFilePath+'/'+'文件名称列表' + str(n) + '.xls'):
    n = n + 1
    
xlsName = '文件名称列表' + str(n) + '.xls'
a.save(xlsName)  # 保存excel
