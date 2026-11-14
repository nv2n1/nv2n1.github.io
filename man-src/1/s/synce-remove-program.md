---
title: "synce-remove-program(1)"
name: "synce-remove-program"
section: "1"
letter: "s"
url: "/docs/linux/man/1-synce-remove-program/"
description: "synce-remove-program – removes a program from your device"
---

<h2>NAME</h2>
<p> synce-remove-program &#8211; removes a program from your device </p>
<h2>SYNOPSIS</h2>
<p> <code>synce-remove-program</code> [-d <i>LEVEL</i>] [-p <i>device_path</i>] [-o <i>UNLOAD_OPT</i>] <i>NAME</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>synce-remove-program</code> removes a program on a device connected through SynCE. </p>
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
<dt>-p <i>PATH</i></p>
<dd> Path to device </p>
<dt>-h</p>
<dd> Display help message. </p>
<dt>-o <i>UNLOAD_OPT</i></p>
<dd> Flags to pass to <i>unload.exe</i> on the remote device. Currently no flags are known, but this flag is here in case we find some. </p>
<dt><i>NAME</i></p>
<dd> The name of the program on the device. Program names are in the form &quot;Provider Program&quot;. This is the same way the name will appear under Settings -&gt; Remove programs on your device, or in the ouput from <i>synce-list-programs</i>. </p>
</dl>
<h2>AUTHOR</h2>
<p> David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-synce/">synce</a>(1) <a href="/docs/linux/man/1-synce-list-programs/">synce-list-programs</a>(1) <a href="/docs/linux/man/1-synce-install-cab/">synce-install-cab</a>(1) <a href="/docs/linux/man/1-prun/">prun</a>(1) </p>
<h2>Index</h2>
