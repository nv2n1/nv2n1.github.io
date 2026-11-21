---

title: "pls(1)"
name: "pls"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pls/"
description: "pls – list directory contents"
---

<p> pls &#8211; list directory contents </p>
<h2>SYNOPSIS</h2>
<p> <code>pls</code> [-a] [-R] [-d <i>LEVEL</i>] [-p <i>DEVNAME</i>] [-h] [<i>DIRECTORY</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pls</code> list the contents of a directory on a device connected through SynCE. </p>
<p> Forward slashes (&#8216;/&#8217;) on the command line are converted to backward slashes (&#8216;\&#8217;). </p>
<dl>
<dt>File attributes</dt>
<dd>
</dd><dt>
</dt><dd> A Archive</dd>
<dt>
</dt><dd> C Compressed</dd>
<dt>
</dt><dd> D Directory</dd>
<dt>
</dt><dd> H Hidden</dd>
<dt>
</dt><dd> I In ROM</dd>
<dt>
</dt><dd> M ROM module (can only be executed, not read!)</dd>
<dt>
</dt><dd> N Normal</dd>
<dt>
</dt><dd> R Read-only</dd>
<dt>
</dt><dd> S System</dd>
<dt>
</dt><dd> T Temporary </dd>
</dl>
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
<dt>-a</dt>
<dd> Show all files including those marked as hidden. </dd>
<dt>-R</dt>
<dd> Recursively list subdirectories. </dd>
<dt>-h</dt>
<dd> Display help message. </dd>
<dt><i>DIRECTORY</i></dt>
<dd> The full path name to the directory. Wild cards are allowed, but only for the trailing part of the path, and should be protected from the shell. If this parameter is relative, it is assumed to be relative to the &quot;My Documents&quot; folder. Similarly, if this parameter is omitted, the contents of the &quot;My Documents&quot; folder is listed. </dd>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> synce(1) <a href="/docs/linux/man/1-pcp/">pcp</a>(1) <a href="/docs/linux/man/1-pls/">pls</a>(1) <a href="/docs/linux/man/1-prm/">prm</a>(1) <a href="/docs/linux/man/1-pmkdir/">pmkdir</a>(1) <a href="/docs/linux/man/1-prmdir/">prmdir</a>(1) </p>
