#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project: silkworm.

Description:
Silkworm is a poll-based US Presidential Election forecaster.

Author: Mike Woodward

Created on: 2020-10-05


"""

# %%---------------------------------------------------------------------------
# Module metadata
# -----------------------------------------------------------------------------
__author__ = "Mike Woodward"
__license__ = "MIT"


# %%---------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from bokeh.models.widgets import (Panel)
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.layouts import column

# %%---------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


# %%---------------------------------------------------------------------------
# VoteForecastByTime
# -----------------------------------------------------------------------------
class VoteForecastByTime():
    """Shows the forecasted electoral college votes over time."""

    # %%
    def __init__(self, controller):
        """Method initializes object. First part of two-part initialization.
        Put initialization code here that's very unlikely to fail."""

        self.controller = controller

        # Shows the forecast for electoral college votes over time.
        self.electoralcollegevotesbytime = figure(
            title="""Electoral college votes by time""",
            x_axis_type="""datetime""",
            sizing_mode="""stretch_both""")

        # Layout the widgets
        self.layout = column(children=[self.electoralcollegevotesbytime],
                             sizing_mode='scale_width')
        self.panel = Panel(child=self.layout,
                           title='Vote forecast by time')


    # %%
    def setup(self):
        """Method sets up object. Second part of two-part initialization.
        Place initialization code here that's more likely to fail."""

        # No widgets on this tab have a callback, so this is an empty method.
        pass


    # %%
    def update(self):
        """Method updates view object. By default, just a stub. Depending
        on your implementation, it might not be needed."""

        pass
