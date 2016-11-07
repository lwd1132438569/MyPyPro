#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt 

#参数初始化
inputfile = '../data/sampling.xlsx'
data = pd.read_excel(inputfile) #导入数据

x = data.iloc[:,1:].as_matrix().astype(int)
y = data.iloc[:,0].as_matrix().astype(int)
print x
print '***************************************'
print x.shape 
print '**************************************'
print y
print '***************************************'

from keras.models import Sequential
from keras.layers.core import Dense, Activation
# from keras.optimizers import SGD

# model = Sequential() #建立模型
# model.add(Dense(10, batch_input_shape=(None, 26)))
# # model.add(Dense(10, init='uniform', input_dim=26))
# # model.add(Activation('relu')) #用relu函数作为激活函数，能够大幅提供准确度
# model.add(Dense(10))
# model.add(Activation('tanh')) #由于是0-1输出，用sigmoid函数作为激活函数

# model.compile(loss='mean_squared_error', optimizer="rmsprop", metrics=["accuracy"])

# model.fit(x, y, nb_epoch = 100, batch_size = 32,validation_data=(x, y)) #训练模型，学习一千次
# yp = model.predict_classes(x).reshape(len(y)) #分类预测

# # from cm_plot import * #导入自行编写的混淆矩阵可视化函数
# # cm_plot(y,yp).show() #显示混淆矩阵可视化结果

model = Sequential()      
model.add(Dense(26,input_dim=26))      
#model.add(Activation(LeakyReLU(alpha=0.01)))   
model.add(Activation('linear'))  
  
model.add(Dense(26))      
#model.add(Activation(LeakyReLU(alpha=0.1)))   
model.add(Activation('linear'))  
  
model.add(Dense(1))      
#model.add(Activation(LeakyReLU(alpha=0.01)))   
model.add(Activation('linear'))  
  
#sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)  
model.compile(loss='mean_squared_error', optimizer="rmsprop", metrics=["accuracy"])  
# sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
# model.compile(loss='mean_squared_error',optimizer=sgd,metrics=["accuracy"])
#model.compile(loss='mean_squared_error', optimizer=sgd, metrics=["accuracy"])  
    
#model.fit(x_train, y_train, nb_epoch=64, batch_size=20, verbose=0)     
hist = model.fit(x, y, batch_size=5, nb_epoch=100, shuffle=True,verbose=0,validation_split=0.2)  
# print(hist.history)  

#plot prediction data  
# out = model.predict(x)
out = model.predict(x, batch_size=5, verbose=0)
print '#####################'
print out
print '#####################'
# print model.summary()
print model.outputs
print '#####################'
print model.get_config()

score = model.evaluate(x, y, batch_size=5) 
# fig, ax = plt.subplots()  
# ax.plot(x, y,'r') 
# ax.plot(x, out, 'k--', lw=4)  
# ax.set_xlabel('Measured')  
# ax.set_ylabel('Predicted')  
# plt.show()  
# figures(hist) 

fig, ax = plt.subplots()
ax.scatter(y, out)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'g', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()