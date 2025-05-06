import numpy as np
from plyfile import PlyData

# 1) 读取 PLY
ply = PlyData.read('Subsampled-Merged-BINARY-20.ply')
xyz = np.vstack([ply['vertex']['x'],
                 ply['vertex']['y'],
                 ply['vertex']['z']]).T
# 2) 读取强度字段（如果存在，否则补 0）
if 'intensity' in ply['vertex'].data.dtype.names:
    inten = np.array(ply['vertex']['intensity'], dtype=np.float32)
else:
    inten = np.zeros((xyz.shape[0],), dtype=np.float32)
pts = np.hstack([xyz.astype(np.float32),
                 inten.reshape(-1,1)])
# 3) 写入无头 .bin
pts.tofile('semantic_kitti.bin')
