---
title: "dehumanize_number(3)"
name: "dehumanize_number"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dehumanize_number/"
description: "dehumanize_number humanize_number – format a number into a human readable form and viceversa"
---

<h2 class="name">NAME</h2>
<p> <code>dehumanize_number</code> <code>humanize_number</code> &#8211; format a number into a human readable form and viceversa </p>
<h2>LIBRARY</h2>
<p> Lb libbsd</p>
<h2>SYNOPSIS</h2>
<p> In bsd/stdlib.h Ft int Fn dehumanize_number const char *str int64_t *result Ft int Fn humanize_number char *buf size_t len int64_t number const char *suffix int scale int flags</p>
<h2>DESCRIPTION</h2>
<p> The Fn humanize_number function formats the signed 64 bit quantity given in Fa number into Fa buffer . A space and then Fa suffix is appended to the end. Fa buffer must be at least Fa len bytes long. </p>
<p> If the formatted number (including Fa suffix ) would be too long to fit into Fa buffer , then divide Fa number by 1024 until it will. In this case, prefix Fa suffix with the appropriate SI designator. </p>
<p> The prefixes are:</p>
<dl>
<dt><code>Prefix Ta </code><code>Description Ta </code><code>Multiplier</code></p>
<dd>
<dt><code>k<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>kilo<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1024</code></p>
<dd>
<dt><code>M<tt>&nbsp;<wbr></tt>mega<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1048576</code></p>
<dd>
<dt><code>G<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>giga1073741824</code></p>
<dd>
<dt><code>Ttera1099511627776</code></p>
<dd>
<dt><code>Ppeta1125899906842624</code></p>
<dd>
<dt><code>Eexa1152921504606846976</code></p>
<dd></dl>
<p> Fa len must be at least 4 plus the length of<br />
 Fa suffix , in order to ensure a useful result is generated into Fa buffer . To use a specific prefix, specify this as Fa scale (Multiplier = 1024 ^ scale). This can not be combined with any of the Fa scale flags below. </p>
<p> The following flags may be passed in scale</p>
<dl>
<dt><code>HN_AUTOSCALE</code></p>
<dd> Format the buffer using the lowest multiplier possible.</p>
<dt><code>HN_GETSCALE</code></p>
<dd> Return the prefix index number (the number of times Fa number must be divided to fit) instead of formatting it to the buffer.</dl>
<p> The following flags may be passed in flags</p>
<dl>
<dt><code>HN_DECIMAL</code></p>
<dd> If the final result is less than 10, display it using one digit.</p>
<dt><code>HN_NOSPACE</code></p>
<dd> Do not put a space between Fa number and the prefix.</p>
<dt><code>HN_B</code></p>
<dd> Use &#8216;B&#8217; (bytes) as prefix if the original result does not have a prefix.</p>
<dt><code>HN_DIVISOR_1000</code></p>
<dd> Divide Fa number with 1000 instead of 1024.</dl>
<p> The Fn dehumanize_number function parses the string representing an integral value given in Fa str and stores the numerical value in the integer pointed to by Fa result . The provided string may hold one of the suffixes, which will be interpreted and used to scale up its accompanying numerical value.</p>
<h2>RETURN VALUES</h2>
<p> Fn humanize_number returns the number of characters stored in Fa buffer (excluding the terminating NUL) upon success, or -1 upon failure. If <code>HN_GETSCALE</code> is specified, the prefix index number will be returned instead. </p>
<p> Fn dehumanize_number returns 0 if the string was parsed correctly. A -1 is returned to indicate failure and an error code is stored in <i>errno</i></p>
<h2>ERRORS</h2>
<p> Fn dehumanize_number will fail and no number will be stored in Fa result if:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The string in Fa str was empty or carried an unknown suffix.</p>
<dt><code>Bq </code>Er ERANGE</p>
<dd> The string in Fa str represented a number that does not fit in Fa result .</dl>
<h2>SEE ALSO</h2>
<p> humanize_number9</p>
<h2>HISTORY</h2>
<p> Fn humanize_number first appeared in Nx 2.0 . </p>
<p> Fn dehumanize_number first appeared in Nx 5.0 . </p>
<h2>Index</h2>
