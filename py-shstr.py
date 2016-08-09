#!/bin/python3

import re
import inspect

regex = re.compile("\$(\w+)")
def shstr (string):
	for varname in regex.findall(string):
		print ("VAR:"+varname)
		
		try:
			frame = inspect.currentframe()
			value = frame.f_back.f_locals.get(varname, "")
		finally:
			del frame
			
		
		print ("VAL:"+str(value))
		string = string.replace("$"+varname, value)
	return string
	
nombre = "Gus" 
string = "Hola $nombre, $mensaje?" 

modified = shstr(string)
print ("MOD:"+modified)

def sub():
	nombre="Juan"
	print ( shstr("Hola $nombre"))
	
sub() 
