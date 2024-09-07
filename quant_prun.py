import torch
from torch.quantization import quantize_dynamic
from simple_cnn import SimpleCNN

# Load your model
num_classes = 5
model = SimpleCNN(num_classes=num_classes)
model.load_state_dict(torch.load('model.pth'))

# Quantize the model
model_quantized = quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
torch.save(model_quantized.state_dict(), 'model_quantized.pth')
