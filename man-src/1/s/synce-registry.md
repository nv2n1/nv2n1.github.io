---
title: "synce-registry(1)"
name: "synce-registry"
section: "1"
letter: "s"
url: "/docs/linux/man/1-synce-registry/"
description: "synce-registry – read or modify the registry on a PDA"
---

<h2>NAME</h2>
<p> synce-registry &#8211; read or modify the registry on a PDA </p>
<h2>SYNOPSIS</h2>
<p> <code>synce-registry</code> [-d <i>LEVEL</i>] [-p <i>DEVNAME</i>] [-h]<br />
[-r]&nbsp;<wbr><i>PARENTKEY</i>&nbsp;<wbr><i>KEY</i>&nbsp;<wbr><i>VALUE</i><br />
&nbsp;<wbr>&nbsp;<wbr>-w&nbsp;<wbr>[-t TYPE]&nbsp;<wbr><i>PARENTKEY</i>&nbsp;<wbr><i>KEY</i>&nbsp;<wbr><i>VALUE</i>&nbsp;<wbr><i>NEWVALUE</i><br />
&nbsp;<wbr>&nbsp;<wbr>-l&nbsp;<wbr><i>PARENTKEY</i>&nbsp;<wbr><i>KEY</i><br />
&nbsp;<wbr>&nbsp;<wbr>-n&nbsp;<wbr><i>PARENTKEY</i>&nbsp;<wbr><i>NEWKEY</i><br />
&nbsp;<wbr>&nbsp;<wbr>-x&nbsp;<wbr><i>PARENTKEY</i>&nbsp;<wbr><i>KEY</i>&nbsp;<wbr><i>VALUE</i>&nbsp;<wbr>(<code>not supported</code>)<br />
&nbsp;<wbr>&nbsp;<wbr>-X&nbsp;<wbr><i>PARENTKEY</i>&nbsp;<wbr><i>KEY</i>&nbsp;<wbr>(<code>not supported</code>) </p>
<h2>DESCRIPTION</h2>
<p> <code>synce-registry</code> manipulates the registry on a device connected through SynCE. It can read and write values, add new keys and values, and list the values of a key. </p>
<p> Forward slashes (&#8216;/&#8217;) in key names specified on the command line are converted to backward slashes (&#8216;\&#8217;). </p>
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
<dt>[-r] <i>PARENTKEY</i> <i>KEY</i> <i>VALUE</i></p>
<dd>
<p> Read a value. This is the default. </p>
<dt>-w [-t TYPE] <i>PARENTKEY</i> <i>KEY</i> <i>VALUE</i> <i>NEWVALUE</i></p>
<dd>
<p> Write a value. If <i>TYPE</i> is supplied, that type of value will be written; otherwise a string. The following options are valid for <i>TYPE</i>: </p>
<dt>
<dd> <i>sz</i> &#8211; String</p>
<dt>
<dd> <i>dword</i> &#8211; Double-word (4 bytes)</p>
<dt>
<dd> <i>dword_bige</i> &#8211; Double word (4 bytes), big-endian</p>
<dt>
<dd> <i>expand_sz</i> &#8211; String with path expansion</p>
<dt>
<dd> <i>multi_sz</i> &#8211; Multiple strings (<code>not supported</code>)</p>
<dt>
<dd> <i>binary</i> &#8211; Binary data (<code>not supported</code>) </p>
<dt>-l <i>PARENTKEY</i> <i>KEY</i></p>
<dd> List the names of values and subkeys in the given <i>KEY</i>. </p>
<dt>-n <i>PARENTKEY</i> <i>KEY</i></p>
<dd> Create a new key. </p>
<dt>-x <i>PARENTKEY</i> <i>KEY</i> <i>VALUE</i></p>
<dd> Delete the given <i>VALUE</i> from the given <i>KEY</i>. (<code>not implemented</code>) </p>
<dt>-X <i>PARENTKEY</i> <i>KEY</i></p>
<dd> Delete the given <i>KEY</i>. (<code>not implemented</code>) </p>
<dt><i>PARENTKEY</i></p>
<dd>
<p> The top-level key (sometimes called the <i>hive</i>). The only valid options are <i>HKEY_CLASSES_ROOT</i> (abbreviated <i>HKCR</i>), <i>HKEY_CURRENT_USER</i> (<i>HKCU</i>), <i>HKEY_LOCAL_MACHINE</i> (<i>HKLM</i>), and <i>HKEY_USERS</i> (<i>HKU</i>). </p>
<dt><i>KEY</i></p>
<dd> The key to operate on. A key can contain zero or more values and subkeys. </p>
<dt><i>VALUE</i></p>
<dd> The value to operate on. </p>
<dt><i>NEWVALUE</i></p>
<dd> The new value to set <i>VALUE</i> to in a write operation. </p>
</dl>
<h2>AUTHOR</h2>
<p> David Eriksson &lt;twogood [at] users.sourceforge.net&gt;, Scott Gifford &lt;gifford [at] umich.edu&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-synce/">synce</a>(1) <a href="/docs/linux/man/1-pstatus/">pstatus</a>(1) </p>
<h2>Index</h2>
