import numpy as np
import os
import random

datasets_dir = '/Users/anumitasrivastava/tensorflow/Theano-Tutorials'

def one_hot(x,n):
        if type(x) == list:
                x = np.array(x)
        x = x.flatten()
        o_h = np.zeros((len(x),n))
        o_h[np.arange(len(x)),x] = 1
        return o_h

def mnist2_batch(ntrain=60000,ntest=10000,onehot=True):
        data_dir = os.path.join(datasets_dir)
        fd = open(os.path.join(data_dir,'train-images-idx3-ubyte'))
        loaded = np.fromfile(file=fd,dtype=np.uint8)
        trX = loaded[16:].reshape((60000,28*28)).astype(float)

        fd = open(os.path.join(data_dir,'train-labels-idx1-ubyte'))
        loaded = np.fromfile(file=fd,dtype=np.uint8)
        trY = loaded[8:].reshape((60000))

        fd = open(os.path.join(data_dir,'t10k-images-idx3-ubyte'))
        loaded = np.fromfile(file=fd,dtype=np.uint8)
        teX = loaded[16:].reshape((10000,28*28)).astype(float)

        fd = open(os.path.join(data_dir,'t10k-labels-idx1-ubyte'))
        loaded = np.fromfile(file=fd,dtype=np.uint8)
        teY = loaded[8:].reshape((10000))

        trX = trX/255.
        teX = teX/255.
        num = random.randint(30001,59872)
        num2 = num + 128

        trX = trX[num:num2]
        trY = trY[num:num2]

        teX = teX[:ntest]
        teY = teY[:ntest]

        if onehot:
                trY = one_hot(trY, 10)
                teY = one_hot(teY, 10)
        else:
                trY = np.asarray(trY)
                teY = np.asarray(teY)

        return trX,teX,trY,teY


