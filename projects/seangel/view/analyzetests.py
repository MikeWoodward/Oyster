#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project: seangel.

Description:
Sea Angel is a retailer web page timing analysis tool.

Author: Mike Woodward

Created on: 2020-09-25

© Copyright True Fit Inc, 2020.
This software is confidential and proprietary information of True Fit, Inc. It
may not be distributed in whole or part outside of True Fit without the express
written permission of True Fit, Inc.
"""

# %%---------------------------------------------------------------------------
# Module metadata
# -----------------------------------------------------------------------------
__author__ = "Mike Woodward"


# %%---------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import pandas as pd
from bokeh.models.widgets import (Button,
                                  DataTable,
                                  Div,
                                  Panel,
                                  TableColumn)
from bokeh.models import ColumnDataSource
from bokeh.layouts import column

# %%---------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


# %%---------------------------------------------------------------------------
# AnalyzeTests
# -----------------------------------------------------------------------------
class AnalyzeTests():
    """Dialog to select tests for analysis."""

    # %%
    def __init__(self, controller):
        """Method initializes object. First part of two-part initialization.
        Put initialization code here that's very unlikely to fail."""

        self.controller = controller

        # Available tests to analyze.
        self.availableheader = Div(
            text="""Tests you can analyze.""",
            sizing_mode="""stretch_width""")
        # Stub code for DataTable setup.
        source = ColumnDataSource(pd.DataFrame({'x':[1], 'y':[2]}))
        columns = [TableColumn(field='x', title='x_t'),
                   TableColumn(field='y', title='y_t')]
        # Test results pool.
        self.testresultsavailable = DataTable(
            source=source,
            columns=columns)
        # Stub code for DataTable setup.
        source = ColumnDataSource(pd.DataFrame({'x':[1], 'y':[2]}))
        columns = [TableColumn(field='x', title='x_t'),
                   TableColumn(field='y', title='y_t')]
        # The tests the user has selected for analysis.
        self.testresultsselected = DataTable(
            source=source,
            columns=columns)
        # Run the analysis the user has selected
        self.runanalysis = Button(
            label="""Run analysis.""",
            sizing_mode="""stretch_width""",
            button_type="""success""")
        # Progress of the analysis.
        self.analysisprogress = Div(
            text="""No test selected.""",
            sizing_mode="""stretch_width""")

        # Layout the widgets
        self.layout = column(children=[self.availableheader,
                                       self.testresultsavailable,
                                       self.testresultsselected,
                                       self.runanalysis,
                                       self.analysisprogress],
                             sizing_mode='scale_width')
        self.panel = Panel(child=self.layout,
                           title='Analyze tests')


    # %%
    def setup(self):
        """Method sets up object. Second part of two-part initialization.
        Place initialization code here that's more likely to fail."""

        # Setup the callbacks.
        self.runanalysis.on_click(self.callback_runanalysis)


    # %%
    def update(self):
        """Method updates view object. By default, just a stub. Depending
        on your implementation, it might not be needed."""

        pass


    # %%
    def callback_runanalysis(self):
        """Callback method for the Button Bokeh attribute self.runanalysis."""

        # This is stub code. Replace the line below with your code.
        self.update()
