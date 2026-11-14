---
title: "dconf(1)"
name: "dconf"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dconf/"
description: "dconf – Simple tool for manipulating a dconf database"
---

<h2 class="name">NAME</h2>
<p> dconf &#8211; Simple tool for manipulating a dconf database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dconf</code> read [-d] <i>KEY</i></p>
<dt> <code>dconf</code> list <i>DIR</i></p>
<dt> <code>dconf</code> write <i>KEY</i> <i>VALUE</i></p>
<dt> <code>dconf</code> reset [-f] <i>PATH</i></p>
<dt> <code>dconf</code> compile <i>OUTPUT</i> <i>KEYFILEDIR</i></p>
<dt> <code>dconf</code> update [<i>DBDIR</i>]</p>
<dt> <code>dconf</code> watch <i>PATH</i></p>
<dt> <code>dconf</code> dump <i>DIR</i></p>
<dt> <code>dconf</code> load [-f] <i>DIR</i></p>
<dt> <code>dconf</code> help [<i>COMMAND</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dconf</code> program can perform various operations on a dconf database, such as reading or writing individual values or entire directories. This tool operates on dconf directly, without using gsettings schema information. Therefore, it cannot perform type and consistency checks on values. The <code><a href="/docs/linux/man/1-gsettings/">gsettings</a></code>(1) utility is an alternative if such checks are needed. </p>
<p> The <i>DIR</i> arguments must be directory paths (starting and ending with &#8216;/&#8217;), the <i>KEY</i> arguments must be key paths (starting, but not ending with &#8216;/&#8217;) and the <i>PATH</i> arguments can be either directory or key paths. </p>
<p> The <i>OUTPUT</i> argument must the location to write a (binary) dconf database to and the <i>KEYFILEDIR</i> argument must be a .d directory containing keyfiles. </p>
<p> <i>VALUE</i> arguments must be in GVariant format, so e.g. a string must include explicit quotes: &quot;&#8217;foo&#8217;&quot;. This format is also used when printing out values. </p>
<p> Note that dconf needs a D-Bus session bus connection to write changes to the dconf database.</p>
<h2>COMMANDS</h2>
<p> <code>read</code></p>
<dl>
<dt>
<dd> Read the value of a key.</dl>
<p> <code>list</code></p>
<dl>
<dt>
<dd> List the sub-keys and sub-directories of a directory.</dl>
<p> <code>write</code></p>
<dl>
<dt>
<dd> Write a new value to a key.</dl>
<p> <code>reset</code></p>
<dl>
<dt>
<dd> Reset a key or an entire directory. For directories, <code>-f</code> must be specified.</dl>
<p> <code>compile</code></p>
<dl>
<dt>
<dd> Compile a binary database from keyfiles. </p>
<p> The result is always in little-endian byte order, so it can be safely installed in &#8216;share&#8217;. If it is used on a big endian machine, dconf will automatically byteswap the contents on read.</dl>
<p> <code>update</code></p>
<dl>
<dt>
<dd> Update the system dconf databases.</dl>
<p> <code>watch</code></p>
<dl>
<dt>
<dd> Watch a key or directory for changes.</dl>
<p> <code>dump</code></p>
<dl>
<dt>
<dd> Dump an entire subpath to stdout. The output is in a keyfile-like format, with values in GVariant syntax.</dl>
<p> <code>load</code></p>
<dl>
<dt>
<dd> Populate a subpath from stdin. The expected format is the same as produced by <code>dump</code>. Attempting to change non-writable keys cancels the load command. To ignore changes to non-writable keys instead, use <code>-f</code>.</dl>
<p> <code>help</code></p>
<dl>
<dt>
<dd> Display help and exit. If <i>COMMAND</i> is given, display help for this command.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>DCONF_PROFILE</code></p>
<dl>
<dt>
<dd> This environment variable determines which dconf profile to use. See <code><a href="/docs/linux/man/7-dconf/">dconf</a></code>(7).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-dconf/">dconf</a></code>(7), <code><a href="/docs/linux/man/1-gsettings/">gsettings</a></code>(1), <code><a href="/docs/linux/man/1-dconf-editor/">dconf-editor</a></code>(1) </p>
<h2>Index</h2>
