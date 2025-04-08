#基于机器学习的简单交易策略
#导入 pandas
import pandas as pd
#导入绘图库
import matplotlib.pyplot as plt
#导入金融数据获取模块 AKShare
import akshare as ak
import numpy as np
#导入数据集拆分工具
from sklearn.model_selection import train_test_split
#导入KNN分类模型
from sklearn.neighbors import KNeighborsClassifier

#首先定义一个函数，用来获取数据
#传入的三个参数分别是开始日期、结束日期和输出的文件名
def load_stock(start_date, end_date, output_file):
    #首先让程序尝试读取已经下载并保存的文件
    try:
        df = pd.read_pickle(output_file)
        #如果文件已经存在，则输出 “载入股票数据完毕” 
        print("载入股票数据完毕")
    #如果没有找到文件，则重新下载文件
    except FileNotFoundError:
        print("文件未找到，重新下载中")
        #这里指定下载 601816 的交易数据
        df = ak.stock_zh_a_hist(symbol='601857', period='daily', start_date=start_date, end_date=end_date, adjust='hfq')
        #下载成功后保存为 pickle 文件
        df.to_pickle(output_file)
        #通知我们下载完成
        print("下载完成")
    #最后将下载的数据表进行返回
    return df

