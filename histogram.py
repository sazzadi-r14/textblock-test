import json
import plotly.graph_objects as go
import matplotlib.pyplot as plt

with open('response.json') as f:
  data = json.load(f)

x_values = []
y_values = []

# Loop through each text annotation
for annotation in data['responses'][0]['textAnnotations']:
  vertices = annotation['boundingPoly']['vertices']
  
  # Loop through each vertex
  for vertex in vertices:
    x_values.append(vertex['x'])
    y_values.append(vertex['y'])




fig = go.Figure()

# Add histogram data for x coordinates
fig.add_trace(go.Histogram(
    x=x_values,
    name='x coordinates', # name used in legend and hover labels
    xbins=dict( # bins used for histogram
        start=min(x_values),
        end=max(x_values),
        size=(max(x_values)-min(x_values))/50
    ),
    marker_color='#EB89B5',
    opacity=0.75
))

# Add histogram data for y coordinates
fig.add_trace(go.Histogram(
    x=y_values,
    name='y coordinates',
    xbins=dict(
        start=min(y_values),
        end=max(y_values),
        size=(max(y_values)-min(y_values))/50
    ),
    marker_color='#330C73',
    opacity=0.75
))

# Overlay histograms
fig.update_layout(
    barmode='overlay',
    title_text='Histogram of x and y coordinates', # title of plot
    xaxis_title_text='Value', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)

fig.show()
"""



# Create a new figure
plt.figure()

# Create a histogram of the x coordinates
plt.subplot(2, 1, 1)  # 2 rows, 1 column, first plot
plt.hist(x_values, bins=50)
plt.title('X Coordinates')

# Create a histogram of the y coordinates
plt.subplot(2, 1, 2)  # 2 rows, 1 column, second plot
plt.hist(y_values, bins=50)
plt.title('Y Coordinates')

# Display the histograms
plt.tight_layout()
plt.show()

"""