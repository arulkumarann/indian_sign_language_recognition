import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from gesture_dataset import GestureDataset
from simple_cnn import SimpleCNN
from utils import create_dataloaders

def train_model(model, train_loader, val_loader, criterion, optimizer, scheduler, num_epochs, device, early_stopping_patience=3):
    best_val_loss = float('inf')
    patience_counter = 0

    for epoch in range(num_epochs):
        print(f"Epoch {epoch+1}/{num_epochs}")
        print("-" * 10)

        # Training phase
        model.train()
        running_loss = 0.0
        running_corrects = 0

        for inputs, labels in train_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            _, preds = torch.max(outputs, 1)
            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)

        epoch_loss = running_loss / len(train_loader.dataset)
        epoch_acc = running_corrects.double() / len(train_loader.dataset)

        print(f"Train Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}")

        # Validation phase
        model.eval()
        running_loss = 0.0
        running_corrects = 0

        with torch.no_grad():
            for inputs, labels in val_loader:
                inputs = inputs.to(device)
                labels = labels.to(device)

                outputs = model(inputs)
                loss = criterion(outputs, labels)

                _, preds = torch.max(outputs, 1)
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

        val_loss = running_loss / len(val_loader.dataset)
        val_acc = running_corrects.double() / len(val_loader.dataset)

        print(f"Val Loss: {val_loss:.4f} Acc: {val_acc:.4f}")

        # Check for early stopping
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            torch.save(model.state_dict(), 'best_model2.pth')
        else:
            patience_counter += 1
            if patience_counter >= early_stopping_patience:
                print("Early stopping triggered")
                break

        # Adjust learning rate
        scheduler.step()

    return model

def evaluate_model(model, test_loader, criterion, device):
    model.eval()
    running_loss = 0.0
    running_corrects = 0

    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)

            outputs = model(inputs)
            loss = criterion(outputs, labels)

            _, preds = torch.max(outputs, 1)
            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)

    test_loss = running_loss / len(test_loader.dataset)
    test_acc = running_corrects.double() / len(test_loader.dataset)

    print(f"Test Loss: {test_loss:.4f} Acc: {test_acc:.4f}")

if __name__ == "__main__":
    # Parameters
    data_dir = "processed_videos"
    batch_size = 32
    num_epochs = 50  # Increased epochs to allow for early stopping
    learning_rate = 0.0001

    # Data transformations with augmentation
    transform = transforms.Compose([
        transforms.RandomResizedCrop(224),  # Randomly crop and resize images
        transforms.RandomHorizontalFlip(),  # Randomly flip images horizontally
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # Dataset and DataLoader
    dataset = GestureDataset(data_dir, transform=transform)
    train_loader, val_loader, test_loader = create_dataloaders(dataset, batch_size)

    # Model
    num_classes = len(dataset.classes)
    model = SimpleCNN(num_classes=num_classes)

    # Add dropout layers in SimpleCNN and L2 regularization in optimizer (if not done already)

    # Loss function, optimizer, scheduler
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=0.01)  # L2 regularization
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)

    # Device configuration
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Train the model
    model = train_model(model, train_loader, val_loader, criterion, optimizer, scheduler, num_epochs, device)

    # Load the best model and evaluate on the test set
    model.load_state_dict(torch.load('best_model2.pth'))
    evaluate_model(model, test_loader, criterion, device)

    # Save the trained model
    print("Training complete. Saving the final model.")
    torch.save(model.state_dict(), 'final_model2.pth')
