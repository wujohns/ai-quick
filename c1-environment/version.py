from __future__ import print_function
import torch

print('Is cuda avalible: ', torch.cuda.is_available())
print('Cuda Version: ', torch.version.cuda)
print('Cudnn enable', torch.backends.cudnn.enabled)
print('Cudnn Version', torch.backends.cudnn.version())
print('__vision__', torch.__version__)
