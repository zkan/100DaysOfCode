import plotly.offline as off
import plotly.graph_objs as go


data = [
    {
        'x': [0.2, 0.2, 0.6, 1.0, 0.5, 0.4, 0.2, 0.7, 0.9, 0.1, 0.5, 0.3],
        'y': ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2'],
        'name':'kale',
        'marker': {
            'color': '#3D9970'
        },
        'boxmean': False,
        'orientation': 'h',
        "type": "box",
    },
    {
        'x': [0.6, 0.7, 0.3, 0.6, 0.0, 0.5, 0.7, 0.9, 0.5, 0.8, 0.7, 0.2],
        'y': ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2'],
        'name': 'radishes',
        'marker':{
            'color': '#FF4136',
        },
        'boxmean': False,
        'orientation': 'h',
        "type": "box",
    },
    {
        'x': [0.1, 0.3, 0.1, 0.9, 0.6, 0.6, 0.9, 1.0, 0.3, 0.6, 0.8, 0.5],
        'y': ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2'],
        'name':'carrots',
        'marker': {
            'color': '#FF851B',
        },
        'boxmean': False,
        'orientation': 'h',
        "type": "box",
    }
]
layout = {
    'xaxis': {
        'title': 'normalized moisture',
        'zeroline': False,
    },
    'boxmode': 'group',
}
fig = go.Figure(data=data, layout=layout)
off.plot(fig)
