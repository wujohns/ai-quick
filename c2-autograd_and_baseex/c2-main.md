# 自动求导与基础案例
本章节主要就 ai 开发的基础原理，以及在该原理上当前生态的工程使用做详细说明，主要内容包含:  
1. 导数运算在 ai 训练中的运作流程以及作用  
1. 张量(Tensor)的相关介绍  
1. pytorch 反向传播的简单展示  
1. pytorch 实践项目，以及其工程上的计算图机制  

## 导数运算与训练流程
求导在 ai 训练中扮演了关键角色，特别是在深度学习领域。这里通过一个简单的求导案例，简要说明训练流程:  
1. 目前有数据 data_x 与 data_y，期望可以通过 data_x 预测 data_y  
1. 同时指定损失计算方法为 `loss = (预测值 - 实际值)^2` 
1. 现建立一个模型只有一个参数 w，将其模型计算定义为 `y = w * x`，并将 w 的初始值设定为 start_w  
1. 基于该模型计算的预测值为 `infer_y = start_w * data_x`  
1. `loss = (infer_y - data_y)^2`  
1. 损失函数相对于 infer_y 的导数为 `dL/dy = 2 * (infer_y - data_y)`  
1. y 相对于 w 的导数为 `dy/dw = x`
1. 通过 [链式法则](/c2-autograd_and_baseex/c2-grad-chain.md) 可以得知：损失函数相对于 w 的导数为 `dL/dw = (dL/dy) * (dy/dw) = 2 * (infer_y - data_y) * data_x`  

上述的 dL/dw 即权重(参数) w 对 loss 的梯度，利用该梯度我们可以去调整参数 w 以实现降低 loss 的目标，例如(这里使用简单的梯度下降算法):  
`new_w = start_w - 学习率 * dL/dw`

重复这样的过程，即可实现对模型参数的训练，这里也有一个简单的图解:  
![train.png](/c2-autograd_and_baseex/train.png)  

## 张量(Tensor)
张量是一种多维数组，是深度学习中最基本的数据结构之一，其主要有以下的作用:  
1. 用于 `描述样本数据` 与 `作为模型参数`  
1. 在框架中封装了针对该类型的方法便于使用 GPU 设备处理处理  
1. 便于计算图的追溯，以实现自动微分从而计算对应参数的梯度(求导得到的导数)  

备注:   
1. 计算图的特性主要便于自动求导，以实现训练过程中的参数的梯度计算，在本章节后续的部分做详细介绍   

## pytorch 自动求导演示
这里用一个简单的案例展示 pytorch 中的自动求导特性，代码如下:  
```py
import torch

w = torch.rand(2, 2, requires_grad=True)
x = torch.rand(2, 2, requires_grad=True)
b = torch.rand(2, 2, requires_grad=True)

out = w * x + b

# 假设这是一个损失函数
# 实际业务中 loss 一般为上述计算的 out 与实际的 out 的差值
loss = out.sum()
loss.backward()

print(out)
print(loss)
print('-------------')

print(w)
print(x)
print(b)
print('-------------')
print(w.grad)     # w 的导数是 x
print(x.grad)     # x 的导数是 w
print(b.grad)     # b 的导数是 1
```

通过运行这里案例，我们可以了解 pytorch 内置的自动求导特性:  
1. w,x,b 均为张量类型(tensor)，其计算过程均会被追踪与记录，即所谓的计算图  
1. 在执行 loss 计算后，并执行 loss.backward() 时，会依据上述的计算图做求导运算，获得的值则会被记录到对应的张量上(该值即为本次计算中对应张量的梯度)  
1. 计算该梯度的方法为自动微分方法配合求导的链式法则获得  

至此通过上述的机制，我们就获取了调整一个模型参数的所依赖的信息了(即模型参数梯度)  
该机制即为 pytorch 的自动求导机制  

## pytorch 实践项目
这里主要将使用 pytorch 实现一个简单的模型训练，详细可查看文档: [c2-bostan](/c2-autograd_and_baseex/c2-bostan.md)  
