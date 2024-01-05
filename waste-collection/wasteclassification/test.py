import io
import torch
from PIL import Image
import cv2

# Load model
model_path = 'best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
model.eval()

img_path = 'test6.png'

# Load and process the image
with open(img_path, 'rb') as f:
    test_image = f.read()
    img = Image.open(io.BytesIO(test_image))
    results = model([img])

# Convert results to a pandas DataFrame for easier manipulation
results_df = results.pandas().xyxy[0]

# Load the image using OpenCV for drawing bounding boxes
img_cv = cv2.imread(img_path)

# Iterate over detected objects and draw bounding boxes
for index, row in results_df.iterrows():
    box = row[['xmin', 'ymin', 'xmax', 'ymax']].astype(int).values
    label = row['name']  # Assuming YOLOv5 provides the 'name' column for class labels
    color = (0, 255, 0)  # Green
    thickness = 2
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    img_cv = cv2.rectangle(img_cv, (box[0], box[1]), (box[2], box[3]), color, thickness)
    img_cv = cv2.putText(img_cv, label, (box[0], box[1] - 5), font, font_scale, color, thickness, cv2.LINE_AA)

# Display the image with bounding boxes
cv2.imshow("Image with Bounding Boxes", img_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the results
print("Results are:\n", results_df)
