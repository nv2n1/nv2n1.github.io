---
title: "prun(1)"
name: "prun"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prun/"
description: "prun – run program"
---

<h2>NAME</h2>
<p> prun &#8211; run program </p>
<h2>SYNOPSIS</h2>
<p> <code>prun</code> [-d <i>LEVEL</i>] [-p <i>DEVNAME</i>] [-h] <i>PROGRAM</i> [&#8211;] [<i>PARAMETERS</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>prun</code> starts a program on a device connected through SynCE. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-d <i>LEVEL</i></p>
<dd> Set debug log level:</p>
<dt>
<dd> 0 &#8211; No logging (default)</p>
<dt>
<dd> 1 &#8211; Errors only</p>
<dt>
<dd> 2 &#8211; Errors and warnings</p>
<dt>
<dd> 3 &#8211; Everything </p>
<dt>-p <i>DEVNAME</i></p>
<dd> Use the device with the given name, instead of the default. </p>
<dt>-h</p>
<dd> Display help message. </p>
<dt><i>PROGRAM</i></p>
<dd> The program that will be started. </p>
<dt>&#8212;</p>
<dd> Needed if <i>PARAMETERS</i> begin with a dash (&#8216;-&#8216;). </p>
<dt><i>PARAMETERS</i></p>
<dd>
<p> Command line parameters to the program. Note that if you need to pass more than one parameter to the program, you will need to enclose the parameters in quotes. </p>
</dl>
<h2>AUTHOR</h2>
<p> David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-synce/">synce</a>(1) <a href="/docs/linux/man/1-pstatus/">pstatus</a>(1) </p>
<h2>Index</h2>
