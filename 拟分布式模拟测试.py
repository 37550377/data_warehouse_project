"""
数据来源kaggle
技术栈 sql，python，pandas，numpy，jupyter
用jupyter模拟分布式测试
"""
# 主机部分
import numpy
import pandas as pd
# 引用文件时import单变量名，类似于数仓开发不用select *

df_csv= pd.read_csv('D:\kaggle\gdp_1960_2020.csv', encoding='gbk')
df = pd.DataFrame(df_csv)
print(df.head())
f1 = df['year'] == 1960      # 对应sql select gdp from gdp_1960_2020 where year = '1960'
f2 = df['year'] == 1961      # 对应sql select gdp from gdp_1960_2020 where year = '1961'
f3 = df['year'] == 1962
# print(df[f1].head())
#    year  rank            country    state           gdp  gdp_percent
# 0  1960     1  the United States  America  5.433000e+11     0.468483
# 1  1960     2     United Kingdom   Europe  7.323397e+10     0.063149
# 2  1960     3             France   Europe  6.222548e+10     0.053656
# 3  1960     4              China     Asia  5.971647e+10     0.051493
# 4  1960     5              Japan     Asia  4.430734e+10     0.038206
===================================================================
# cell1模拟一个分机
gdp_1960 = df[f1]['gdp'].to_numpy().sum()
对应sql
select sum(gdp) from gdp_1960_2020 where year = '1960'
===================================================================
# cell2模拟一个分机
gdp_1961 = df[f2]['gdp'].to_numpy().sum()
对应sql
select sum(gdp) from gdp_1960_2020 where year = '1961'
===================================================================
# 主机部分
gdp_add = sum([gdp_1960,gdp_1961])    #对应sql select year,sum(gdp) from gdp_1960_2020 group by year
print(gdp_add)
