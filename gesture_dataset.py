
import os
from PIL import Image
from torch.utils.data import Dataset

class GestureDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        self.classes = sorted(os.listdir(data_dir))  # Get the class names
        self.image_paths = []
        self.labels = []

        for idx, gesture in enumerate(self.classes):
            gesture_folder = os.path.join(data_dir, gesture)
            for image_name in os.listdir(gesture_folder):
                image_path = os.path.join(gesture_folder, image_name)
                self.image_paths.append(image_path)
                self.labels.append(idx)

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        image = Image.open(image_path).convert("RGB")
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label
