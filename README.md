#py-shstr

This is a Python3 module that allows shell-like string interpolation on python:

```python3
name = "Gus"
print ( pyshstr("Hello $name!") )
>>> Hello Gus!
```

###Usage
Its really simple:

 1. Import pyshstr
 2. Create some variables 
 3. call pyshstr.shstr with your string containing variables

```python3
import pyshstr
name = "Gus"
print ( pyshstr.shstr("Hello $name!") )
>>> Hello Gus!
```

#### Variables
Variables within a string should be of the form: $**varname** where **varname** is any alphanumeric (0-9a-zA-Z_) valid python variable name. 

Variables can be **local** or **global**. You can disable global lookuo with the **allow_globals** option.
If a variable is not found in the scope there are 3 possible actions:

 1. **ignore**: Do not change the missing variable. This will leave the $**varname** in the string. (Default)
 2. **blank**: Replace the $**varname** in the string with an empty string (this is what a linux shell would do
 3. **doexcept**: Raise an exception. By defalt this will be a **pyshstr.VarnameMissingError** but you can override it with the **custom_error** option

#### Config (Options)
The Config class defines the behavior of pyshstr. This can be altered as such:
```python3
pyshstr.Config.option = value
```

Current options are:


| Option name |  Purpose | Values | Default | 
| -------------- | -------------------------------- | ------------- | ------------ |
| `missing_action` | What will happend when a variable is not found | `pyshstr.MissingActions.ignore`, `pyshstr.MissingActions.blank` or `pyshstr.MissingActions.doexcept` | `pyshstr.MissingActions.ignore` |
| `allow_globals` | Whether or not to look for variables on the global scope  | `True` or `False` | `True` |
| `regex` | The regex used to identify variable names in the string | A Python compiled re object | `re.compile("\$(\w+)")` | 
| `custom_error` | The Exception to raise if a variable isn't found and MissingActions is set to MissingActinos.doexcept | Any python Exception class | `pyshstr.VarnameMissingError` |
| `debug` | Prints debugginf messages | `True` or `False` | `False` |



###But why would I want that?

I love python and I don't like Perl but Perl has strign interpolations just like bash and I really really like  that. This is specially useful for me because in my job I generate a lot of text with a lot of interpolated variables within. 

Yes, you can do this in normal python right?

```python3
name = "Gus"
print ( "Hello %s!" %s )
>>> Hello Gus!
```

But thats one variable, what about this?

```python3
a = "There"
b = "Are"
c = "Too"
d = "Many"
e = "Variables"
f = "In"
g = "Here"
#print ( "OMG %s %s %s %s %s %s %s!" % (a, b, c, d, e, f, g) ) # This is confusing, maybe we should use a dict

print ( "OMG %(a)s %(b)s %(c)s %(d)s %(e)s %(f)s %(g)s!" % {"a":a, "b":b, "c":c, "d":d, "e":e, "f":f, "g":g}  ) # OMG what a mess!

>>> OMG There Are Too Many Variables In Here!

```
Not so easy now huh? Thats what this module does. 

```python3
import pyshstr

a = "There"
b = "Are"
c = "Too"
d = "Many"
e = "Variables"
f = "In"
g = "Here"
print ( pyshstr.shstr("OMG $a $b $c $d $e $f $g"))
>>> OMG There Are Too Many Variables In Here!

```

"But I could do that a little simpler with **locals()** " you say. 
Yes. Yes you can but with pyshstr you can also:

 - Interpolate **local** and **global** variables
 - Set which action to do if a variable is missing
 - Customize the format of the variables in the strings
 - **TO-DO**: Interpolate function-returns

## Important note:

It looks like this is such an useful thing Python is going to make it native from **python 3.6** (https://www.python.org/dev/peps/pep-0498/). So maybe this module will be useful only if you are stuck in < 3.6 
Anyhow, it's free. 

