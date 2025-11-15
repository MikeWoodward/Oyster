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
# ScheduleTests
# -----------------------------------------------------------------------------
class ScheduleTests():
    """Panel to schedule WebPageTest tests."""

    # %%
    def __init__(self, controller):
        """Method initializes object. First part of two-part initialization.
        Put initialization code here that's very unlikely to fail."""

        self.controller = controller

        # help text.
        self.help = Div(
            text="""Helpful text.""",
            sizing_mode="""stretch_width""")
        # Stub code for DataTable setup.
        source = ColumnDataSource(pd.DataFrame({'x':[1], 'y':[2]}))
        columns = [TableColumn(field='x', title='x_t'),
                   TableColumn(field='y', title='y_t')]
        # The specification files available.
        self.specificationsavailable = DataTable(
            source=source,
            columns=columns)
        # Stub code for DataTable setup.
        source = ColumnDataSource(pd.DataFrame({'x':[1], 'y':[2]}))
        columns = [TableColumn(field='x', title='x_t'),
                   TableColumn(field='y', title='y_t')]
        # The specification file selected.
        self.specificationselected = DataTable(
            source=source,
            columns=columns)
        # Submits the tests for execution on WebPageTest
        self.submittests = Button(
            label="""Submit tests to WebPageTest.""",
            sizing_mode="""stretch_width""",
            button_type="""success""")
        # Progress of jobs submitted to WebPageTest.
        self.testprogress = Div(
            text="""No tests submitted.""",
            sizing_mode="""stretch_width""")

        # Layout the widgets
        self.layout = column(children=[self.help,
                                       self.specificationsavailable,
                                       self.specificationselected,
                                       self.submittests,
                                       self.testprogress],
                             sizing_mode='scale_width')
        self.panel = Panel(child=self.layout,
                           title='Schedule tests')


    # %%
    def setup(self):
        """Method sets up object. Second part of two-part initialization.
        Place initialization code here that's more likely to fail."""

        # Setup the callbacks.
        self.submittests.on_click(self.callback_submittests)


    # %%
    def update(self):
        """Method updates view object. By default, just a stub. Depending
        on your implementation, it might not be needed."""

        pass


    # %%
    def callback_submittests(self):
        """Callback method for the Button Bokeh attribute self.submittests."""

        # This is stub code. Replace the line below with your code.
        self.update()
