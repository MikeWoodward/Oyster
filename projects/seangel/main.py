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
from controller.controller import Controller


# %%---------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
# This code is called by the Bokeh server.
# No if __name__ here because of the way that Bokeh works.
controller = Controller()
controller.setup()
# display must be called after setup or else callbacks don't work
controller.display()
controller.update()
