import torch
import numpy as np
from torch.autograd import Variable

class RandomVariable():
    def _size(self):
        raise NotImplementedError("size is not implemented")
    def _pdf(self):
        raise NotImplementedError("pdf is not implemented")
    def _logpdf(self, x):
        raise NotImplementedError("log_pdf is not implemented")

    def _sample(self):
        raise NotImplementedError("sample is not implemented")


def VariableCast(value, grad = False):
    '''casts an input to torch Variable object
    input
    -----
    value - Type: scalar, Variable object, torch.Tensor, numpy ndarray
    grad  - Type: bool . If true then we require the gradient of that object

    output
    ------
    torch.autograd.variable.Variable object
    '''
    if isinstance(value, Variable):
        return value
    elif torch.is_tensor(value):
        return Variable(value, requires_grad = grad)
    elif isinstance(value, np.ndarray):
        return Variable(torch.from_numpy(value), requires_grad = grad)
    else:
        return Variable(torch.Tensor([value]), requires_grad = grad)
