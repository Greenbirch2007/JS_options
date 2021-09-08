

import datetime
import time

import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException




from retrying import retry
import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException
from lxml import etree


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


















def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l




def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items
def retry_if_io_error(exception):
    return isinstance(exception, ZeroDivisionError)






'''
1. 创建 URL队列, 响应队列, 数据队列 在init方法中
2. 在生成URL列表中方法中,把URL添加URL队列中
3. 在请求页面的方法中,从URL队列中取出URL执行,把获取到的响应数据添加响应队列中
4. 在处理数据的方法中,从响应队列中取出页面内容进行解析, 把解析结果存储数据队列中
5. 在保存数据的方法中, 从数据队列中取出数据,进行保存
6. 开启几个线程来执行上面的方法
'''

def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper




def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num



class JSPool_M(object):

    def __init__(self,url):
        self.url = url

    def page_request(self):

        '''
        服务器上必须配置无头模式
        '''
        ch_options = webdriver.ChromeOptions()
        # # 为Chrome配置无头模式
        # ch_options.add_argument("--headless")
        # ch_options.add_argument('--no-sandbox')
        # ch_options.add_argument('--disable-gpu')
        # ch_options.add_argument('--disable-dev-shm-usage')
        # 在启动浏览器时加入配置
        driver = webdriver.Chrome(options=ch_options)



        driver.get(self.url)
        time.sleep(6)
        #点击

        driver.find_element(By.CSS_SELECTOR, ".side-icon-link-option img").click()

        # 点击后跳转到新页面

        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        html = driver.page_source
        print(html)
        return html

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''


        html  = self.page_request()
        element = etree.HTML(html)

        call_last_price = element.xpath('//*[@id="priceTable"]/div/div[4]/table/tbody/tr/td[8]/text()[1]')
        strike_price = element.xpath('//*[@id="priceTable"]/div/div[4]/table/tbody/tr/td[9]/text()[1]')
        put_last_price = element.xpath('//*[@id="priceTable"]/div/div[4]/table/tbody/tr/td[10]/text()[1]')

        f_strike_price = RemoveDot(remove_block(strike_price))
        base_list = [28250, 28500, 28750, 29000, 29250, 29500, 29750, 30000, 30250, 30500, 30750]
        print(call_last_price)
        # for i1,i2,i3 in zip(call_last_price,f_strike_price,put_last_price):
        #     print(i1,i2,i3)
            # call_list = (i1,i2)
            # put_list= (i3,i2)
            # for item in base_list:
            #     if call_list[1] == item:
            #         print(call_list,put_list)







def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS_Mons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        cursor.executemany('insert into FJSs (js225_,js400_,js_225_4000) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass






if __name__ == '__main__':
    # while True:

    big_list = []
    js_options ='https://www.jpx.co.jp/'


    jsp1 = JSPool_M(js_options)# 这里把请求和解析都进行了处理
    jsp1.page_parse_()


        #
        #
        #
        # js225_=big_list[0]
        # js400_=big_list[1]
        #
        # # 要价差，不要比价
        # js_225_400 = float(js225_)-float(js400_)
        #
        # title_l = [js225_,js400_,js_225_400]
        #
        # ff_l = []
        # f_tup = tuple(title_l)
        # ff_l.append((f_tup))
        # print(big_list)
        # print(ff_l)
        # insertDB(ff_l)
        # time.sleep(60)
        # print(datetime.datetime.now())
#1720
# 1803
# 3612
# 4555







# create table js_options_put (id int not null primary key auto_increment,js28250 FLOAT, js28500 FLOAT, js28750 FLOAT, js29000 FLOAT, js29250 FLOAT, js29500 FLOAT, js29750 FLOAT, js30000 FLOAT, js30250 FLOAT, js30500 FLOAT, js30750 FLOAT, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;
# create table js_options_call (id int not null primary key auto_increment,js28250 FLOAT, js28500 FLOAT, js28750 FLOAT, js29000 FLOAT, js29250 FLOAT, js29500 FLOAT, js29750 FLOAT, js30000 FLOAT, js30250 FLOAT, js30500 FLOAT, js30750 FLOAT, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;
