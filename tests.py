#!/bin/python3

import unittest
import pyshstr

class TestRegularReplacements(unittest.TestCase):
    
    def test_single_variable(self):
        text = "Hello $name!"
        name = "world"        
        self.assertEqual("Hello world!", pyshstr.shstr(text))

    def test_multiple_varibles(self):
        text = "Hello $name, $optional_message. My favourite numebr is: $number"
        name = "Gustavo"
        optional_message = "how are you?"
        number = "5"
        self.assertEqual("Hello Gustavo, how are you?. My favourite numebr is: 5", pyshstr.shstr(text))
        
    def test_non_strings(self):
        import datetime
        text = "Current date: $date"
        date = datetime.datetime.now()
        self.assertEqual("Current date: %s" % str(date), pyshstr.shstr(text))
        
    def test_non_strings2(self):
        text = "$number is Five"
        number = 5
        self.assertEqual("5 is Five", pyshstr.shstr(text))
        
class TestMissingVariables(unittest.TestCase):
    
    def test_blank(self):
        pyshstr.Config.missing_action = pyshstr.MissingActions.blank
        text = "This $var is missing"
        self.assertEqual("This  is missing", pyshstr.shstr(text))
        
    def test_ignore(self):
        pyshstr.Config.missing_action = pyshstr.MissingActions.ignore
        text = "This $var is missing"
        self.assertEqual("This $var is missing", pyshstr.shstr(text))

    def test_doexcept(self):
        pyshstr.Config.missing_action = pyshstr.MissingActions.doexcept
        text = "This $var is missing"
        with self.assertRaises(pyshstr.VarnameMissingError):
            pyshstr.shstr(text)

name = "world"
class TestConfigOptions(unittest.TestCase):
    
    def test_allow_globals(self):
        pyshstr.Config.allow_globals = True
        text="Hello $name!"
        self.assertEqual("Hello world!", pyshstr.shstr(text))
    
    def test_disallow_globals(self):
        pyshstr.Config.custom_error = pyshstr.VarnameMissingError
        pyshstr.Config.allow_globals = False
        pyshstr.Config.missing_action = pyshstr.MissingActions.doexcept
        text="Hello $name!"
        with self.assertRaises(pyshstr.VarnameMissingError):
            pyshstr.shstr(text)
            
    def test_custom_error(self):
        class CustomError(Exception):
            pass
        
        pyshstr.Config.custom_error = CustomError
        pyshstr.Config.missing_action = pyshstr.MissingActions.doexcept
        
        text="This variable is not declared: $non_existing"
        with self.assertRaises(CustomError):
            pyshstr.shstr(text)
        
    def test_custom_regex(self):
        pass

if __name__ == '__main__':
    unittest.main()

    

