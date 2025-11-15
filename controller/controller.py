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
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs
from model.model import Model
from view.about import About
from view.generate import Generate


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

        # Instantiate each of the tabs.
        self.about = About(self)
        self.generate = Generate(self)

        self.panels = [self.generate,
                       self.about]

        # Create tabs, note the order here is the display order.
        self.tabs = Tabs(tabs=[p.panel for p in self.panels])

    # %%
    def setup(self):
        """Method sets up object. Second part of two-part initialization."""

        schemas = self.model.setup()

        if self.model.error or not schemas:
            self.generate.display_message(self.model.error_string)
        else:
            self.generate.display_message("")

        self.about.setup()
        self.generate.setup(schemas)


    # %%
    def verify(self, specification_filename, specification_contents, schema):
        """Method updates object."""

        self.model.verify(specification_filename,
                          specification_contents,
                          schema)

        if self.model.error:
            self.generate.display_message(self.model.error_string)
            return
        else:
            self.generate.display_message("No verification errors found.")

    # %%
    def generate_code(self):
        """Generates the code."""
        
        self.model.generate()

        if self.model.error:
            self.generate.display_message(self.model.error_string)
        else:
            self.generate.display_message("Code generated successfully.")


    # %%
    def display(self):
        """Displays the visualization. Calls the Bokeh methods to make the
        application start. Note the server actually renders the GUI in the
        browser.
        Returns:
        None"""

        curdoc().add_root(self.tabs)
        curdoc().title = 'oyster'
