---
title: "synce-install-cab(1)"
name: "synce-install-cab"
section: "1"
letter: "s"
url: "/docs/linux/man/1-synce-install-cab/"
description: "synce-install-cab – install .cab file"
---

<h2>NAME</h2>
<p> synce-install-cab &#8211; install .cab file </p>
<h2>SYNOPSIS</h2>
<p> <code>synce-install-cab</code> [-d <i>LEVEL</i>] [-p <i>device_path</i>] [-o <i>WCE_OPT</i>] [-n] <i>FILENAME</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>synce-install-cab</code> installs a .cab file on a device connected through SynCE. </p>
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
<dt>-o <i>WCE_OPT</i></p>
<dd> Flags to pass to <i>wceload.exe</i> on the remote device. Useful flags include:</p>
<dt>
<dd> /noui &#8211; Install silently</p>
<dt>
<dd> /delete 1 &#8211; Don&#8217;t delete CAB file after installation</p>
<dt>
<dd> /nouninstall &#8211; Don&#8217;t create an uninstall file</p>
<dt>
<dd> /askdest &#8211; Ask where to install</p>
<dt>
<dd> /noaskdest &#8211; Get install information from registry </p>
<dt>-n</p>
<dd> Don&#8217;t run wceload (just copy CAB files) </p>
<dt><i>FILENAME</i></p>
<dd> The .cab file(s) that will be installed. If no filenames are specified, <i>wceload.exe</i> will nontheless be run on the remote device; this will install any CAB files already copied, for example with the <i>-n</i> flag. </p>
</dl>
<h2>AUTHOR</h2>
<p> David Eriksson &lt;twogood [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-synce/">synce</a>(1) <a href="/docs/linux/man/1-synce-remove-program/">synce-remove-program</a>(1) <a href="/docs/linux/man/1-synce-list-programs/">synce-list-programs</a>(1) <a href="/docs/linux/man/1-prun/">prun</a>(1) <a href="/docs/linux/man/1-pcp/">pcp</a>(1) </p>
<h2>Index</h2>
