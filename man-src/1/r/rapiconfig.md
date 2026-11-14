---
title: "rapiconfig(1)"
name: "rapiconfig"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rapiconfig/"
description: "rapiconfig – upload an XML config file to a SynCE connected device"
---

<h2>NAME</h2>
<p> rapiconfig &#8211; upload an XML config file to a SynCE connected device </p>
<h2>SYNOPSIS</h2>
<p> <code>rapiconfig</code> [-d <i>LEVEL</i>] [-P DEVNAME] [-h] [-p] [-m] <i>FILENAME</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>rapiconfig</code> uploads an XML config file to a device connected via SynCE. </p>
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
<dt>-p</p>
<dd> Process the document. </p>
<dt>-m</p>
<dd> Return metadata. </p>
<dt><i>FILENAME</i></p>
<dd> Name of the XML configuration document. </p>
</dl>
<h2>AUTHOR</h2>
<p> David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-synce/">synce</a>(1) </p>
<h2>Index</h2>
