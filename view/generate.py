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
from io import BytesIO
import base64
from bokeh.models.widgets import (Button,
                                  Div,
                                  FileInput,
                                  Panel,
                                  Select)
from bokeh.layouts import column


# %%---------------------------------------------------------------------------
# Generate
# -----------------------------------------------------------------------------
class Generate():
    """Panel generates projects from a JSON specification file."""

    # %%
    def __init__(self, controller):
        """Method sets up object. First part of two-part initialization."""

        self.controller = controller

        # Describe the selection options
        self.description = \
            Div(text="""You need to choose the JSON schema file and """
                     """the JSON specification file. The schema file """
                     """contains the code generation rules and the """
                     """specification file contains details for the """
                     """application you want to generate.""",
                sizing_mode="""stretch_width""")
        # Schema description
        self.description_schema = \
            Div(text="""Select the schema you want to use for code """
                     """generation. Unless you know otherwise, you """
                     """should use the first schema on the list.""")
        # Schema selection
        self.select_schema = Select(
            title="Schemas:",
            value="foo",
            options=["foo", "bar", "baz", "quux"],
            sizing_mode="""fixed""",
            width=300)

        # Describe the specification file
        self.description_specification = \
            Div(text="""Choose the specification file to generate the """
                     """application.""",
                sizing_mode="""stretch_width""")
        # The specification file.
        self.specification_file = FileInput(accept='.json',
                                            sizing_mode="""stretch_width""")
        # Generates project from the specification file.
        self.generate = Button(label="""Generate""",
                               button_type="""success""",
                               width=300,
                               sizing_mode='fixed')

        # Error message description
        self.message = \
            Div(text="""""",
                sizing_mode="""fixed""",
                width=300)

        # Layout widgets and figures
        self.layout = column(children=[self.description,
                                       self.description_schema,
                                       self.select_schema,
                                       self.description_specification,
                                       self.specification_file,
                                       self.generate,
                                       self.message],
                             sizing_mode='scale_width')
        self.panel = Panel(child=self.layout, title='Generate application')


    # %%
    def setup(self, schemas):
        """Method sets up object. Second part of two-part initialization."""

        if schemas:
            self.select_schema.options = schemas
            self.select_schema.value = schemas[0]

        self.specification_file.on_change('value',
                                          self.callback_specification_file)
        self.generate.on_click(self.callback_generate)


    # %%
    def callback_specification_file(self, attrname, old, new):
        """Callback method for specification file"""

        # File contents converted to a usable format.
        specification_contents = BytesIO(base64.b64decode(
            self.specification_file.value)).getvalue()

        # Schema name
        schema = self.select_schema.value

        # Controller will verify schema
        self.controller.verify(self.specification_file.filename,
                               specification_contents,
                               schema)

    # %%
    def callback_generate(self):
        """Callback method for code generate"""
        self.controller.generate_code()


    # %%
    def display_message(self, text):
        """Display an error or other message"""
        self.message.text = """<hr>""" + text
