---
title: "humanize_number(3)"
name: "humanize_number"
section: "3"
letter: "h"
url: "/docs/linux/man/3-humanize_number/"
---

<h2 class="name">NAME</h2>
 

 <b>dehumanize_number</b> <b>humanize_number</b> - format a number into a human readable form and viceversa 

<h2>LIBRARY</h2>

 Lb libbsd

<h2>SYNOPSIS</h2>

 In bsd/stdlib.h Ft int Fn dehumanize_number const char *str int64_t *result Ft int Fn humanize_number char *buf size_t len int64_t number const char *suffix int scale int flags

<h2>DESCRIPTION</h2>

 The Fn humanize_number function formats the signed 64 bit quantity given in Fa number into Fa buffer . A space and then Fa suffix is appended to the end. Fa buffer must be at least Fa len bytes long. 

 If the formatted number (including Fa suffix ) would be too long to fit into Fa buffer , then divide Fa number by 1024 until it will. In this case, prefix Fa suffix with the appropriate SI designator. 

 The prefixes are:
<dl> 

<dt><b>Prefix Ta </b><b>Description Ta </b><b>Multiplier</b>
<dd>
<dt><b>k<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>kilo<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1024</b>
<dd>
<dt><b>M<tt>&nbsp;<wbr></tt>mega<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1048576</b>
<dd>
<dt><b>G<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>giga1073741824</b>
<dd>
<dt><b>Ttera1099511627776</b>
<dd>
<dt><b>Ppeta1125899906842624</b>
<dd>
<dt><b>Eexa1152921504606846976</b>
<dd></dl>
 

 

 Fa len must be at least 4 plus the length of
 Fa suffix , in order to ensure a useful result is generated into Fa buffer . To use a specific prefix, specify this as Fa scale (Multiplier = 1024 ^ scale). This can not be combined with any of the Fa scale flags below. 

 The following flags may be passed in scale
<dl> 

<dt><b>HN_AUTOSCALE</b>
<dd> Format the buffer using the lowest multiplier possible.
<dt><b>HN_GETSCALE</b>
<dd> Return the prefix index number (the number of times Fa number must be divided to fit) instead of formatting it to the buffer.</dl>
 

 

 The following flags may be passed in flags
<dl> 

<dt><b>HN_DECIMAL</b>
<dd> If the final result is less than 10, display it using one digit.
<dt><b>HN_NOSPACE</b>
<dd> Do not put a space between Fa number and the prefix.
<dt><b>HN_B</b>
<dd> Use 'B' (bytes) as prefix if the original result does not have a prefix.
<dt><b>HN_DIVISOR_1000</b>
<dd> Divide Fa number with 1000 instead of 1024.</dl>
 

 

 The Fn dehumanize_number function parses the string representing an integral value given in Fa str and stores the numerical value in the integer pointed to by Fa result . The provided string may hold one of the suffixes, which will be interpreted and used to scale up its accompanying numerical value.

<h2>RETURN VALUES</h2>

 Fn humanize_number returns the number of characters stored in Fa buffer (excluding the terminating NUL) upon success, or -1 upon failure. If <b>HN_GETSCALE</b> is specified, the prefix index number will be returned instead. 

 Fn dehumanize_number returns 0 if the string was parsed correctly. A -1 is returned to indicate failure and an error code is stored in <i>errno</i>

<h2>ERRORS</h2>

 Fn dehumanize_number will fail and no number will be stored in Fa result if:
<dl> 

<dt><b>Bq </b>Er EINVAL
<dd> The string in Fa str was empty or carried an unknown suffix.
<dt><b>Bq </b>Er ERANGE
<dd> The string in Fa str represented a number that does not fit in Fa result .</dl>
 

<h2>SEE ALSO</h2>

 humanize_number9

<h2>HISTORY</h2>

 Fn humanize_number first appeared in Nx 2.0 . 

 Fn dehumanize_number first appeared in Nx 5.0 . 

<h2>Index</h2>


