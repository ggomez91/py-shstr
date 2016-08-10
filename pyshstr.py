#!/bin/python3

import re
import inspect
from enum import Enum

class MissingActions(Enum):
    ignore      =  0  
    blank       =  1
    doexcept    =  2


class VarnameMissingError (NameError):
    pass
    
class Config:
    missing_action      =  MissingActions.ignore
    allow_globals       =  True
    regex               =  re.compile("\$(\w+)")
    custom_error        =  VarnameMissingError
    debug               =  False



def debug (msg):
    if Config.debug:
        print ("\033[93m[debug]\t{}\033[00m".format(msg))
    
def _replace(string, varname, value):
    return string.replace("$"+varname, str(value))
  
def shstr (string):
    for varname in Config.regex.findall(string):

        try:
            frame = inspect.currentframe()
            
            debug ("Looking for '%s' in local namespace" % varname)
            value = frame.f_back.f_locals.get(varname) 
            if value: debug ("Value found") 
            
            # If var is None and global search is allowed, look in the global namespace
            if  value is None and Config.allow_globals:
                debug ("Looking for '%s' in global namespace" % varname)
                value = frame.f_back.f_globals.get(varname) 
                if value: debug ("Value found")
            
            # if value wasn't found yet, check the missing action to do. 
            if value is None:
                if Config.missing_action == MissingActions.ignore:
                    pass 
                elif Config.missing_action == MissingActions.blank:
                    pass 
                elif Config.missing_action == MissingActions.doexcept:
                    raise Config.custom_error(varname)
                
        finally:
            del frame

        if value:
            string = _replace(string, varname, value)
        
        # is the value is missing and the action is to blank, set ""
        elif Config.missing_action == MissingActions.blank:
            string = _replace(string, varname, "")
        
        # No need to code for 'ignore' action. 
            
    return string


