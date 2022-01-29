import time

import pymysql
import requests
from lxml import etree

from sqlalchemy import create_engine
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType

call_price = "J29000"
put_price = "J23000"


def remove__(list_content):
    if "," in list_content[0]:
        list_content[0] = "".join(list_content[0].split(","))
    if "," in list_content[1]:
        list_content[1] = "".join(list_content[1].split(","))
    if "," in list_content[2]:
        list_content[2] = "".join(list_content[2].split(","))
    if list_content[1] == "-":
        list_content[1] = ""
    if list_content[2] == "-":
        list_content[2] = ""
    return list_content
def get_data():
    url = "https://fu.minkabu.jp/chart/nk225_option"
    response = requests.get(url)
    element = etree.HTML(response.text)
    thePrice = element.xpath('//*[@id="option_chart_table"]/table/tbody/tr/td[5]/text()')
    callprice = element.xpath('//*[@id="option_chart_table"]/table/tbody/tr/td[4]/span[1]/text()')
    putprice = element.xpath('//*[@id="option_chart_table"]/table/tbody/tr/td[6]/span[1]/text()')
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='js_op',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    engine_js_op = create_engine('mysql+pymysql://root:123456@localhost:3306/js_op')
    cursor = connection.cursor()
    option_list = []
    for i1, i2, i3 in zip(thePrice, callprice, putprice):
        option_list.append(remove__([i1, i2, i3]))
    for item in option_list:
        tablename = "J" + item[0]
        print(tablename, tuple(item[1:]))
        cursor.execute('insert into {0} (callprice,putprice) values {1}'.format(tablename, tuple(item[1:])))
        connection.commit()
        print('向MySQL中添加数据成功！')
    call_price_sql = "select  callprice from {0};".format(call_price)
    call_price_num = pd.read_sql_query(call_price_sql, engine_js_op)
    call_price_list = list(call_price_num["callprice"])
    put_price_sql = "select  putprice from {0};".format(put_price)
    put_price_num = pd.read_sql_query(put_price_sql, engine_js_op)
    put_price_list = list(put_price_num["putprice"])
    time_sql = "select  LastTime from {0};".format(put_price)
    time_num = pd.read_sql_query(time_sql, engine_js_op)
    LastTime_list = list(time_num["LastTime"])
    print(put_price_list)
    print(call_price_list)
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width='1000px', height='300px'))
            .add_xaxis(LastTime_list)
            .add_yaxis("call_spread {0}".format(call_price), call_price_list)
            .add_yaxis("put_spread {0}".format(put_price), put_price_list)
            .set_global_opts(title_opts=opts.TitleOpts(title="js_op", subtitle="js_op"),
                             datazoom_opts=opts.DataZoomOpts(is_show=True))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    )
    line.render('js_op.html')
    line.render_notebook()

    # select  callprice from  J29000;

    connection.close()


# 1 call volumn  element.xpath('//*[@id="option_chart_table"]/table/tbody/tr/td[1]/text()')

# 4 call lastprice element.xpath('//*[@id="option_chart_table"]/table/tbody/tr/td[4]/span[1]/text()')
# 5 thePrice   element.xpath('//*[@id="option_chart_table"]/table/tbody/tr/td[5]/text()')
# 6 put lastprice  element.xpath('//*[@id="option_chart_table"]/table/tbody/tr/td[6]/span[1]/text()')
# 9 call volumn element.xpath('//*[@id="option_chart_table"]/table/tbody/tr/td[9]/text()')

# 4500 1000

# callprice putprice


if __name__ == "__main__":
    while True:
        get_data()
        time.sleep(5)