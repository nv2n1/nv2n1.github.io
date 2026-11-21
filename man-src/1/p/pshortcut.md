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
<p> <code>pshortcut</code> [-d <i>LEVEL</i>] [-p <i>DEVNAME</i>] [-h] <i>SHORTCUT</i> <i>TARGET</i> </p>
<p> <code>pshortcut</code> creates a shortcut to a file on a device connected through SynCE. </p>
<p> Forward slashes (&#8216;/&#8217;) in remote file names specified on the command line are converted to backward slashes (&#8216;\&#8217;). </p>
<p> This tool must be run as the same user as the dccmd daemon. </p>
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
<dt><i>SHORTCUT</i></dt>
<dd>
<p> Full path to the new shortcut that should be created. </p>
</dd><dt><i>TARGET</i></dt>
<dd>
<p> Full path to the shortcut&#8217;s target; that is, the file the shortcut should point to. </p>
</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Scott Gifford &lt;gifford [at] umich.edu&gt;.</p>
<h2>SEE ALSO</h2>
<p> synce(1) <a href="/docs/linux/man/1-pcp/">pcp</a>(1) <a href="/docs/linux/man/1-pls/">pls</a>(1) <a href="/docs/linux/man/1-prm/">prm</a>(1) <a href="/docs/linux/man/1-pmkdir/">pmkdir</a>(1) <a href="/docs/linux/man/1-prmdir/">prmdir</a>(1) </p>
