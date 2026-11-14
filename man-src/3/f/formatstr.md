---
title: "formatstr(3)"
name: "formatstr"
section: "3"
letter: "f"
url: "/docs/linux/man/3-formatstr/"
description: "formatstr – String Formatter object"
---

<h2>NAME</h2>
<p> formatstr &#8211; String Formatter object</p>
<h2>DESCRIPTION</h2>
<p> Object used to format base objects into strings. It extends the functionality of the string Formatter object to include new modifiers for different objects. Some of these new modifiers include conversion of strings into a sequence of hex characters, conversion of strings to their corresponding CRC32 or CRC16 representation.</p>
<h2>CLASSES</h2>
<h3>class FormatStr(string.Formatter)</h3>
<pre><code>
String Formatter object
FormatStr()
    -&gt;New string formatter object
    Usage : from formatstr import FormatStr
            x = FormatStr()
    out = x.format(fmt_spec, *args, **kwargs)
              out = x.vformat(fmt_spec, args, kwargs)
                        Arguments should be surrounded by curly braces{},
            anything that is
            not contained in curly braces is considered literal text which is
            copied unchanged to the output.Positional arguments to be used in the format spec are specified
            by their index : {0},
            {1}, etc.Named arguments to be used in the format spec are specified by their name : {name1}, {name2}, etc.Modifiers are specified after the positional index or name preceded by a ":", "{0:#x}" --display first positional argument in hex Examples :
#Format string using positional arguments
    out = x.format("{0} -&gt; {1}", a, b)
#Format string using named arguments
              out = x.format("{key}: {value}", key = "id", value = 32)
#Format string using both positional and named arguments
                        out = x.format("{key}: {value}, {0}, {1}", a, b, key = "id", value = 32)
#Use vformat() method instead when positional arguments are given
#as a list and named arguments are given as a dictionary
#The following examples show the same as above
                                  pos_args = [ a, b ] named_args = {"key" : "id", "value" : 32} out = x.vformat("{0} -&gt; {1}", pos_args) out = x.vformat("{key}: {value}", named_args) out = x.vformat("{key}: {value}, {0}, {1}", pos_args, named_args)
#Convert string into hex
                                                                                                                                                                                                out = x.format("{0:x}", "hello") #out = "68656c6c6f"
#Convert string into hex with leading 0x
    out = x.format("{0:#x}", "hello") #out = "0x68656c6c6f"
#Convert string into crc32
    out = x.format("{0:crc32}", "hello") #out = "0x3610a686"
#Convert string into crc16
    out = x.format("{0:crc16}", "hello") #out = "0x9c62"
#Substring using "@" format modifier
#Format{0 : @sindex[, eindex] } is like value[sindex : eindex]
#{0 : @3 } is like value[3 : ]
#{0 : @3, 5 } is like value[3 : 5]
#{0 : .5 } is like value[ : 5]
    out = x.format("{0:@3}", "hello") #out = "lo" out = x.format("{0:.2}", "hello") #out = "he"
#Integer extension to display umax name instead of the value
#Format : {0 : max32 | umax32 | max64 | umax64 }
#Output : if value matches the largest number in format given,
#the max name is displayed, else the value is displayed
    out = x.format("{0:max32}", 0x7fffffff) #out = "max32" out = x.format("{0:max32}", 35) #out = "35"
#Number extension to display the value with units
#Format : {0 : units[.precision] }
#Output : convert value to a string with units, by default
#precision = 2 and all trailing zeros are removed.
#To force the precision use a negative number.
    out = x.format("{0:units}", 1024) #out = "1KB" out = x.format("{0:units.4}", 2000) #out = "1.9531KB" out = x.format("{0:units.-2}", 1024) #out = "1.00KB"
#Date extension for int, long or float
#Format : {0 : date[ : datefmt] }
#The spec given by datefmt is converted using strftime()
#The conversion spec "%q" is used to display microseconds
#Output : display value as a date
    stime = 1416846041.521868 out = x.format("{0:date}", stime) #out = "Mon Nov 24 09:20:41 2014" out = x.format("{0:date:%Y-%m-%d}", stime) #out = "2014-11-24"
#List format specification
#Format : {0 [[ : listfmt] : itemfmt] }
#If one format spec, it is applied to each item in the list
#If two format specs, the first is the item separator and
#the second is the spec applied to each item in the list
    alist = [ 1, 2, 3, 0xffffffff ] out = x.format("{0:umax32}", alist) #out = "[1, 2, 3, umax32]" out = x.format("{0:--:umax32}", alist) #out = "1--2--3--umax32" Methods defined here : -- -- -- -- -- -- -- -- -- -- -format_field(self, value, format_spec) Override original method to include modifier extensions get_value(self, key, args, kwargs)
Override original method to return "" when the positional argument or named argument does not exist : x.format("0:{0}, 1:{1}, arg1:{arg1}, arg2:{arg2}", a, arg1 = 11)
                                                                                                          the{1} will return "" since there is only one positional argument
                                                                                                              the{arg2} will return "" since arg2 is not a named argument
</code></pre>
<h2>FUNCTIONS</h2>
<h3>crc16(value)</h3>
<p> Convert string to its crc16 representation</p>
<h3>crc32(value)</h3>
<p> Convert string to its crc32 representation</p>
<h3>hex(value)</h3>
<p> Convert string to its hex representation</p>
<h3>int_units(value)</h3>
<p> Convert string value with units to an integer </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>value:</code></p>
<dd> String to convert</dl>
</dl>
<dl>
<dt>
<dd>
<p> Examples:</dl>
<h3>out = <a href="//www.systutorials.com/docs/linux/man/1MB-num_units/">num_units</a>(1MB) # out = 1048576</h3>
<h3>str_units(value, precision=2)</h3>
<p> Convert number to a string value with units </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>value:</code></p>
<dd> Number to convert</p>
<dt><code>precision:</code></p>
<dd> Return string value with the following floating point precision. By default no trailing zeros are returned but if the precision is given as a negative number the precision is enforced [default: 2]</dl>
</dl>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
