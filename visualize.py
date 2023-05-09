import cv2
import json
import requests
import numpy as np
import matplotlib.pyplot as plt

# Load the response from the JSON file
with open("response.json", "r") as f:
    response = json.load(f)

# Load the image
image_url = "https://firebasestorage.googleapis.com/v0/b/code-transcriber.appspot.com/o/misc%2Ftest3.jpg?alt=media&token=ef165a60-294c-4a46-b135-53c339ec7bc1"
image_data = requests.get(image_url).content
image_data = np.frombuffer(image_data, dtype=np.uint8)
image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Draw bounding boxes around entire lines
pages = response["responses"][0]["fullTextAnnotation"]["pages"]
for page in pages:
    for block in page["blocks"]:
        for paragraph in block["paragraphs"]:
            for line in paragraph["words"]:
                vertices = line["boundingBox"]["vertices"]
                pts = [(v["x"], v["y"]) for v in vertices]
                cv2.polylines(image, [np.array(pts)], True, (0, 255, 0), 2)

# Display the image with bounding boxes
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.axis("off")
plt.show()
