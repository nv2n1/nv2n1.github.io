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
<dt>-d <i>LEVEL</i></dt>
<dd> Set debug log level:</dd>
<dt>
</dt><dd> 0 &#8211; No logging (default)</dd>
<dt>
</dt><dd> 1 &#8211; Errors only</dd>
<dt>
</dt><dd> 2 &#8211; Errors and warnings</dd>
<dt>
</dt><dd> 3 &#8211; Everything </dd>
<dt>-p <i>DEVNAME</i></dt>
<dd> Use the device with the given name, instead of the default. </dd>
<dt>-h</dt>
<dd> Display help message. </dd>
<dt><i>PROGRAM</i></dt>
<dd> The program that will be started. </dd>
<dt>&#8212;</dt>
<dd> Needed if <i>PARAMETERS</i> begin with a dash (&#8216;-&#8216;). </dd>
<dt><i>PARAMETERS</i></dt>
<dd>
<p> Command line parameters to the program. Note that if you need to pass more than one parameter to the program, you will need to enclose the parameters in quotes. </p>
</dd></dl>
<h2>AUTHOR</h2>
<p> David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> synce(1) <a href="/docs/linux/man/1-pstatus/">pstatus</a>(1) </p>
