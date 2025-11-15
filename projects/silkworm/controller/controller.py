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
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs
from model.model import Model
from view.about import About
from view.managedata import ManageData
from view.runforecast import RunForecast
from view.voteforecastbytime import VoteForecastByTime
from view.voteforecastdistribution import VoteForecastDistribution
from view.electoralcollegebygeography import ElectoralCollegeByGeography
from view.electoralcollegebystate import ElectoralCollegeByState
from view.pollviewer import PollViewer


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
self.managedata = ManageData(self)
self.runforecast = RunForecast(self)
self.voteforecastbytime = VoteForecastByTime(self)
self.voteforecastdistribution = VoteForecastDistribution(self)
self.electoralcollegebygeography = ElectoralCollegeByGeography(self)
self.electoralcollegebystate = ElectoralCollegeByState(self)
self.pollviewer = PollViewer(self)

        self.panels = [self.about,
                       self.managedata,
                       self.runforecast,
                       self.voteforecastbytime,
                       self.voteforecastdistribution,
                       self.electoralcollegebygeography,
                       self.electoralcollegebystate,
                       self.pollviewer]

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
        curdoc().title = 'silkworm'
