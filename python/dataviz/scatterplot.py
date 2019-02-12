import numpy as np
import plotly.offline as off
import plotly.graph_objs as go


N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker=dict(
        size=16,
        color=np.random.randn(500), # set color equal to a variable
        colorscale='Viridis',
        showscale=True
    )
)

data = [trace]

off.plot(data, filename='basic-scatter')
