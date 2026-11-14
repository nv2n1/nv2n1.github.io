---
title: "pstatus(1)"
name: "pstatus"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pstatus/"
description: "pstatus – show device status"
---

<h2>NAME</h2>
<p> pstatus &#8211; show device status </p>
<h2>SYNOPSIS</h2>
<p> <code>pstatus</code> [-d <i>LEVEL</i>] [-p <i>DEVNAME</i>] [-h] </p>
<h2>DESCRIPTION</h2>
<p> <code>pstatus</code> displays information about a device connected through SynCE. </p>
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
</dl>
<h2>AUTHOR</h2>
<p> David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-synce/">synce</a>(1) <a href="/docs/linux/man/1-prun/">prun</a>(1) </p>
<h2>Index</h2>
