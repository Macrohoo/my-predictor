import pandas as pd
import numpy as np

#球员精确数据源
df_data = pd.read_excel("球员数据源.xlsx")
df_data = df_data.set_index(['TEAM','Date'])#复合索引 重新将多列设置为索引

#指定球员数据源制作
df_player = pd.read_excel("球员数据源.xlsx")

#层次索引合并
lefth = df_player
righth = df_data
#由Team和Date为连接键的列，以lefth为基础的左连接，右侧行索引作为连接键
df_merge = pd.merge(lefth, righth, left_on=['TEAM', 'Date'], right_index = True)

#输出Excel
df_merge.to_excel("球员新数据.xlsx", index = False)
