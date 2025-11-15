#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 17:35:01 28-Jun-2020

Author: Mike Woodward

Project: oyster

This code is licensed under the MIT license
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
                                  Panel)
from bokeh.layouts import column

# %%---------------------------------------------------------------------------
# CONSTANTS
# -----------------------------------------------------------------------------
TEXT = ("""<h1>Overview</h1>"""
        """<p>"""
        """This software generates an application from a JSON specification """
        """file. The """
        """output is 'bare bones': it will run, but won't function """
        """properly until the user connects up the various elements. """
        """The generated code has a model-view-controller inspired """
        """code structure. """
        """</p>"""
        """<h1>Folder structure</h1>"""
        """<p>"""
        """Oyster generates a project folder that contains main.py, """
        """a model folder that contains the model.py file (where the """
        """project data is handled), a view folder that contains files """
        """for each of the tabs, and a controller folder than contains """
        """controller.py."""
        """</p>"""
        """<h1>Running the generated application</h1>"""
        """<p>"""
        """Let's say you generate an application called 'lighthouse'. To '"""
        """run lighthouse, navigate to the folder above lighthouse and """
        """type<br>"""
        """bokeh serve --show lighthouse"""
        """</p>""")

# %%---------------------------------------------------------------------------
# About
# -----------------------------------------------------------------------------
class About():
    """Describes the application and what it does."""

    # %%
    def __init__(self, controller):
        """Method sets up object. First part of two-part initialization."""

        self.controller = controller

        # Describes the appilciation and what it does.
        self.description = Div(text=TEXT,
                               sizing_mode="""stretch_width""")

        # Layout widgets and figures
        self.layout = column(children=[self.description],
                             sizing_mode='stretch_both')
        self.panel = Panel(child=self.layout, title='About')

    # %%
    def setup(self):
        """Method sets up object. Second part of two-part initialization."""


    # %%
    def update(self):
        """Method updates object."""

        pass
