# test_real_time.py

import torch
import cv2
from torchvision import transforms
from PIL import Image
from simple_cnn import SimpleCNN

# Parameters
model_path = "gesture_model.pth"
input_size = 224  # Image size expected by the model
num_classes = 5  # Adjust based on your dataset
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Transformations
transform = transforms.Compose([
    transforms.Resize((input_size, input_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Load model
model = SimpleCNN(num_classes=num_classes)
model.load_state_dict(torch.load(model_path, map_location=device))
model.to(device)
model.eval()

# Class labels
class_labels = ['Gesture1', 'Gesture2', 'Gesture3', 'Gesture4', 'Gesture5',  # Update with actual class names
                'Gesture6', 'Gesture7', 'Gesture8', 'Gesture9', 'Gesture10']

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to PIL Image
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    input_image = transform(pil_image).unsqueeze(0).to(device)

    # Prediction
    with torch.no_grad():
        output = model(input_image)
        _, predicted = torch.max(output, 1)
        predicted_label = class_labels[predicted.item()]

    # Display the prediction
    cv2.putText(frame, f'Prediction: {predicted_label}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Gesture Recognition", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
