#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
# from pyspark.sql import SparkSession

inputfile = '../data/sickinfo.xlsx'
data = pd.read_excel(inputfile) #导入数据

df = data.iloc[:,:]
y = data.iloc[:,0]
address = df[df["地址"] != ' ']

print addr_use

# spark = SparkSession\
#         .builder\
#         .appName("EMPI")\
#         .getOrCreate()
# empi = spark.read.csv(inputfile)
#
# print empi.take(10)

