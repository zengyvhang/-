# -*- coding:utf-8 -*-
import datetime
def get_scene(文件路径):
    原数据文件=open(f"{文件路径}","r",encoding="UTF-8")
    监控项目_list=[]
    数据=[]
    时间轴_绝对=[]
    时间轴_相对=[]
    开始记录的行数=1
    #数据为原文本按行分割后的列表
    for i in 原数据文件:
        数据.append(i)
    #获取监控项目
    for i in range(len(数据[0].split(","))):
        监控项目_list.append(数据[0].split(",")[i].replace("\n",""))
    #获取时间轴
    for i in range(1,len(数据)):
        h=i//3600
        m=(i-h*3600)//60
        s=(i-h*3600-m*60)
        时间轴_相对.append(f"{h}:{m}:{s}")
    return 监控项目_list,数据,时间轴_绝对,时间轴_相对,开始记录的行数