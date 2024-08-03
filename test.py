# import random
#
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# from torch.autograd import Variable
# import torchvision.datasets as dset
# import torchvision.transforms as transforms
# import torch.optim as optim
# import time
# import matplotlib.pyplot as plt
#
#
# trans = transforms.Compose([transforms.ToTensor()])  # Transformador para el dataset
# root = "./data"
# test_set = dset.MNIST(root=root, train=False, transform=trans)
#
# img = [random.randint(0, len(test_set)-1) for _ in range(20)]
#
# _, axes = plt.subplots(nrows=4, ncols=5, figsize=(11, 7))
# aa = iter(img)
# for i, ax in enumerate(axes):
#     for j, axe in enumerate(ax):
#         id = next(aa)
#         axe.imshow(test_set[id][0].squeeze(0), cmap=plt.cm.gray_r, interpolation="nearest")
#         axe.set_title(test_set[id][1])
#
# plt.show()

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-100000, 100000, 100000)

plt.plot(x, np.tan(x))
plt.show()
