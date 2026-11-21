---

title: "rapiconfig(1)"
name: "rapiconfig"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rapiconfig/"
description: "rapiconfig – upload an XML config file to a SynCE connected device"
---

<p> rapiconfig &#8211; upload an XML config file to a SynCE connected device </p>
<h2>SYNOPSIS</h2>
<p> <code>rapiconfig</code> [-d <i>LEVEL</i>] [-P DEVNAME] [-h] [-p] [-m] <i>FILENAME</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>rapiconfig</code> uploads an XML config file to a device connected via SynCE. </p>
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
<dt>-p</dt>
<dd> Process the document. </dd>
<dt>-m</dt>
<dd> Return metadata. </dd>
<dt><i>FILENAME</i></dt>
<dd> Name of the XML configuration document. </dd>
</dl>
<h2>AUTHOR</h2>
<p> David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> synce(1) </p>
