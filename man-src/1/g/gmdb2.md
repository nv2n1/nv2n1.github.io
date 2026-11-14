---
title: "gmdb2(1)"
name: "gmdb2"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmdb2/"
description: "gmdb2 – GNOME UI for MDB Tools"
---

<h2>NAME</h2>
<p> <code>gmdb2 </code>&#8211; GNOME UI for MDB Tools</p>
<h2>SYNOPSIS</h2>
<pre>
<code>gmdb2</code> [<i>database</i>]
</pre>
<h2>DESCRIPTION</h2>
<p> <code>gmdb2</code> is a GNOME UI for MDB Tools.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MDB_JET3_CHARSET</code></p>
<dd> Defines the charset of the input JET3 (access 97) file. Default is CP1252. See <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1).</p>
<dt><code>MDBICONV</code></p>
<dd> Defines the output charset. Default is UTF-8. mdbtools must have been compiled with iconv.</p>
<dt><code>MDBOPTS</code></p>
<dd> semi-column separated list of options:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> use_index</p>
<dt>&bull;</p>
<dd> no_memo</p>
<dt>&bull;</p>
<dd> debug_like</p>
<dt>&bull;</p>
<dd> debug_write</p>
<dt>&bull;</p>
<dd> debug_usage</p>
<dt>&bull;</p>
<dd> debug_ole</p>
<dt>&bull;</p>
<dd> debug_row</p>
<dt>&bull;</p>
<dd> debug_props</p>
<dt>&bull;</p>
<dd> debug_all is a shortcut for all debug_* options</dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mdb-export/">mdb-export</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-prop/">mdb-prop</a></code>(1) <code><a href="/docs/linux/man/1-mdb-sql/">mdb-sql</a></code>(1) <code><a href="/docs/linux/man/1-mdb-ver/">mdb-ver</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-header/">mdb-header</a></code>(1) <code><a href="/docs/linux/man/1-mdb-parsecsv/">mdb-parsecsv</a></code>(1) <code><a href="/docs/linux/man/1-mdb-schema/">mdb-schema</a></code>(1) <code><a href="/docs/linux/man/1-mdb-tables/">mdb-tables</a></code>(1) </p>
<h2>AUTHORS</h2>
<p> The <code>gmdb2</code> utility was written by Brian Bruns. </p>
<h2>Index</h2>
