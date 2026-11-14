---
title: "xlsatoms(1)"
name: "xlsatoms"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xlsatoms/"
description: "xlsatoms – list interned atoms defined on server"
---

<h2 class="name">NAME</h2>
<p> xlsatoms &#8211; list interned atoms defined on server </p>
<h2>SYNOPSIS</h2>
<p> <code>xlsatoms</code> [-options &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xlsatoms</i> lists the interned atoms. By default, all atoms starting from 1 (the lowest atom value defined by the protocol) are listed until unknown atom is found. If an explicit range is given, <i>xlsatoms</i> will try all atoms in the range, regardless of whether or not any are undefined.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>dpy</i></p>
<dd> This option specifies the X server to which to connect.</p>
<dt><code>-format </code><i>string</i></p>
<dd> This option specifies a <i>printf</i>-style string used to list each atom <i>&lt;value,name&gt;</i> pair, printed in that order (<i>value</i> is an <i>unsigned long</i> and <i>name</i> is a <i>char *</i>). <i>Xlsatoms</i> will supply a newline at the end of each line. The default is <i>%lu	%s</i>.</p>
<dt><code>-range </code><i>[low]-[high]</i></p>
<dd> This option specifies the range of atom values to check. If <i>low</i> is not given, a value of 1 assumed. If <i>high</i> is not given, <i>xlsatoms</i> will stop at the first undefined atom at or above <i>low</i>.</p>
<dt><code>-name </code><i>string</i></p>
<dd> This option specifies the name of an atom to list. If the atom does not exist, a message will be printed on the standard error.</p>
<dt><code>-version</code></p>
<dd> Print out the program version and exit.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/1-xprop/">xprop</a>(1)</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display to use.</dl>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium </p>
<h2>Index</h2>
