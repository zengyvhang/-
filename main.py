# -*- coding:utf-8 -*-
import threading
import pyecharts
from pyecharts.types import opts
from moduls.Build import build
from moduls.GetMSIAfterburner import get_MSI
from moduls.Getscene import get_scene
import datetime
isMSi =True
文件路径="./HardwareMonitoring.hml"
是否显示x轴=False
是否显示y轴=True
数据颜色='#AEE8FC'
背景颜色="#000000"
s=datetime.datetime.now()
if isMSi==True:
    监控项目_list,数据,时间轴_绝对,时间轴_相对,开始记录的行数=get_MSI(文件路径)
    a=2
else:
    监控项目_list,数据,时间轴_绝对,时间轴_相对,开始记录的行数=get_scene(文件路径)
    a=0
#创建图标并添加y轴
for 监控项目索引 in range(len(监控项目_list)):
    y_list=[]
    for i in range(开始记录的行数,len(数据)):
        y_list.append(数据[i].split(",")[监控项目索引+a].replace("\n","").replace(" ",""))
    图表=pyecharts.charts.Line(init_opts=opts.InitOpts(width='1920px', height='1080px',bg_color=None))
    #多线程
    build_thread_项目=threading.Thread(target=build,args=(
        图表,
        时间轴_相对,
        y_list,
        监控项目_list[监控项目索引],
        数据颜色,
        背景颜色,
        是否显示x轴,
        是否显示y轴,
        s,
        ))
    build_thread_项目.start()
