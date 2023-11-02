# 波士顿房价预测训练
import torch
import re
import numpy as np
import os

# 绝对路径获取方法
curPath = os.path.dirname(os.path.abspath(__file__))
def getAbsPath (relativePath):
  joinPath = os.path.join(curPath, relativePath)
  return os.path.normpath(
    os.path.abspath(joinPath)
  )
housingDataPath = getAbsPath('./housing.data')

# 数据导入（来自housing.data）start ------------------------------------------------------------------
# 从文件中读取并格式化
ff = open(housingDataPath).readlines()  # 以行的模式读取数据
data = []
for item in ff:
  # 将数据间隔的空格合并为一个空格
  out = re.sub(r'\s{2,}', ' ', item).strip()
  data.append(out.split(' '))

data = np.array(data).astype(np.float32)  # 数据类型转换(string to float64)
print(data.shape)   # 输出 (506, 14) 即 506 行，14 列

# 确认输入输出
Y = data[:, -1]     # 最后一列作为输出
X = data[:, 0:-1]   # 除去最后一列之外，其他列作为输入

# 确认训练集与测试集
X_train = X[0:496, ...]
Y_train = Y[0:496, ...]
X_test = X[496:, ...]
Y_test = Y[496:, ...]

# 数据导入（来自housing.data）end ------------------------------------------------------------------

# 搭建网络 start ------------------------------------------------------------------
class Net(torch.nn.Module):
  def __init__(self, n_feature, n_output):
    super(Net, self).__init__()

    # 定义了一个双层网络
    self.hidden = torch.nn.Linear(n_feature, 100)
    self.predict = torch.nn.Linear(100, n_output)   # 网络层定义(定义了一个简单的只有一层线性层的网络)

  def forward(self, x):
    out = self.hidden(x)
    out = torch.relu(out)
    out = self.predict(out)
    return out

# 初始化网络
net = Net(13, 1)  # 依据上述的数据构建，前13列作为输入(n_feature)，最后一列作为结果(n_output)

# 搭建网络 end --------------------------------------------------------------------

# loss & optimizer 定义（loss方法与优化器）
loss_func = torch.nn.MSELoss()    # 均方函数作为 loss 判定策略
# optimizer = torch.optim.SGD(net.parameters(), lr=0.0001)
optimizer = torch.optim.Adam(net.parameters(), lr=0.01)

# training (这里训练 10000 次)
for i in range(10000):
  # 转换为可用于训练的 tensor 数据结构
  x_data = torch.tensor(X_train, dtype=torch.float32)
  y_data = torch.tensor(Y_train, dtype=torch.float32)

  # 进行 forward 并获取对应的 loss
  pred = net.forward(x_data)
  pred = torch.squeeze(pred)      # 删除冗余维度（需要与 y_data 对齐才能计算 loss）
  loss = loss_func(pred, y_data) * 0.001  # 计算 loss

  # 调用优化器进行优化
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

  # 打印结果
  print('ite:{}, loss:{}'.format(i, loss))
  print(pred[0:10])
  print(y_data[0:10])

  # 使用测试集进行测试
  x_data = torch.tensor(X_test, dtype=torch.float32)
  y_data = torch.tensor(Y_test, dtype=torch.float32)
  pred = net.forward(x_data)
  pred = torch.squeeze(pred)
  loss_test = loss_func(pred, y_data) * 0.001
  print('ite:{}, loss_test:{}'.format(i, loss_test))

# 保存模型 start --------------------------------------------
# 直接保存，占用空间较大，通过 torch.load(<model_path>) 即可载入
torch.save(net, getAbsPath('../models/bostan.pkl'))

# 仅保存参数，需要先定义 net 后，才能载入 net.load_state_dict(<model_path>)
# torch.save(net.state_dict(), getAbsPath('./params.pkl'))

# 保存模型 end --------------------------------------------
