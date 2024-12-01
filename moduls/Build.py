# -*- coding:utf-8 -*-
from snapshot_phantomjs import snapshot
from pyecharts.types import opts
import pyecharts
import datetime
def build(图表,相对时间,zjz,项目,数据颜色,背景颜色,是否显示x轴,是否显示y轴,s):

    #图表=pyecharts.charts.Bar(init_opts=opts.InitOpts(width='1920px', height='1080px',bg_color='GREEN'))
    图表.add_xaxis(相对时间)
    图表.add_yaxis("",zjz,color=数据颜色,is_symbol_show=False)
    
    #设置全局配置项
    图表.set_global_opts(
        toolbox_opts=opts.ToolboxOpts(
            feature=opts.ToolBoxFeatureOpts(save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                type_ = ".png",
                name=f"{项目}",
                background_color=背景颜色,
                pixel_ratio=1,
            ),
                                            brush=1,                       
                                            )
            ),
        yaxis_opts=opts.AxisOpts(             
                                 max_=120,
                                 is_show= 是否显示y轴,
                                 ) ,
        xaxis_opts=opts.AxisOpts(
                                 is_show= 是否显示x轴,
                                 ) ,
    )
    #pyecharts.render.make_snapshot(snapshot,图表.render(f"./output/{项目}.html"),f"./output/{项目}.png")
    图表.render(f"./output/{项目}.html")
    print(datetime.datetime.now()-s)