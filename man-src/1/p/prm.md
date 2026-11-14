---
title: "prm(1)"
name: "prm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prm/"
description: "prm – remove file"
---

<h2>NAME</h2>
<p> prm &#8211; remove file </p>
<h2>SYNOPSIS</h2>
<p> <code>prm</code> [-d <i>LEVEL</i>] [-p <i>DEVNAME</i>] [-h] <i>FILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>prm</code> removes a file on a device connected through SynCE. </p>
<p> Forward slashes (&#8216;/&#8217;) on the command line are converted to backward slashes (&#8216;\&#8217;). </p>
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
<dt><i>FILE</i></p>
<dd> Full path name to the file that should be removed. </p>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-synce/">synce</a>(1) <a href="/docs/linux/man/1-pcp/">pcp</a>(1) <a href="/docs/linux/man/1-pls/">pls</a>(1) <a href="/docs/linux/man/1-pmv/">pmv</a>(1) <a href="/docs/linux/man/1-pmkdir/">pmkdir</a>(1) <a href="/docs/linux/man/1-prmdir/">prmdir</a>(1) </p>
<h2>Index</h2>
