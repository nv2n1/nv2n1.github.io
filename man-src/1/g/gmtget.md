---
title: "gmtget(1)"
name: "gmtget"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtget/"
description: "gmtget – Get individual GMT default parameters"
---

<h2>NAME</h2>
<p> gmtget &#8211; Get individual GMT default parameters</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtget</code> [ <i>defaultsfile</i> ] [ ] <i>PARAMETER1</i> [ <i>PARAMETER2</i> <i>PARAMETER3</i> &#8230; ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtget</code> will list the value of one or more GMT default parameters.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>PARAMETER</code></p>
<dd> Provide one or several parameters of interest. The current value of those parameters will be writen to <i>stdout</i>. For a complete listing of available parameters and their meaning, see the <code>gmt.conf</code> man page.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-G</code><i>defaultsfile</i></p>
<dd> Name of specific <code>gmt.conf</code> file to read [Default looks first in current directory, then in your home directory, then in ~/.gmt and finally in the system defaults].</p>
<dt><code>-L</code></p>
<dd> Return the values of the parameters on separate lines [Default returns all selected parameter values on one line separated by spaces]</dl>
<h2>EXAMPLE</h2>
<p> To list the value of the parameter PS_COMMENTS: </p>
<pre>
gmt get PS_COMMENTS
</pre>
<p> To get both the values of the parameter MAP_GRID_CROSS_SIZE_PRIMARY and MAP_GRID_CROSS_SIZE_SECONDARY on one line, try </p>
<pre>
gmt get MAP_GRID_CROSS_SIZE_PRIMARY MAP_GRID_CROSS_SIZE_SECONDARY
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtdefaults</code>, <code>gmtset</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
