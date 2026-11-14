---
title: "baseobj(3)"
name: "baseobj"
section: "3"
letter: "b"
url: "/docs/linux/man/3-baseobj/"
description: "baseobj – Base object"
---

<h2>NAME</h2>
<p> baseobj &#8211; Base object</p>
<h2>DESCRIPTION</h2>
<p> Base class so objects will inherit the methods providing the string representation of the object and methods to change the verbosity of such string representation. It also includes a simple debug printing and logging mechanism including methods to change the debug verbosity level and methods to add debug levels.</p>
<h2>CLASSES</h2>
<h3>class BaseObj(__builtin__.object)</h3>
<pre><code>
Base class so objects will inherit the methods providing the string
representation of the object and a simple debug printing and logging
mechanism.
Usage:
    from baseobj import BaseObj
#Named arguments
    x = BaseObj(a=1, b=2)
#Dictionary argument
    x = BaseObj({'a':1, 'b':2})
#Tuple arguments : first for keys and second for the values
    x = BaseObj(['a', 'b'], [1, 2])
#All of the above will create an object having two attributes:
    x.a = 1 and x.b = 2
#Add attribute name, this will be the only attribute to be displayed
    x.set_attrlist("a")
#Add list of attribute names to be displayed in that order
    x.set_attrlist(["a", "b"])
#Set attribute with ordered display rights
    x.set_attr("a", 1)
#This is the same as
    setattr(x, "a", 1) or x.a = 1
    x.set_attrlist("a")
#Set attribute with switch duplicate
#The following creates an extra attribute "switch" with
#the same value as attribute "a":
#x.a == x.switch
#x.a is x.switch
    x.set_attr("a", 1, switch=True)
#Make the current object flat by allowing all the attributes
#for the new attribute to be accessed directly by the current
#object so the following is True:
#x.d == x.c.d
    x.set_attr("c", BaseObj(d=11, e=22), switch=True)
#Set the comparison attribute so x == x.a is True
    x.set_eqattr("a")
#Set verbose level of object's string representation
    x.debug_repr(level)
#Set string format for verbose level 1
    x.set_strfmt(1, "arg1:{0}")
#In the above example the first positional argument is "a"
#so the str(x) gives "arg1:1"
#Set attribute shared by all instances
#If a global or shared attribute is set on one instance,
#all other instances will have access to it:
#y = BaseObj(d = 2, e = 3)
#then the following is true
#x.g == y.g
#x.g is y.g
    x.set_global("g", 5)
#Set level mask to display all debug messages matching mask
    x.debug_level(0xFF)
#Add a debug mapping for mask 0x100
    x.debug_map(0x100, 'opts', "OPTS: ")
#Set global indentation to 4 spaces for dprint
    x.dindent(4)
#Set global indentation to 4 spaces for displaying objects
    x.sindent(4)
#Set global truncation to 64 for displaying string objects
    x.strsize(64)
#Do not display timestamp for dprint messages
    x.tstamp(enable=False)
#Change timestamp format to include the date
    x.tstamp(fmt="{0:date:%Y-%m-%d %H:%M:%S.%q} ")
#Get timestamp if enabled, else return an empty string
    out = x.timestamp()
#Open log file
    x.open_log(logfile)
#Close log file
    x.close_log()
#Write data to log file
    x.write_log(data)
#Format the given arguments
    out = x.format("{0:x} - {1}", 1, "hello")
#Format the object attributes set by set_attrlist()
    out = x.format("{0:x} - {1}")
#Print debug message only if OPTS bitmap matches the current
#debug level mask
    x.dprint("OPTS", "This is an OPTS debug message")
Methods defined here:
---------------------
__eq__(self, other)
Comparison method: this object is treated like the attribute
defined by set_eqattr()
__getattr__(self, attr)
Return the attribute value for which the lookup has not found
the attribute in the usual places. It checks the internal
dictionary for any attribute references, it checks if this
is a flat object and returns the appropriate attribute.
And finally, if any of the attributes listed in _attrlist
does not exist it returns None as if they exist but not
defined
__init__(self, *kwts, **kwds)
Constructor
Initialize object's private data according to the arguments given.
Arguments can be given as positional, named arguments or a
combination of both.
__ne__(self, other)
Comparison method: this object is treated like the attribute
defined by set_eqattr()
__repr__(self)
String representation of object
The representation depends on the verbose level set by debug_repr().
If set to 0 the generic object representation is returned, else
the representation of the object includes all object attributes
and their values with proper indentation.
__str__(self)
Informal string representation of object
The representation depends on the verbose level set by debug_repr().
If set to 0 the generic object representation is returned, else
the representation of the object includes all object attributes
and their values.
close_log(self)
Close log file.
debug_level(self, level=0)
Set debug level mask.

level:
Level to set. This could be a number or a string expression
of names defined by debug_map()



Examples:
#Set level
    x.debug_level(0xFF)
#Set level using expression
    x.debug_level('all')
    x.debug_level('debug ^ 1')

dprint(self, level, msg, indent=0)
Print debug message if level is allowed by the verbose level
given in debug_level().
format(self, fmt, *kwts, **kwds)
Format the arguments and return the string using the format given.
If no arguments are given either positional or named then object
attributes set by set_attrlist() are used as positional arguments
and all object attributes are used as named arguments

fmt:
String format to use for the arguments, where {0}, {1}, etc.
are used for positional arguments and {name1}, {name2}, etc.
are used for named arguments given after fmt.


open_log(self, logfile)
Open log file.
set_attr(self, name, value, switch=False)
Add name/value as an object attribute and add the name to the
list of attributes to display

name:
Attribute name
value:
Attribute value


set_attrlist(self, attr)
Add list of attribute names in object to display by str() or repr()

                                                                 attr : Name
                                                                        or
                                                                        list of names to add to the list of attribute names
                                                                        to display

                                                                        set_eqattr(self, attr)
Set the comparison attribute

attr:
Attribute to use for object comparison



Examples:
    x = BaseObj(a=1, b=2)
    x.set_eqattr("a")
    x == 1 will return True, the same as x.a == 1

set_global(self, name, value)
Set global variable.
set_strfmt(self, level, format)
Save format for given display level

level:
Display level given as a first argument
format:
String format for given display level, given as a second argument


Static methods defined here:
----------------------------
debug_map(bitmap, name='', disp='')
Add a debug mapping.
Generic debug levels map
  &lt;bitmap&gt;  &lt;name&gt;  &lt;disp prefix&gt;
   0x000    'none'
   0x001    'info'  'INFO: ' # Display info messages only
   0x0FF    'debug' 'DBG:  ' # Display info and all debug messages (0x02-0x80)
  &gt;0x100    user defined verbose levels
debug_repr(level=None)
Return or set verbose level of object's string representation.
When setting the verbose level, return the verbose level before
setting it.

level:
Level of verbosity to set



Examples:
#Set verbose level to its minimal object representation
    x.debug_repr(0)
#Object representation is a bit more verbose
    x.debug_repr(1)
#Object representation is a lot more verbose
    x.debug_repr(2)

dindent(indent=None)
Set global dprint indentation.
flush_log()
Flush data to log file.
sindent(indent=None)
Set global object indentation.
strsize(size)
Set global string truncation.
timestamp(fmt=None)
Return the timestamp if it is enabled.

fmt:
Timestamp format, default is given by the format
set by tstamp()


tstamp(enable=None, fmt=None)
Enable/disable timestamps on dprint messages and/or
set the default format for timestamps

enable:
Boolean to enable/disable timestamps
fmt:
Set timestamp format


write_log(data)
Write data to log file.
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-formatstr/">formatstr</a>(3)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
