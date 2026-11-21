---

title: "synce-list-programs(1)"
name: "synce-list-programs"
section: "1"
letter: "s"
url: "/docs/linux/man/1-synce-list-programs/"
description: "synce-list-programs – shows a list of all installed programs"
---

<h2>NAME</h2>
<p> synce-list-programs &#8211; shows a list of all installed programs </p>
<p> <code>synce-list-programs</code> [-d <i>LEVEL</i>] [-p <i>DEVNAME</i>] [-h] </p>
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
</dl>
<p> <code>synce-list-programs</code> shows a list of all programs installed on a device connected through SynCE. </p>
<h2>AUTHOR</h2>
<p> David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> synce(1) <a href="/docs/linux/man/1-synce-install-cab/">synce-install-cab</a>(1) <a href="/docs/linux/man/1-synce-remove-program/">synce-remove-program</a>(1) </p>
