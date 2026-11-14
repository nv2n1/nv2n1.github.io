---
title: "tcl_getboolean(3)"
name: "tcl_getboolean"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_getboolean/"
description: "Tcl_GetInt, Tcl_GetDouble, Tcl_GetBoolean – convert from string to integer, double, or boolean"
---

<p>Tcl_GetInt, Tcl_GetDouble, Tcl_GetBoolean &#8211; convert from string to integer, double, or boolean </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_GetInt</code>(<i>interp, src, intPtr</i>)
int
<code>Tcl_GetDouble</code>(<i>interp, src, doublePtr</i>)
int
<code>Tcl_GetBoolean</code>(<i>interp, src, boolPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>const char <i>*src</i> (in) Textual value to be converted.</p>
<dd>int <i>*intPtr</i> (out) Points to place to store integer value converted from <i>src</i>.</p>
<dd>double <i>*doublePtr</i> (out) Points to place to store double-precision floating-point value converted from <i>src</i>.</p>
<dd>int <i>*boolPtr</i> (out) Points to place to store boolean value (0 or 1) converted from <i>src</i>. </p>
</dl>
<h2>Description</h2>
<p>These procedures convert from strings to integers or double-precision floating-point values or booleans (represented as 0- or 1-valued integers). Each of the procedures takes a <i>src</i> argument, converts it to an internal form of a particular type, and stores the converted value at the location indicated by the procedure&#8217;s third argument. If all goes well, each of the procedures returns <code>TCL_OK</code>. If <i>src</i> does not have the proper syntax for the desired type then <code>TCL_ERROR</code> is returned, an error message is left in the interpreter&#8217;s result, and nothing is stored at *<i>intPtr</i> or *<i>doublePtr</i> or *<i>boolPtr</i>. </p>
<p> <code>Tcl_GetInt</code> expects <i>src</i> to consist of a collection of integer digits, optionally signed and optionally preceded by white space. If the first two characters of <i>src</i> after the optional white space and sign are &#8220;0x&#8221; then <i>src</i> is expected to be in hexadecimal form; otherwise, if the first such character is &#8220;0&#8221; then <i>src</i> is expected to be in octal form; otherwise, <i>src</i> is expected to be in decimal form. </p>
<p> <code>Tcl_GetDouble</code> expects <i>src</i> to consist of a floating-point number, which is: white space; a sign; a sequence of digits; a decimal point; a sequence of digits; the letter &#8220;e&#8221;; a signed decimal exponent; and more white space. Any of the fields may be omitted, except that the digits either before or after the decimal point must be present and if the &#8220;e&#8221; is present then it must be followed by the exponent number. </p>
<p> <code>Tcl_GetBoolean</code> expects <i>src</i> to specify a boolean value. If <i>src</i> is any of <code>0</code>, <code>false</code>, <code>no</code>, or <code>off</code>, then <code>Tcl_GetBoolean</code> stores a zero value at <i>*boolPtr</i>. If <i>src</i> is any of <code>1</code>, <code>true</code>, <code>yes</code>, or <code>on</code>, then 1 is stored at <i>*boolPtr</i>. Any of these values may be abbreviated, and upper-case spellings are also acceptable. </p>
<h2>Keywords</h2>
<p>boolean, conversion, double, floating-point, integer</p>
