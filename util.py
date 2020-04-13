"""
file: torchparameters.py

A file containing some parameters for initializing some torch
parameters such as which precision all of the variables should be 
declared in.
"""

import torch

# set default data type for networks
TORCH_DTYPE = torch.float

def set_dtype():
    torch.set_default_dtype(TORCH_DTYPE)
