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
from bokeh.models.widgets import (Button,
                                  Div,
                                  Dropdown,
                                  Panel,
                                  TextInput)
from bokeh.layouts import column

# %%---------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


# %%---------------------------------------------------------------------------
# ManageData
# -----------------------------------------------------------------------------
class ManageData():
    """Panel to manage data sources."""

    # %%
    def __init__(self, controller):
        """Method initializes object. First part of two-part initialization.
        Put initialization code here that's very unlikely to fail."""

        self.controller = controller

        # Displays the Electoral College Vote allocations by year.
        self.ecvyearallocations = TextInput(
            title="""Electoral College Vote allocations by year in system""",
            value="""No allocations in system""")
        # Displays the election result years in the system.
        self.electionresults = TextInput(
            title="""Presidential Election results in system""",
            value="""No allocations in system""")
        # Displays the Presidential polling in system.
        self.polling = TextInput(
            title="""Presidential Election polling in system""",
            value="""No allocations in system""")
        # Header to explain what cross-check button does.
        self.headingverification = Div(
            text="""Click the button below to start a cross-check that the data in the system is both correct and consistent.""",
            sizing_mode="""stretch_width""")
        # Starts the verification data cross-check..
        self.verificationbutton = Button(
            label="""Cross-check data.""",
            sizing_mode="""stretch_width""",
            button_type="""success""")
        # Displays the results of the cross-check.
        self.verfificationresults = TextInput(
            title="""Cross-check results""",
            value="""Cross-check verification not run.""")
        # Header to explain what the polling data download does.
        self.headingpollingdatadownload = Div(
            text="""Choose the polling year in the dropdown control and click the download button to download the data.""",
            sizing_mode="""stretch_width""")
        # Polling year to download
        self.pollyear = Dropdown(
            label="""Polling year to download""",
            menu=['dummy1', 'dummy2', 'dummy3'],
            button_type="""warning""")
        # Poll download button
        self.polldownload = Button(
            label="""Download polling data""",
            sizing_mode="""stretch_width""",
            button_type="""success""")
        # Displays the results of the polling download.
        self.pollingdownloadresults = TextInput(
            title="""Polling download results""",
            value="""No polling download.""")

        # Layout the widgets
        self.layout = column(children=[self.ecvyearallocations,
                                       self.electionresults,
                                       self.polling,
                                       self.headingverification,
                                       self.verificationbutton,
                                       self.verfificationresults,
                                       self.headingpollingdatadownload,
                                       self.pollyear,
                                       self.polldownload,
                                       self.pollingdownloadresults],
                             sizing_mode='scale_width')
        self.panel = Panel(child=self.layout,
                           title='Manage data')


    # %%
    def setup(self):
        """Method sets up object. Second part of two-part initialization.
        Place initialization code here that's more likely to fail."""

        # Setup the callbacks.
        self.ecvyearallocations.on_change("value", self.callback_ecvyearallocations)
        self.electionresults.on_change("value", self.callback_electionresults)
        self.polling.on_change("value", self.callback_polling)
        self.verificationbutton.on_click(self.callback_verificationbutton)
        self.verfificationresults.on_change("value", self.callback_verfificationresults)
        self.pollyear.on_click(self.callback_pollyear)
        self.polldownload.on_click(self.callback_polldownload)
        self.pollingdownloadresults.on_change("value", self.callback_pollingdownloadresults)


    # %%
    def update(self):
        """Method updates view object. By default, just a stub. Depending
        on your implementation, it might not be needed."""

        pass


    # %%
    def callback_ecvyearallocations(self, attrname, old, new):
        """Callback method for the TextInput Bokeh attribute self.ecvyearallocations."""
        # This is stub code. Replace the line below with your code.
        self.update()


    # %%
    def callback_electionresults(self, attrname, old, new):
        """Callback method for the TextInput Bokeh attribute self.electionresults."""
        # This is stub code. Replace the line below with your code.
        self.update()


    # %%
    def callback_polling(self, attrname, old, new):
        """Callback method for the TextInput Bokeh attribute self.polling."""
        # This is stub code. Replace the line below with your code.
        self.update()


    # %%
    def callback_verificationbutton(self):
        """Callback method for the Button Bokeh attribute self.verificationbutton."""

        # This is stub code. Replace the line below with your code.
        self.update()


    # %%
    def callback_verfificationresults(self, attrname, old, new):
        """Callback method for the TextInput Bokeh attribute self.verfificationresults."""
        # This is stub code. Replace the line below with your code.
        self.update()


    # %%
    def callback_pollyear(self, new):
        """Callback method for the Dropdown Bokeh attribute self.pollyear."""

        # This is stub code. Replace the line below with your code.
        self.update()


    # %%
    def callback_polldownload(self):
        """Callback method for the Button Bokeh attribute self.polldownload."""

        # This is stub code. Replace the line below with your code.
        self.update()


    # %%
    def callback_pollingdownloadresults(self, attrname, old, new):
        """Callback method for the TextInput Bokeh attribute self.pollingdownloadresults."""
        # This is stub code. Replace the line below with your code.
        self.update()
