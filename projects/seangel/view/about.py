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
from bokeh.models.widgets import (Div,
                                  Panel)
from bokeh.layouts import column

# %%---------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


# %%---------------------------------------------------------------------------
# About
# -----------------------------------------------------------------------------
class About():
    """Panel to introduce software."""

    # %%
    def __init__(self, controller):
        """Method initializes object. First part of two-part initialization.
        Put initialization code here that's very unlikely to fail."""

        self.controller = controller

        # First column HTML.
        self.column1 = Div(
            text="""LOGO TEXT""",
            sizing_mode="""stretch_width""")
        # Second column HTML.
        self.column2 = Div(
            text="""This application manages the sea angel...""",
            sizing_mode="""stretch_width""")

        # Layout the widgets
        self.layout = column(children=[self.column1,
                                       self.column2],
                             sizing_mode='scale_width')
        self.panel = Panel(child=self.layout,
                           title='About')


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
