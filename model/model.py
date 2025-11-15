#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 17:35:01 28-Jun-2020

Author: Mike Woodward

Project: oyster

This code is licensed under the MIT license.
"""

# %%---------------------------------------------------------------------------
# Module metadata
# -----------------------------------------------------------------------------
__author__ = "Mike Woodward"
__license__ = "MIT"

# %%---------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from copy import deepcopy
import glob
import json
from json.decoder import JSONDecodeError
import os
from jsonschema import (validators,
                        ValidationError,
                        SchemaError,
                        Draft7Validator)
try:
    from model.generatecode import GenerateCode
except ModuleNotFoundError:
    from generatecode import GenerateCode    

# %%---------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def extend_with_default(validator_class):
    """Code adds defaults to specification file."""
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        for property_, subschema in properties.items():

            if "default" in subschema:
                instance.setdefault(property_, deepcopy(subschema["default"]))

        for error in validate_properties(validator,
                                         properties,
                                         instance,
                                         schema):
            yield error

    return validators.extend(
        validator_class, {"properties" : set_defaults},
    )


# %%---------------------------------------------------------------------------
# Method decorators
# -----------------------------------------------------------------------------
def reset_error(func):
    """Resets the error attributes."""
    def wrapper(self, *arg, **kw):
        self.error = False
        self.error_string = ""
        return func(self, *arg, **kw)
    return wrapper


# %%---------------------------------------------------------------------------
# Model
# -----------------------------------------------------------------------------
class Model():
    """Class Model is part of the model-view-controller architecture. It
    contains the data model - the data used in the application."""

    # %%
    def __init__(self):
        """Method initializes object. First part of two-part initialization."""
        self.error = False
        self.error_string = ""

        self.schemas_folder = None
        self.specification = None

    # %%
    @reset_error
    def setup(self):
        """Method sets up object. Second part of two-part initialization.
        Does intialization that's more likley to fail."""

        # Set up folder attributes
        model_folder = os.path.dirname(os.path.realpath(__file__))
        self.schemas_folder = os.path.join(model_folder, 'schemas')

        # Look for schema json files in the schemas folder.
        schema_files = glob.glob(os.path.join(self.schemas_folder,
                                              'schema*.json'))

        if not schema_files:
            self.error = True
            self.error_string = \
                ("""Could not find any schema files on server.""")
            return []

        # Remove the folder name and the .json suffix and sort in descending
        # order
        schema_names = [os.path.basename(x)[:-5] for x in schema_files]
        schema_names.sort(reverse=True)

        return schema_names

    # %%
    @reset_error
    def verify(self,
               specification_filename,
               specification_contents,
               schema_name):
        """Verifies the JSON files."""

        # Load the schema
        # ---------------

        # Re-create the full schema filename
        schema_filename = os.path.join(
            self.schemas_folder,
            schema_name + '.json')

        # Attempt to open the schema file
        if not os.path.isfile(schema_filename):
            self.error = True
            self.error_string = ("""The schema {0} doesn't exist in """
                                 """the model folder on the server. This """
                                 """means the """
                                 """specification file can't be checked. """
                                 """To fix the problem, put the JSON """
                                 """schema file in the model folder."""
                                 .format(schema_name))
            return

        # Load the JSON
        with open(schema_filename, 'r') as schema_file:
            try:
                _schema = json.load(schema_file)
            except JSONDecodeError as error:
                self.error = True
                self.error_string = ("""JSON error in JSON schema """
                                     """{0}. The JSON error is '{1}' it """
                                     """occurred on line {2} on column """
                                     """{3}.""".format(schema_name,
                                                       error.msg,
                                                       error.lineno,
                                                       error.colno))
                return

        # Validate the JSON is a schema
        try:
            Draft7Validator.check_schema(_schema)
        except SchemaError as error:
            self.error = True
            self.error_string = ("""Schema {0} failed the schema validation """
                                 """check. The best next step is to check """
                                 """the schema with an online JSON schema """
                                 """validator.""".format(
                                     schema_name))
            return

        # JSON specification
        # ------------------

        # Process the JSON string as a JSON object
        try:
            self.specification = json.loads(specification_contents)
        except JSONDecodeError as error:
            self.error = True
            self.error_string = ("""JSON error in the JSON specification """
                                 """{0}. The JSON error is '{1}' it """
                                 """occurred on line {2} on column """
                                 """{3}.""".format(specification_filename,
                                                   error.msg,
                                                   error.lineno,
                                                   error.colno))
            return

        # Validate the specification against the schema
        # ---------------------------------------------

        try:
            # Validate the JSON, but add defaults to the specification.
            # Code comes from:
            # https://python-jsonschema.readthedocs.io/en/stable/faq/?highlight=default#why-doesn-t-my-schema-s-default-property-set-the-default-on-my-instance
            DefaultValidatingDraft7Validator =\
                extend_with_default(Draft7Validator)
            # Note jsonschem.validate(obj, schema,
            #                         cls=DefaultValidatingDraft7Validator)
            # will not work because the metaschema contains `default`
            # directives.
            DefaultValidatingDraft7Validator(
                _schema).validate(self.specification)
        except SchemaError as error:
            self.error = True
            self.error_string = ("""Schema {0} failed schema validation """
                                 """check. """
                                 """The first context is {1}.""".format(
                                     schema_name,
                                     error.context[0]))
        except ValidationError as error:
            self.error = True
            messages = '\n'.join([dummy.message for dummy in error.context])
            self.error_string = ("""The JSON specification file {0} """
                                 """failed the schema validation check """
                                 """against schema {1} """
                                 """with error messages:\n{2}."""
                                 .format(specification_filename,
                                         schema_name,
                                         messages))
            return


    # %%
    @reset_error
    def generate(self):
        """Generates source code from the specification"""

        generator = GenerateCode(self.specification)
        generator.generate_main()
        generator.generate_model()
        generator.generate_controller()
        generator.generate_views()
        generator.generate_miscellaneous()


# %%
# Code to test the model
if __name__ == "__main__":

    model = Model()
    schemas = model.setup()

    if model.error:
        print(model.error_string)
        import sys
        sys.exit()
    schema = schemas[0]

    specification_filename = "silkworm.json"
    specification_file = open("../projects/{0}".format(
        specification_filename), 'r')
    specification_contents = specification_file.read()

    model.verify(specification_filename,
                 specification_contents,
                 schema)
    if model.error:
        print(model.error_string)
        import sys
        sys.exit()

    model.generate()
