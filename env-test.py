'''
import torch
print("CUDA available:", torch.cuda.is_available())
import range_utils.nn.functional.map_count as mc
print("range_utils loaded:", mc)
'''
import torch
x = torch.randn(2,2).cuda()
print(x * 2)
