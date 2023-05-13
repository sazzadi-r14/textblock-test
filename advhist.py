import json
import plotly.graph_objects as go

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
    y_values.append((vertices[0]['y'] + vertices[2]['y']) / 2)  # Taking average of y-coordinates of first and third vertex

fig = go.Figure()

# Add histogram data for x coordinates
fig.add_trace(go.Histogram(
    x=x_values,
    name='x coordinates',
    xbins=dict(
        start=min(x_values),
        end=max(x_values),
        size=1  # Bin size of 1 pixel
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
        size=1  # Bin size of 1 pixel
    ),
    marker_color='#330C73',
    opacity=0.75
))

# Overlay histograms
fig.update_layout(
    barmode='overlay',
    title_text='Histogram of x and y coordinates',
    xaxis_title_text='Value',
    yaxis_title_text='Count',
    bargap=0.2,
    bargroupgap=0.1
)

fig.show()
