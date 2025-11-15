#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 07:34:19 2020

@author: mikewoodward
"""

# %%---------------------------------------------------------------------------
# Module metadata
# -----------------------------------------------------------------------------
__author__ = "Mike Woodward"
__license__ = "MIT"


# %%---------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import os
from time import sleep
from datetime import datetime
from string import Template
import re
import shutil
import textwrap


# %%---------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def generate_project_folder(folder_name,
                            folder_location):
    """Generate a project folder."""
    folder = os.path.join(folder_location, folder_name)

    # If the folder exists, create a new folder with a timestamp
    # appended. The sleep statement guarantees uniqueness in a quick
    # and dirty way.
    if os.path.isdir(folder):
        sleep(1)
        folder += '-' + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    os.mkdir(folder)

    return folder


def generate_header_tail(stub, key_list):
    """Generate the tail of the header."""
    return '\n'.join([textwrap.fill(stub[key], 79)
                      for key in key_list if key in stub])


def generate_metadata(stub, key_list):
    """Generate the metadata statements for the files."""
    return '\n'.join(['__{0}__ = "{1}"'.format(key, stub[key])
                      for key in key_list if key in stub])


def generate_imports(widgets):
    """Generate the import statements."""
    widget_types = {widget['type'] for widget in widgets}
    # Panel needed by all tabs
    widget_types.update(['Panel'])

    imports = ''

    if 'DataTable' in widget_types:
        widget_types.add('TableColumn')
        imports += ("""import pandas as pd\n""")

    if 'FileInput' in widget_types:
        imports += ("from io import BytesIO\n"
                    "import base64\n")

    if 'figure' in widget_types:
        widget_types.remove('figure')
        include_figure = True
    else:
        include_figure = False

    widget_types = sorted(list(widget_types))
    imports += ('from bokeh.models.widgets import ({0})'
                .format(',\n'
                        .ljust(36)
                        .join(widget_types)))

    if include_figure:
        imports += "\nfrom bokeh.plotting import figure"

    if include_figure or 'DataTable' in widget_types:
        imports += "\nfrom bokeh.models import ColumnDataSource"

    return imports


def generate_init(widget):
    """Generate code for the init method."""
    if widget['type'] == 'DataTable':
        text = ["""# Stub code for DataTable setup.""",
                """source = """
                """ColumnDataSource(pd.DataFrame({'x':[1], 'y':[2]}))""",
                """columns = [TableColumn(field='x', title='x_t'),""",
                """           TableColumn(field='y', title='y_t')]"""]
        arguments = ["""source=source""",
                     """columns=columns"""]

    else:
        text = []
        arguments = []

    text += ["""# {0}""".format(widget['description'])]

    if 'arguments' in widget:
        for k, v in widget['arguments'].items():
            if isinstance(v, str):
                arguments += ["""{0}=\"\"\"{1}\"\"\"""".format(k, v)]
            else:
                arguments += ["""{0}={1}""".format(k, v)]
    if arguments:
        arguments = '\n' + ',\n'.join([12*' ' + argument
                                       for argument in arguments])

    text += ['{0} = {1}({2})'.format(
                widget['attribute name'],
                widget['type'],
                arguments)]

    return '\n'.join([8*' ' + line for line in text])


def generate_setup(widget):
    """Generate code for the setup method."""
    if widget['callback']['method'] == 'on_click':
        return """{0}.{1}({2})""".format(
            widget['attribute name'],
            widget['callback']['method'],
            widget['callback']['callback method name'])
    elif widget['callback']['method'] == 'on_change':
        return """{0}.{1}("{2}", {3})""".format(
            widget['attribute name'],
            widget['callback']['method'],
            widget['callback']['attribute name'],
            widget['callback']['callback method name'])


def generate_callback(widget):
    """Generate the callback function text."""
    # Remove the self. if present
    methodname = widget['callback']['callback method name'].replace(
        'self.', '')

    text = """    # %%\n"""

    if widget['callback']['method'] == 'on_click':

        if 'attribute name' in widget['callback']:
            text += ("""    def {0}(self, {1}):\n"""
                     """        \"\"\"Callback method for the {2} """
                     """Bokeh attribute {3}.\"\"\"\n"""
                     """\n""".format(methodname,
                                     widget['callback']['attribute name'],
                                     widget['type'],
                                     widget['attribute name']))
        else:
            text += ("""    def {0}(self):\n"""
                     """        \"\"\"Callback method for the {1} """
                     """Bokeh attribute {2}.\"\"\"\n"""
                     """\n""".format(methodname,
                                     widget['type'],
                                     widget['attribute name']))
    elif widget['callback']['method'] == 'on_change':
        text += ("""    def {0}(self, attrname, old, new):\n"""
                 """        \"\"\"Callback method for the {1} """
                 """Bokeh attribute {2}.\"\"\"\n""".format(
                     methodname,
                     widget['type'],
                     widget['attribute name']))

    # FileInput specific code
    if widget['type'] == 'FileInput':
        text += (
            """        # File contents converted to a usable format.\n"""
            """        contents = BytesIO(base64.b64decode(\n"""
            """            {0}.value))\n\n""".format(widget['attribute name']))

    # Add rest of callback
    text += ("""        # This is stub code. Replace the line below """
             """with your code.\n"""
             """        self.update()"""
             """\n""")

    return text


# %%---------------------------------------------------------------------------
# GenerateCode
# -----------------------------------------------------------------------------
class GenerateCode():
    """Generates code for project based on specification file."""

    # %%
    def __init__(self, specificatiom):

        self.specification = specificatiom

        # Set up folder attributes
        model_folder = os.path.dirname(os.path.realpath(__file__))
        self.templates_folder = os.path.join(model_folder, 'templates')
        projects_folder = os.path.normpath(os.path.join(model_folder,
                                                        '../projects'))
        self.project_folder = generate_project_folder(
            folder_name=self.specification['project']['name'],
            folder_location=projects_folder)

        # Add class, filenames, attribute names, and callback names to
        # specification. Slightly easier to do it this way than
        # repeat it several places in the code.
        for tab in self.specification['tabs']:
            tab['classname'] = re.sub(r"[^A-Za-z]+", '', tab['name'].title())
            tab['filename_base'] = re.sub(r"[^A-Za-z]+",
                                          '',
                                          tab['name'].lower())
            for widget in tab['widgets']:
                widget['attribute name'] = ('self.' +
                                            re.sub(r"[^A-Za-z0-9]+",
                                                   '',
                                                   widget['name'].lower()))
                if 'callback' in widget:
                    widget['callback']['callback method name'] = (
                        'self.callback_' +
                        widget['attribute name'].replace('self.', ''))

    # %%
    def generate_miscellaneous(self):
        """Generate assorted miscellaneous files."""
        # Copy theme.yaml file
        shutil.copy2(os.path.join(self.templates_folder, 'theme.yaml'),
                     os.path.join(self.project_folder, 'theme.yaml'))

    # %%
    def generate_main(self):
        """Generate the main.py file and adds the static folder."""
        replacements = {}
        self._generate_base('main.txt', replacements,
                            'main.py', self.project_folder)

        # Create the static folder
        static_folder = os.path.join(self.project_folder, 'static')
        os.mkdir(static_folder)

    # %%
    def generate_model(self):
        """Generate the model.py file."""
        # Create the folder
        model_folder = os.path.join(self.project_folder, 'model')
        os.mkdir(model_folder)

        replacements = {}
        self._generate_base('model.txt', replacements,
                            'model.py', model_folder)

    # %%
    def generate_controller(self):
        """Generate the controller.py file."""
        # Create the folder
        controller_folder = os.path.join(self.project_folder, 'controller')
        os.mkdir(controller_folder)

        # Build the replacement dict
        imports = '\n'.join(
            ['from view.{0} import {1}'.format(tab['filename_base'],
                                               tab['classname'])
             for tab in self.specification['tabs']])

        tabs1 = '\n'.join(
            ["self.{0} = {1}(self)".format(tab['classname'].lower(),
                                           tab['classname'])
             for tab in self.specification['tabs']])

        tabs2 = ',\n'.ljust(25).join(
            ['self.{0}'.format(tab['classname'].lower())
             for tab in self.specification['tabs']])

        replacements = {'imports': imports,
                        'tabs1': tabs1,
                        'tabs2': tabs2}

        # Generate the file
        self._generate_base('controller.txt', replacements,
                            'controller.py', controller_folder)

    # %%
    def generate_views(self):
        """Generate the view files."""
        # Create the folder
        view_folder = os.path.join(self.project_folder, 'view')
        os.mkdir(view_folder)

        # Loop through each tab - one view file for each tab
        for tab in self.specification['tabs']:

            # Build the replacement dict
            # ==========================

            # Imports
            # -------
            imports = generate_imports(tab['widgets'])

            # init
            # ----
            # Used in the init method
            init = \
                ('\n'.join(
                    [generate_init(widget) for widget in tab['widgets']]))

            # Used in the init method - widget layout
            widget_names = ',\n'.ljust(41).join(
                [widget['attribute name'] for widget in tab['widgets']])

            # setup
            # -----
            # Callback function definitions used in the setup method
            # Only write code if there are callbacks, otherwise,
            # write a placeholder.
            setup = [generate_setup(widget) for widget in tab['widgets']
                     if 'callback' in widget]

            if not setup:
                setup = ["""# No widgets on this tab have a """
                         """callback, so this is an empty method.""",
                         """pass"""]
            else:
                setup = ["""# Setup the callbacks."""] + setup

            setup = '\n'.join([8*' '+line for line in setup])

            # callbacks
            # ---------
            # Create code for the callback functions, if they exist.
            callbacks = '\n\n'.join(
                [generate_callback(widget) for widget in tab['widgets'] if
                 'callback' in widget])
            if callbacks:
                callbacks = '\n\n' + callbacks

            # Replacment (code generation)
            # ----------------------------
            # Create the replacement dictionary
            replacements = {
                'imports': imports,
                'classname': tab['classname'],
                'class_description': tab['description'],
                'init': init,
                'widget_names': widget_names,
                'name': "'{0}'".format(tab['name']),
                'setup': setup,
                'callbacks': callbacks}

            # Generate the file
            self._generate_base('view.txt',
                                replacements,
                                tab['filename_base'] + '.py',
                                view_folder)

    # %%
    def _generate_base(self, template, replacements,
                       file, folder):
        """Generate the base for each file."""
        with open(os.path.join(self.templates_folder,
                               template)) as base_file:
            base_text = base_file.read()

        replacements['header'] = \
            generate_header_tail(self.specification['project'],
                                 ['copyright', 'legal notice'])
        replacements['metadata'] = \
            generate_metadata(self.specification['project'],
                              ['author', 'license'])
        replacements['project'] = self.specification['project']['name']
        replacements['description'] = \
            self.specification['project']['description']
        replacements['author'] = self.specification['project']['author']
        replacements['creation_date'] = datetime.now().strftime("%Y-%m-%d")

        text_out = Template(base_text).substitute(replacements)

        with open(os.path.join(folder, file), 'w') as out_file:
            out_file.write(text_out)
