---

title: "pmv(1)"
name: "pmv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmv/"
description: "pmv – move (rename) files"
---

<h2>NAME</h2>
<p> pmv &#8211; move (rename) files </p>
<p> <code>pmv</code> [- <i>LEVEL</i>] [-p <i>DEVNAME</i>] [-h] <i>SOURCE</i> <i>DESTINATION</i> </p>
<p> <code>pmv</code> renames or moves a file on a device connected through SynCE. </p>
<p> Forward slashes (&#8216;/&#8217;) on the command line are converted to backward slashes (&#8216;\&#8217;). </p>
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
<dt><i>SOURCE</i></dt>
<dd> Full path to the current filename. </dd>
<dt><i>DESTINATION</i></dt>
<dd> Full path to the new filename. </dd>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> synce(1) <a href="/docs/linux/man/1-pcp/">pcp</a>(1) <a href="/docs/linux/man/1-pls/">pls</a>(1) <a href="/docs/linux/man/1-prm/">prm</a>(1) <a href="/docs/linux/man/1-pmkdir/">pmkdir</a>(1) <a href="/docs/linux/man/1-prmdir/">prmdir</a>(1) </p>
