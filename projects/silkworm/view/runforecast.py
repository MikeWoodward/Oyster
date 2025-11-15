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
from bokeh.models.widgets import (Div,
                                  Panel,
                                  Select,
                                  TextInput)
from bokeh.layouts import column

# %%---------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


# %%---------------------------------------------------------------------------
# RunForecast
# -----------------------------------------------------------------------------
class RunForecast():
    """Run the forecast."""

    # %%
    def __init__(self, controller):
        """Method initializes object. First part of two-part initialization.
        Put initialization code here that's very unlikely to fail."""

        self.controller = controller

        # Explains how to run the model.
        self.headingrunexplain = Div(
            text="""Select the year for analysis then run the forecast.""",
            sizing_mode="""stretch_width""")
        # Menu of available Presidential elections to forecast.
        self.selecttheyeartoforecast = Select(
            title="""Year to forecast""",
            options=['dummy1', 'dummy2', 'dummy3'],
            value="""dummy1""")
        # Shows status of the forecast model.
        self.statusreport = TextInput(
            title="""Run the forecast""",
            value="""No forecast results run.""")

        # Layout the widgets
        self.layout = column(children=[self.headingrunexplain,
                                       self.selecttheyeartoforecast,
                                       self.statusreport],
                             sizing_mode='scale_width')
        self.panel = Panel(child=self.layout,
                           title='Run forecast')


    # %%
    def setup(self):
        """Method sets up object. Second part of two-part initialization.
        Place initialization code here that's more likely to fail."""

        # Setup the callbacks.
        self.selecttheyeartoforecast.on_change("value", self.callback_selecttheyeartoforecast)
        self.statusreport.on_change("value", self.callback_statusreport)


    # %%
    def update(self):
        """Method updates view object. By default, just a stub. Depending
        on your implementation, it might not be needed."""

        pass


    # %%
    def callback_selecttheyeartoforecast(self, attrname, old, new):
        """Callback method for the Select Bokeh attribute self.selecttheyeartoforecast."""
        # This is stub code. Replace the line below with your code.
        self.update()


    # %%
    def callback_statusreport(self, attrname, old, new):
        """Callback method for the TextInput Bokeh attribute self.statusreport."""
        # This is stub code. Replace the line below with your code.
        self.update()
