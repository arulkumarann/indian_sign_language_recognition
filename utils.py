import torch
from torch.utils.data import random_split, DataLoader

def create_dataloaders(dataset, batch_size, split_ratio=(0.8, 0.1, 0.1), num_workers=4, seed=42):
    """
    Create train, validation, and test dataloaders with a given split ratio and batch size.

    Parameters:
        dataset (torch.utils.data.Dataset): The dataset to split.
        batch_size (int): The batch size for the dataloaders.
        split_ratio (tuple): The ratio to split the dataset into train, validation, and test sets.
        num_workers (int): Number of workers for data loading.
        seed (int): Random seed for reproducibility.

    Returns:
        tuple: Train, validation, and test dataloaders.
    """
    # Set seed for reproducibility
    torch.manual_seed(seed)
    
    # Calculate sizes for each split
    total_size = len(dataset)
    train_size = int(split_ratio[0] * total_size)
    val_size = int(split_ratio[1] * total_size)
    test_size = total_size - train_size - val_size
    
    # Ensure the split sizes are correct
    assert train_size + val_size + test_size == total_size, "Split sizes do not match the total dataset size."
    
    # Split the dataset
    train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])
    
    # Create dataloaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)

    return train_loader, val_loader, test_loader
