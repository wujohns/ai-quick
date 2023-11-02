# 使用手动求导模拟 pytorch 的自动求导逻辑
import torch

class line(torch.autograd.Function):
  @staticmethod
  def forward(ctx, w, x, b):
    # y = w*x + b
    ctx.save_for_backward(w, x, b)
    return w * x + b

  @staticmethod
  def backward(ctx, grad_out):
    w, x, b = ctx.saved_tensors
    grad_w = grad_out * x   # w 的导数为 x
    grad_x = grad_out * w   # x 的导数为 w
    grad_b = grad_out       # b 的导数为 1
    return grad_w, grad_x, grad_b
  
w = torch.rand(2, 2, requires_grad=True)
x = torch.rand(2, 2, requires_grad=True)
b = torch.rand(2, 2, requires_grad=True)

out = line.apply(w, x, b)
out.backward(torch.ones(2, 2))

print(w)
print(x)
print(b)
print('-------------')
print(w.grad)
print(x.grad)
print(b.grad)
