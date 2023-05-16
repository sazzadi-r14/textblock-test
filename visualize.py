import cv2
import json
import requests
import numpy as np
import matplotlib.pyplot as plt
from code_ocr_utils import detect_lines


LINE_COLORS = [
  (230, 25, 75),
  (60, 180, 75),
  (255, 225, 25),
  (0, 130, 200),
  (245, 130, 48),
  (145, 30, 180), 
  (70, 240, 240), 
  (240, 50, 230), 
  (210, 245, 60), 
  (250, 190, 212), 
  (0, 128, 128), 
  (220, 190, 255), 
  (170, 110, 40), 
  (255, 250, 200), 
  (128, 0, 0), 
  (170, 255, 195), 
  (128, 128, 0), 
  (255, 215, 180), 
  (0, 0, 128), 
  (128, 128, 128), 
  (255, 255, 255), 
  (0, 0, 0)
]

# Load the response from the JSON file
with open("response.json", "r") as f:
    response = json.load(f)

response = detect_lines(response)

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
  line_id = annotation['line_id']
  line_color = LINE_COLORS[line_id % len(LINE_COLORS)] 


  # Create an array of points for the bounding box
  pts = np.array([[vertex['x'], vertex['y']] for vertex in vertices[0:2]], np.int32)
  pts = pts.reshape((-1,1,2))
  # Draw the bounding box on the image
  cv2.polylines(image, [pts], True, line_color, 3)

# Save the image with bounding boxes
cv2.imwrite('image_with_boxes.jpg', image)