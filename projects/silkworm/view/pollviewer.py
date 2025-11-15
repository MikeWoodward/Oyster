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
import pandas as pd
from bokeh.models.widgets import (DataTable,
                                  DateSlider,
                                  Div,
                                  Panel,
                                  TableColumn,
                                  TextInput)
from bokeh.models import ColumnDataSource
from bokeh.layouts import column

# %%---------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


# %%---------------------------------------------------------------------------
# PollViewer
# -----------------------------------------------------------------------------
class PollViewer():
    """Shows the polls in the system for the selected election."""

    # %%
    def __init__(self, controller):
        """Method initializes object. First part of two-part initialization.
        Put initialization code here that's very unlikely to fail."""

        self.controller = controller

        # Stub code for DataTable setup.
        source = ColumnDataSource(pd.DataFrame({'x':[1], 'y':[2]}))
        columns = [TableColumn(field='x', title='x_t'),
                   TableColumn(field='y', title='y_t')]
        # Opinion polls in the system.
        self.opinionpolls = DataTable(
            source=source,
            columns=columns)
        # The date for charting.
        self.choosethedatefordisplay = DateSlider(
            title="""Choose the date for display""",
            start="""2018-11-13T20:20:39+00:00""",
            end="""2025-11-13T20:20:39+00:00""",
            step=10000,
            value="""2018-11-13T20:20:39+00:00""")
        # Explanatory text for election year.
        self.headingselectedelectionyear = Div(
            text="""Selected election year.""",
            sizing_mode="""stretch_width""")
        # The election year used for the simulation.
        self.selectedelectionyear = TextInput(
            title="""Election year""",
            value="""No election year.""")

        # Layout the widgets
        self.layout = column(children=[self.opinionpolls,
                                       self.choosethedatefordisplay,
                                       self.headingselectedelectionyear,
                                       self.selectedelectionyear],
                             sizing_mode='scale_width')
        self.panel = Panel(child=self.layout,
                           title='Poll viewer')


    # %%
    def setup(self):
        """Method sets up object. Second part of two-part initialization.
        Place initialization code here that's more likely to fail."""

        # Setup the callbacks.
        self.choosethedatefordisplay.on_change("value", self.callback_choosethedatefordisplay)
        self.selectedelectionyear.on_change("value", self.callback_selectedelectionyear)


    # %%
    def update(self):
        """Method updates view object. By default, just a stub. Depending
        on your implementation, it might not be needed."""

        pass


    # %%
    def callback_choosethedatefordisplay(self, attrname, old, new):
        """Callback method for the DateSlider Bokeh attribute self.choosethedatefordisplay."""
        # This is stub code. Replace the line below with your code.
        self.update()


    # %%
    def callback_selectedelectionyear(self, attrname, old, new):
        """Callback method for the TextInput Bokeh attribute self.selectedelectionyear."""
        # This is stub code. Replace the line below with your code.
        self.update()
