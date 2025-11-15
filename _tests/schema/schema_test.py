#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:54:10 2020

@author: mikewoodward
"""

import json
from json.decoder import JSONDecodeError
from jsonschema import validate, ValidationError, SchemaError, Draft7Validator
import os.path
import sys

SCHEMA_FILE_NAME = "address_schema.json"
CHECK_FILE_NAME = 'address.json'

def read_in_json(filename):
    
    with open(filename, 'r') as json_file:
        try:
            json_data = json.load(json_file)
        except JSONDecodeError as error:
            error_string = ("""JSON error in JSON file """
                                 """{0}. The JSON error is '{1}' it """
                                 """occurred on line {2} on column """
                                 """{3}.""".format(filename,
                                                   error.msg, 
                                                   error.lineno,
                                                   error.colno))
            print(error_string)
            quit()
        
        print("JSON {0} read in - no JSON errors".format(filename))

    return json_data
        

schema_json = read_in_json(SCHEMA_FILE_NAME)

try:
    Draft7Validator.check_schema(schema_json)
except SchemaError as error:
    error_string = ("""Schema {0} failed validation check. """
                    """The first context is {1}.""".format(
                        SCHEMA_FILE_NAME,
                        error.context[0]))
    print(error_string)
    sys.exit()

check_json = read_in_json(CHECK_FILE_NAME)

try:
    validate(instance=check_json, schema=schema_json)
except SchemaError as error:
    error_string = ("""Schema {0} failed validation check. """
                    """The first context is {1}.""".format(
                        SCHEMA_FILE_NAME,
                        error.context[0]))
    print(error_string)
except ValidationError as error:
    error_string = ("""The JSON specification file {0} """
                         """failed the schema validation check """
                         """with an error message "{1}". The """
                         """instance the validator was checking """
                         """was {2}."""
                         .format(CHECK_FILE_NAME,
                                 error.message,
                                 error.instance))
    print(error_string)