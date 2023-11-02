# bostan 房价预测问题
1. 这里是一个简易的回归模型案例，主要介绍 pytorch 中训练模型的基础方法  
1. 并依据这个基础案例简要解析 pytorch 的模型训练内在逻辑  

## 样本数据
样本数据是一个 506 行，14 列的房价统计数据，前 13 列为相关参数(输入)，最后一列是房价，数据文件为 [housing.data](/c2-autograd_and_baseex/housing.data)  

## 训练说明
训练代码可以参考 [bostan_train.py](/c2-autograd_and_baseex/bostan_train.py)  
这里对训练部分的核心逻辑做解析说明:  
```py
...
class Net(torch.nn.Module):
  def __init__(self, n_feature, n_output):
    super(Net, self).__init__()

    # 定义了一个双层网络
    self.hidden = torch.nn.Linear(n_feature, 100)
    self.predict = torch.nn.Linear(100, n_output)

  def forward(self, x):
    out = self.hidden(x)
    out = torch.relu(out)
    out = self.predict(out)
    return out

# 初始化网络
net = Net(13, 1)

# loss & optimizer 定义（loss方法与优化器）
loss_func = torch.nn.MSELoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.01)

# training (这里训练 10000 次)
for i in range(10000):
  # 转换为可用于训练的 tensor 数据结构
  x_data = torch.tensor(X_train, dtype=torch.float32)
  y_data = torch.tensor(Y_train, dtype=torch.float32)

  # 进行 forward 并获取对应的 loss
  pred = net.forward(x_data)
  pred = torch.squeeze(pred)  # 删除冗余维度（需要与 y_data 对齐才能计算 loss）
  loss = loss_func(pred, y_data) * 0.001  # 计算 loss

  # 调用优化器进行优化
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
...
```

流程图说明:  
![c2-autograd_and_baseex/train_bostan_struc.png](/c2-autograd_and_baseex/train_bostan_struc.png)  

流程与代码的关系:  
![c2-autograd_and_baseex/train_bostan_compare.png](/c2-autograd_and_baseex/train_bostan_compare.png)  

## 推理说明
推理参考代码 [bostan_infer.py](/c2-autograd_and_baseex/bostan_infer.py)  

## 额外补充说明
1. 由于案例的数据量较少且模型规模较小，所以训练时直接一次性载入了所有训练数据  
1. 实际开发分批载入数据进行训练本次训练中没有体现，在后续章节中训练 gpt2 时会对这类场景再做详细说明    
