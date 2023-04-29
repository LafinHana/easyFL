"""
train_data (torch.utils.data.Dataset),
test_data (torch.utils.data.Dataset),
and the model (torch.nn.Module) should be implemented here.

"""
import torch.nn

train_data = None
test_data = None

def get_model(*args, **kwargs) -> torch.nn.Module:
    raise NotImplementedError