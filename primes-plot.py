#!/usr/bin/env python

"""
Create a Plotly graphic showing a spiral for a number selected from a slider.
"""

__author__ = "Joel Allred"
__copyright__ = "Copyright 2020, Joel Allred"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Joel Allred"
__email__ = "joel.allred@gmail.com"

import numpy as np
import plotly.graph_objects as go


def add_scatter_and_line(fig, target, colour):
    """
    Add lines and dots of a spiral for target on fig.
    :param fig: The Plotly figure to draw the lines on.
    :param target: Integer to draw the spiral for
    :param colour: Spiral colour
    :return: void
    """
    r = np.arange(1, target + 1)
    theta = target * 2 * np.pi / r
    precision_factor = 20
    r100 = np.arange(1, target + 1, 1 / precision_factor)
    theta100 = target * 2 * np.pi / r100
    fig.add_trace(
        go.Scatterpolar(
            r=r100,
            theta=theta100,
            thetaunit="radians",
            name=target.astype(str),
            mode='lines',
            visible=False,
            line=dict(
                width=0.5,
                color=colour,
                shape='spline'
            )
        )
    )
    fig.add_trace(
        go.Scatterpolar(
            r=r,
            theta=theta,
            thetaunit="radians",
            name=target.astype(str),
            mode="markers",
            visible=False,
            marker=dict(
                color=colour,
                symbol="square",
                size=5
            )
        )
    )


def add_square_root_circle(fig, target):
    """
    Add red square root circle on the figure
    :param fig: The plotly figure to draw the lines on.
    :param target: Integer to draw the spiral for
    :return: void
    """
    square_root_circle_precision = 20
    fig.add_trace(
        go.Scatterpolar(
            r=np.repeat(np.math.sqrt(target), square_root_circle_precision + 1),
            theta=np.arange(0, 2 * np.pi + 10, 2 * np.pi / square_root_circle_precision),
            thetaunit="radians",
            mode='lines',
            name='square root',
            visible=False,
            line=dict(
                width=2,
                color="red",
                shape='spline'
            )
        )
    )


# Create the Plotly figure.
fig = go.Figure()

# Define the range of values for the slider
values = np.arange(1, 100, 1)

# Do we also want to show a spiral for n + 2?
show_plus_two = False

for value in values:
    add_scatter_and_line(fig, value, "royalblue")
    add_scatter_and_line(fig, value + 2, "green")
    add_square_root_circle(fig, value)

fig.update_layout(
    showlegend=True,
    polar=dict(
        radialaxis=dict(showticklabels=True, ticks='', type='log'),  # try log different base?
        angularaxis=dict(showticklabels=False, ticks='')
    )
)

fig.data[0].visible = True
fig.data[1].visible = True
fig.data[2].visible = show_plus_two
fig.data[3].visible = show_plus_two
fig.data[4].visible = True

steps = []
for i in range(len(values)):
    value_id = values[i]
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Showing spiral for: " + str(value_id)}],
        label=value_id.astype(str)
    )
    step["args"][0]["visible"][5 * i] = True
    step["args"][0]["visible"][5 * i + 1] = True
    step["args"][0]["visible"][5 * i + 2] = show_plus_two
    step["args"][0]["visible"][5 * i + 3] = show_plus_two
    step["args"][0]["visible"][5 * i + 4] = True
    steps.append(step)

sliders = [
    dict(
        active=0,
        currentvalue={"prefix": "Showing blue spiral for: "},
        pad={"t": 50},
        steps=steps
    )
]

fig.update_layout(
    sliders=sliders
)

fig.show()
