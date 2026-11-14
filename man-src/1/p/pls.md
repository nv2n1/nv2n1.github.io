---
title: "pls(1)"
name: "pls"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pls/"
description: "pls – list directory contents"
---

<h2>NAME</h2>
<p> pls &#8211; list directory contents </p>
<h2>SYNOPSIS</h2>
<p> <code>pls</code> [-a] [-R] [-d <i>LEVEL</i>] [-p <i>DEVNAME</i>] [-h] [<i>DIRECTORY</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pls</code> list the contents of a directory on a device connected through SynCE. </p>
<p> Forward slashes (&#8216;/&#8217;) on the command line are converted to backward slashes (&#8216;\&#8217;). </p>
<dl>
<dt>File attributes</p>
<dd>
<dt>
<dd> A Archive</p>
<dt>
<dd> C Compressed</p>
<dt>
<dd> D Directory</p>
<dt>
<dd> H Hidden</p>
<dt>
<dd> I In ROM</p>
<dt>
<dd> M ROM module (can only be executed, not read!)</p>
<dt>
<dd> N Normal</p>
<dt>
<dd> R Read-only</p>
<dt>
<dd> S System</p>
<dt>
<dd> T Temporary </p>
</dl>
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
<dt>-a</p>
<dd> Show all files including those marked as hidden. </p>
<dt>-R</p>
<dd> Recursively list subdirectories. </p>
<dt>-h</p>
<dd> Display help message. </p>
<dt><i>DIRECTORY</i></p>
<dd> The full path name to the directory. Wild cards are allowed, but only for the trailing part of the path, and should be protected from the shell. If this parameter is relative, it is assumed to be relative to the &quot;My Documents&quot; folder. Similarly, if this parameter is omitted, the contents of the &quot;My Documents&quot; folder is listed. </p>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-synce/">synce</a>(1) <a href="/docs/linux/man/1-pcp/">pcp</a>(1) <a href="/docs/linux/man/1-pls/">pls</a>(1) <a href="/docs/linux/man/1-prm/">prm</a>(1) <a href="/docs/linux/man/1-pmkdir/">pmkdir</a>(1) <a href="/docs/linux/man/1-prmdir/">prmdir</a>(1) </p>
<h2>Index</h2>
