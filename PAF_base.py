# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:22:29 2021

@author: shane
"""

from admin import read_json, select_thing
from pdfops import write_fillable_pdf
import os

fields=['Departments', 'Program', #cjr
 'First Name', 'Last Name', 'Initial_4', 'EmplID', 'No', 'Street', 'Apt', #cjr
 'City', 'State', 'Zip Code', 'Phone Number', #cjr
 'TitleRank', 'Functional Title', #cjr but can be updated
 'CUNYfirst Position', 'Line', #cjr but can be updated... based on pos num file?
 'Action', 'Reason',    #from user input + hr guide file
 'Effective Date', 'Or Effective Period Starting', 'and Ending', #from user input
 'Salary amount', 'Salary', 'Per Annum', 'Fraction of Annual Rate', #from user input
 'Remarks','idfield'] #from user input + HR Guide actions, from os count
#Phase 1 - determine what type of operation 
#single, multi-person, multi-action, or multi-person,multi-action (pattern)
template=r'Y:\Templates\Autotemplates\Personnel Action Form.pdf'
def phase1():
    options=['Single - One PAF describing one action for one employee',
         'Multi-Action - PAFs describing multiple actions for one employee',
         'Multi-person - PAFs describing one action for multiple employees',
         'Pattern - PAFS describing the same set of actions for multiple employees']
    selections={l:x for l,x in zip([i.split(' - ')[0] for i in options],['00','10','01','11'])}
    
    selection=select_thing(options).split(' - ')[0]
    return(selections[selection])
#Phase 2 - identify person or persons based on several criteria
#fuzzy name lookup, emplid, category of staff, department, etc
def matching_criteria(criteria):
    if criteria in critdict:    #simple json lookup
        category=critdict[criteria] #returns appropriate json location
    return(read_json(category))
def efficient_search(selection,dictionary):
    
    searchstr=input(
            f"Please type a portion of the {selection} for this search:\n"
            )
    newdict={k:dictionary[k] for k in dictionary.keys() if searchstr in k}
    print("These are your results:")
    selection=select_thing([k for k in newdict.keys()])
    return(newdict[selection])
    
def select_person():
    #this is where we look for at least one person
    #perhaps using some sort of lookup?
    #idk figure it out, shane
    options=['Name','Emplid','Category of Staff','Title','Department'] #need data source here
    selection=select_thing(options)
    searchdict=matching_criteria(selection)
        
    return(persondict)

def phase2(inst_str:str):   #accepts instruction string from phase1
    
    
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