---

title: "synce-registry(1)"
name: "synce-registry"
section: "1"
letter: "s"
url: "/docs/linux/man/1-synce-registry/"
description: "synce-registry – read or modify the registry on a PDA"
---

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
<dt>[-r] <i>PARENTKEY</i> <i>KEY</i> <i>VALUE</i></dt>
<dd>
<p> Read a value. This is the default. </p>
</dd><dt>-w [-t TYPE] <i>PARENTKEY</i> <i>KEY</i> <i>VALUE</i> <i>NEWVALUE</i></dt>
<dd>
<p> Write a value. If <i>TYPE</i> is supplied, that type of value will be written; otherwise a string. The following options are valid for <i>TYPE</i>: </p>
</dd><dt>
</dt><dd> <i>sz</i> &#8211; String</dd>
<dt>
</dt><dd> <i>dword</i> &#8211; Double-word (4 bytes)</dd>
<dt>
</dt><dd> <i>dword_bige</i> &#8211; Double word (4 bytes), big-endian</dd>
<dt>
</dt><dd> <i>expand_sz</i> &#8211; String with path expansion</dd>
<dt>
</dt><dd> <i>multi_sz</i> &#8211; Multiple strings (<code>not supported</code>)</dd>
<dt>
</dt><dd> <i>binary</i> &#8211; Binary data (<code>not supported</code>) </dd>
<dt>-l <i>PARENTKEY</i> <i>KEY</i></dt>
<dd> List the names of values and subkeys in the given <i>KEY</i>. </dd>
<dt>-n <i>PARENTKEY</i> <i>KEY</i></dt>
<dd> Create a new key. </dd>
<dt>-x <i>PARENTKEY</i> <i>KEY</i> <i>VALUE</i></dt>
<dd> Delete the given <i>VALUE</i> from the given <i>KEY</i>. (<code>not implemented</code>) </dd>
<dt>-X <i>PARENTKEY</i> <i>KEY</i></dt>
<dd> Delete the given <i>KEY</i>. (<code>not implemented</code>) </dd>
<dt><i>PARENTKEY</i></dt>
<dd>
<p> The top-level key (sometimes called the <i>hive</i>). The only valid options are <i>HKEY_CLASSES_ROOT</i> (abbreviated <i>HKCR</i>), <i>HKEY_CURRENT_USER</i> (<i>HKCU</i>), <i>HKEY_LOCAL_MACHINE</i> (<i>HKLM</i>), and <i>HKEY_USERS</i> (<i>HKU</i>). </p>
</dd><dt><i>KEY</i></dt>
<dd> The key to operate on. A key can contain zero or more values and subkeys. </dd>
<dt><i>VALUE</i></dt>
<dd> The value to operate on. </dd>
<dt><i>NEWVALUE</i></dt>
<dd> The new value to set <i>VALUE</i> to in a write operation. </dd>
</dl>
<h2>AUTHOR</h2>
<p> David Eriksson &lt;twogood [at] users.sourceforge.net&gt;, Scott Gifford &lt;gifford [at] umich.edu&gt;.</p>
<h2>SEE ALSO</h2>
<p> synce(1) <a href="/docs/linux/man/1-pstatus/">pstatus</a>(1) </p>
