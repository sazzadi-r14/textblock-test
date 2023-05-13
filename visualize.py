import cv2
import json
import requests
import numpy as np
import matplotlib.pyplot as plt

# Load the response from the JSON file
with open("response.json", "r") as f:
    response = json.load(f)

# Load the image
image_url = "https://firebasestorage.googleapis.com/v0/b/code-transcriber.appspot.com/o/misc%2Ftest4.jpg?alt=media&token=26480a5f-8b7e-43b7-81de-b6fffafac426"
image_data = requests.get(image_url).content
image_data = np.frombuffer(image_data, dtype=np.uint8)
image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Draw bounding boxes around entire lines
# Loop through each text annotation
for annotation in response['responses'][0]['textAnnotations']:
  vertices = annotation['boundingPoly']['vertices']

  # Create an array of points for the bounding box
  pts = np.array([[vertex['x'], vertex['y']] for vertex in vertices], np.int32)
  pts = pts.reshape((-1,1,2))

  # Draw the bounding box on the image
  cv2.polylines(image, [pts], True, (0,255,0), 3)

# Save the image with bounding boxes
cv2.imwrite('image_with_boxes.jpg', image)