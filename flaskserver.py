# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:37:13 2018

@author: Administrator

flaskserver.py
@app.route路由，地址索引需要对应页面上的地址索引
return里面的地址对应文件地址
"""

from flask import Flask,request,render_template
import os
import json

app=Flask(__name__)                     #创建一个flask实例
app.debug = True                       #设置为测试模式，有修改时自动重启，生产环境请勿开启，仅在测试环境使用

class data():
    def __init__(self):
        self.jdshopids = dict(J01='jd店01',
                   J02='jd店02',
                   J03='jd店03',
                   J04='jd店04',
                   J05='jd店05',
                   J06='jd店06')
        self.tmshopids = dict(T01='tm店01',
                     T02='tm店02',
                     T03='tm店03')
        self.hnshops = dict(ZY01='zy店01')
        
    def jd(self):
        return self.jdshopids
    def tm(self):
        return self.tmshopids
    def hn(self):
        return self.hnshops
    
class Analysis_chart():
    """分析的图表类"""
    def __init__(self):
        self.ana_type = None
        self.ana_statue = None
        self.chart_lists = ['line-simple','area-basic','line-smooth']
        self.xAxis = {}              #x轴
        self.yAxis = {}              #y轴
        self.series = {}             #系列，指数据分类
        self.title = {}              #编辑标题栏
        self.legend = {}             #编辑标签栏
        self.toolbox = {}            #编辑工具栏
        self.tooltip = {}            #工具栏的tip
        self.animationEasing = None    #动画缓冲函数：elasticOut弹出式动画
        self.option = {}             #echarts引用的最终json数据
    
    def ECHART(self,**kwargs):
        """series_type 决定图的类型 """
        self.__init__()   #保证每次调用该函数都能初始化参数
        for k in kwargs:
            if 'title_' in k:
                self.title[k.replace('title_','')] = kwargs[k]
            if 'xAxis_' in k:
                self.xAxis[k.replace('xAxis_','')] = kwargs[k]
            if 'yAxis_' in k:
                self.yAxis[k.replace('yAxis_','')] = kwargs[k]
            if 'series_' in k:
                self.series[k.replace('series_','')] = kwargs[k]
            if 'legend_' in k:
                self.legend[k.replace('legend_','')] = kwargs[k]
            if 'toolbox_' in k:
                self.toolbox[k.replace('toolbox_','')] = kwargs[k]
            if 'tooltip_' in k:
                self.tooltip[k.replace('tooltip_','')] = kwargs[k]
            if k=='xAxis':
                self.option['xAxis'] = self.xAxis
            if k=='yAxis':
                self.option['yAxis'] = self.yAxis
            if k=='legend':
                self.option['legend'] = self.legend
        if len(self.title)>0:
            self.option['title'] = self.title
        if len(self.xAxis)>0:
            self.option['xAxis'] = self.xAxis
        if len(self.yAxis)>0:
            self.option['yAxis'] = self.yAxis
        if len(self.series)>0:
            self.option['series'] = self.series
        if len(self.legend)>0:
            self.option['legend'] = self.legend
        if len(self.toolbox)>0:
            self.option['toolbox'] = self.toolbox
        if len(self.tooltip)>0:
            self.option['tooltip'] = self.tooltip
        return json.dumps(self.option)

class reports_img():
    """管理报表中的图片url地址类"""
    def __init__(self):
        self.imgUrl = None
    def get_img_list(self,adr):
        return os.listdir(adr)
    
   
    
    
    
@app.route('/',methods=['GET','POST'])  #路由系统生成 视图对应url
def home():                             #视图函数
    shop = data()
    jdshopids=shop.jd()
    tmshopids=shop.tm()
    hnshops=shop.hn()
    chart = Analysis_chart()
    echarts = []
    option1 = chart.ECHART(title_text=u'折线图',
                          xAxis_type='category',
                          xAxis_data=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                          yAxis_type='value',
                          series_data=[820, 932, 901, 934, 1290, 1330, 1320],
                          series_type='line')
    option2 = chart.ECHART(title_text=u'曲线图',
                          xAxis_type='category',
                          xAxis_data=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                          yAxis_type='value',
                          series_data=[600, 530, 901, 800, 1100, 1068, 1400],
                          series_type='line',
                          series_smooth='true')
    option3 = chart.ECHART(title_text=u'条形图',
                          xAxis_type='category',
                          xAxis_data=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                          yAxis_type='value',
                          series_data=[800, 630, 701, 300, 1100, 868, 1400],
                          series_type='bar')
    option4 = chart.ECHART(title_text=u'饼状图',
                          tooltip_trigger='item',
                          tooltip_formatter="{a} <br/>{b} : {c} ({d}%)",
                          legend_type='scroll',
                          legend_orient='vertical',
                          legend_right=10,
                          legend_top=20,
                          legend_bottom=20,
                          legend_data=['直接访问','邮件营销','联盟广告','视频广告','搜索引擎'],
                          series_name='系列1',
                          series_data=[
                                        {"value":335, "name":'直接访问'},
                                        {"value":310, "name":'邮件营销'},
                                        {"value":234, "name":'联盟广告'},
                                        {"value":135, "name":'视频广告'},
                                        {"value":1548, "name":'搜索引擎'}
                                    ],    #这里要显示，必须得键值对应
                          series_type='pie',
                          series_radius='40%',
                          series_center=['40%', '50%'],
                          series_itemStyle={
                                "emphasis": {
                                    "shadowBlur": 10,
                                    "shadowOffsetX": 0,
                                    "shadowColor": 'rgba(0, 0, 0, 0.5)'}})
    option5 = chart.ECHART(title_text=u'散点图',
                           xAxis={},
                           yAxis={},
                           series_symbolSize=20,
                           series_data=[
                                        [10.0, 8.04],
                                        [8.0, 6.95],
                                        [13.0, 7.58],
                                        [9.0, 8.81],
                                        [11.0, 8.33],
                                        [14.0, 9.96],
                                        [6.0, 7.24],
                                        [4.0, 4.26],
                                        [12.0, 10.84],
                                        [7.0, 4.82],
                                        [5.0, 5.68]
                                    ],
                           series_type='scatter')
    option6 = chart.ECHART(title_text=u'漏斗图',
                           tooltip_trigger='item',
                           tooltip_formatter='{a} <br/> {b} : {c}%',
                           toolbox_feature={
                                            "dataView": {"readOnly": "false"},
                                            "restore": {},
                                            "saveAsImage": {}
                                        },
                           legend_data=['展现','点击','访问','咨询','订单'],
                           legend_bottom='bottom',
                           series_name='漏斗图',
                           series_type='funnel',
                           series_left='10%',
                           series_top=60,
                           series_bottom=60,
                           series_width='80%',
                           series_min=0,
                           series_max=100,
                           series_minSize='0%',
                           series_maxSize='100%',
                           series_sort='descending',
                           series_gap=2,
                           series_label={
                                 "normal": {
                                     "show": "true",
                                     "position": 'inside'
                                 },
                                 "emphasis": {
                                     "textStyle": {
                                         "fontSize": 20
                                     }
                                 }
                             },
                           series_labelLine={
                                 "normal": {
                                     "length": 10,
                                     "lineStyle": {
                                         "width": 1,
                                         "type": 'solid'
                                     }
                                 }
                             },
                           series_itemStyle={
                                 "normal": {
                                     "borderColor": '#fff',
                                     "borderWidth": 1
                                 }
                             },
                           series_data=[
                                 {"value": 60, "name": '访问'},
                                 {"value": 40, "name": '咨询'},
                                 {"value": 20, "name": '订单'},
                                 {"value": 80, "name": '点击'},
                                 {"value": 100,"name": '展现'}
                             ])
    echarts.append(option1)
    echarts.append(option2)
    echarts.append(option3)
    echarts.append(option4)
    echarts.append(option5)
    echarts.append(option6)
    return render_template('home.html', jdshopids=jdshopids, tmshopids=tmshopids, hnshops=hnshops, echarts=echarts, num=[x for x in range(len(echarts))]) #response响应
    
@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')
    
    
@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password.',username=username)

@app.route('/templates/viewflow/shop/<shopid>.html')
def shop(shopid=None):
    shop = data()
    jdshopids=shop.jd()
    tmshopids=shop.tm()
    hnshops=shop.hn()
    if jdshopids.get(shopid,0):
        return render_template('/viewflow/shop.html',shopid = shopid, jdshopids={shopid:jdshopids[shopid]})
    if tmshopids.get(shopid,0):
        return render_template('/viewflow/shop.html',shopid = shopid, tmshopids={shopid:tmshopids[shopid]})
    if hnshops.get(shopid,0):
        return render_template('/viewflow/shop.html',shopid = shopid, hnshops={shopid:hnshops[shopid]})

@app.route('/templates/viewflow/shop/<report>/<report_name>.html')
def report(report='report1', report_name='report1'):
    return render_template('/viewflow/shop/report1.html')

@app.route('/templates/set-echart.html')
def set_echarts():
    params = ["paravalues1","paravalues2","paravalues3"]
    menus = dict(paravalues1=dict(a="leftmenu1_set1",b="leftmenu1_set2"),
                 paravalues2=dict(a="leftmenu2_set1",b="leftmenu2_set2"),
                 paravalues3=dict(a="leftmenu3_set1",b="leftmenu3_set2"))
    menusJson = json.dumps(menus)
    return render_template('set-echart.html', params=params, menus=menus, menusJson=menusJson)

if __name__=='__main__':
    app.run()                           #启动socket