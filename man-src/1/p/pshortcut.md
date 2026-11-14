---
title: "pshortcut(1)"
name: "pshortcut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pshortcut/"
description: "pshortcut – create a shortcut"
---

<h2>NAME</h2>
<p> pshortcut &#8211; create a shortcut </p>
<h2>SYNOPSIS</h2>
<p> <code>pshortcut</code> [-d <i>LEVEL</i>] [-p <i>DEVNAME</i>] [-h] <i>SHORTCUT</i> <i>TARGET</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>pshortcut</code> creates a shortcut to a file on a device connected through SynCE. </p>
<p> Forward slashes (&#8216;/&#8217;) in remote file names specified on the command line are converted to backward slashes (&#8216;\&#8217;). </p>
<p> This tool must be run as the same user as the dccmd daemon. </p>
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
<dt><i>SHORTCUT</i></p>
<dd>
<p> Full path to the new shortcut that should be created. </p>
<dt><i>TARGET</i></p>
<dd>
<p> Full path to the shortcut&#8217;s target; that is, the file the shortcut should point to. </p>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Scott Gifford &lt;gifford [at] umich.edu&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-synce/">synce</a>(1) <a href="/docs/linux/man/1-pcp/">pcp</a>(1) <a href="/docs/linux/man/1-pls/">pls</a>(1) <a href="/docs/linux/man/1-prm/">prm</a>(1) <a href="/docs/linux/man/1-pmkdir/">pmkdir</a>(1) <a href="/docs/linux/man/1-prmdir/">prmdir</a>(1) </p>
<h2>Index</h2>
