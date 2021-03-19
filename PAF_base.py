# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:22:29 2021

@author: shane
"""

#Phase 1 - determine what type of operation 
#single, multi-person, multi-action, or multi-person,multi-action (pattern)

#Phase 2 - identify person or persons based on several criteria
#fuzzy name lookup, emplid, category of staff, department, etc

#Phase 3 - population of additional data
#Effective dates (mandatory, even in declaring lack of knowledge)
#Comments (optional)

#Phase 4 - Filling in PDF document
#fil in fields, create CF action list to append to document, UUID embedding

#Phase 5 - File creation (on a shared drive) and monitoring/ communications

#TODO identify fields on current PAF. 
#TODO create PAF template for use and copy into y:/autotemplates/
#TODO evaluate existing PDF writing module to determine general utility
#TODO Gather data from HR Guide 
#(action/reasons, CF action/reasons, action type groups, appropriate categories of staff)
#TODO codify HR Guide data into json and store in y:/program data/
#TODO Build skeleton of process out 
#something like pick action type, pick person, pick action subtype?, print to pdf
#TODO wrap skeletal process in selection process similar to repo_helper
#TODO test repeatedly
#TODO implement GUI wrapper