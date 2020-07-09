# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:10:02 2020

@author: Administrator
"""
import pandas as pd
from pd import dataframe
#部分重命名columns = dict，使用字典类型的数据对列进行重命名。
dataframe.rename(columns = {"old_name": "new_name"})
dataframe.rename(columns = {"old1": "new1", "old2":"new2"},  inplace=True)
#全部重命名 columns = new_columns，新列名的长度必须与旧列名一致。
new_col = ['new1', 'new2',... , 'newn']
dataframe.columns = new_col
#读取文件的时候重命名 names = new_col，可以在读取文件的时候，给出新列名。
pd.read_csv('data', names = new_col, header=0)
#使用str
dataframe.columns = dataframe.columns.str.replace('' '', ''_'')