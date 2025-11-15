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
from controller.controller import Controller


# %%---------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
# This code is called by the Bokeh server.
# "No if __name__ here because of the way that Bokeh works.
controller = Controller()
controller.setup()
controller.display()
