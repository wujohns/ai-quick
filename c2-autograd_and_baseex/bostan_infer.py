# 使用已有的模型进行推理(即应用)
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
modelPath = getAbsPath('../models/bostan.pkl')
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
x_data = torch.tensor(X_test, dtype=torch.float32)
y_data = torch.tensor(Y_test, dtype=torch.float32)

# 使用测试集进行测试 ------------------------------------------------------------------

# 网络的定义依旧需要写好
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

# 载入 model
net = torch.load(modelPath)

# 使用训练好的模型进行测试
pred = net.forward(x_data)
pred = torch.squeeze(pred)
loss_func = torch.nn.MSELoss()
loss_test = loss_func(pred, y_data) * 0.001
print('loss_test:{}'.format(loss_test))
