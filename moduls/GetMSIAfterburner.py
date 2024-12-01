# -*- coding:utf-8 -*-
import datetime
def get_MSI(文件路径):
    原数据文件=open(f"{文件路径}","r",encoding="ANSI")
    监控项目_list=[]
    数据=[]
    时间轴_绝对=[]
    时间轴_相对=[]
    #数据为原文本按行分割后的列表
    for i in 原数据文件:
        数据.append(i)
    #获取软件版本
    软件版本=数据[0].split(",")[-1].replace("\n","").lstrip().rstrip()
    #获取显卡型号
    显卡型号=数据[1].split(",")[-1].replace("\n","").lstrip().rstrip()
    #获取监控项目
    for i in range(2,len(数据[2].split(","))):
        监控项目_list.append(数据[2].split(",")[i].replace("\n","").lstrip().rstrip())
    #获取开始记录的行数
    for i in range(len(数据)):
        if 数据[i].split(",")[0]=="80":
            开始记录的行数=i
            break
    #获取时间轴
    for i in range(开始记录的行数,len(数据)):
        时间轴_绝对.append(datetime.datetime.strptime((数据[i].split(",")[1].lstrip()),'%m-%d-%Y %H:%M:%S'))
        时间轴_相对.append(str(时间轴_绝对[i-开始记录的行数]-时间轴_绝对[0]))
    return 监控项目_list,数据,时间轴_绝对,时间轴_相对,开始记录的行数