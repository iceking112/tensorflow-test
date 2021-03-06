import tensorflow as tf
import numpy as np

# 构建网络
D_input = 2
D_label = 1
D_hidden = 2
lr = 1e-4

x = tf.placeholder(tf.float32, [None, D_input], name="x")
t = tf.placeholder(tf.float32, [None, D_label], name="t")

W_h1 = tf.Variable(tf.truncated_normal([D_input, D_hidden], stddev=0.1), name="W_h")
b_h1 = tf.Variable(tf.constant(0.1, shape=[D_hidden]), name="b_h")
pre_act_h1 = tf.matmul(x, W_h1) + b_h1
act_h1 = tf.nn.relu(pre_act_h1, name='act_h')

W_o = tf.Variable(tf.truncated_normal([D_hidden, D_label], stddev=0.1), name="W_o")
b_o = tf.Variable(tf.constant(0.1, shape=[D_label]), name="b_o")
pre_act_o = tf.matmul(act_h1, W_o) + b_o
y = tf.nn.relu(pre_act_o, name='act_y')

loss = tf.reduce_mean((y - t) ** 2)

train_step = tf.train.AdamOptimizer(lr).minimize(loss)

#生成数据
X=[[0,0],[0,1],[1,0],[1,1]]
Y=[[0],[1],[1],[0]]
X=np.array(X).astype('int16')
Y=np.array(Y).astype('int16')

#加载
sess = tf.InteractiveSession()
tf.initialize_all_variables().run()

#训练
for i in range(50000):
    sess.run(train_step,feed_dict={x:X,t:Y} )
# for i in range(10000):
#     for j in range(X.shape[0]): #X.shape[0]表示样本个数
#         sess.run(train_step,feed_dict={x:X[j],t:Y[j]})

#计算预测值
print(sess.run(y,feed_dict={x:X}))

#查看隐藏层的输出
print(sess.run(act_h1,feed_dict={x:X}))