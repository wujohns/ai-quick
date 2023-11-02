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
