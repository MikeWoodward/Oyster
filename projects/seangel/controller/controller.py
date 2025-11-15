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
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs
from model.model import Model
from view.about import About
from view.scheduletests import ScheduleTests
from view.analyzetests import AnalyzeTests


# %%---------------------------------------------------------------------------
# Controller
# -----------------------------------------------------------------------------
class Controller():
    """The Controller class is part of the model-view-controller architecture.
    Links views and Model and controls interaction between them."""

    # %%
    def __init__(self):
        """Method initializes object. First part of two-part initialization. The
        initialization done here should be low risk - we need the GUI to be built
        before we can show error messages."""

        self.model = Model()

        # Create the panels by instantiating each of the tabs. Note the order
        # in the list is the tab order in the GUI.
	self.about = About(self)
self.scheduletests = ScheduleTests(self)
self.analyzetests = AnalyzeTests(self)

        self.panels = [self.about,
                       self.scheduletests,
                       self.analyzetests]

        # Create tabs, note the order here is the display order.
        self.tabs = Tabs(tabs=[p.panel for p in self.panels])

    # %%
    def setup(self):
        """Method sets up object. Second part of two-part initialization."""

        for panel in self.panels:
            panel.setup()

    # %%
    def update(self):
        """Method updates object."""

        self.model.update()

        for panel in self.panels:
            panel.update()

    # %%
    def display(self):
        """Displays the visualization. Calls the Bokeh methods to make the
        application start. Note the server actually renders the GUI in the
        browser.
        Returns:
        None"""

        curdoc().add_root(self.tabs)
        curdoc().title = 'seangel'
