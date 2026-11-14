---
title: "mdb_dump(1)"
name: "mdb_dump"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb_dump/"
description: "mdb_dump – LMDB environment export tool"
---

<h2 class="name">NAME</h2>
<p> mdb_dump &#8211; LMDB environment export tool </p>
<h2>SYNOPSIS</h2>
<p> <code>mdb_dump</code> [<code>-V</code>] [<code>-f</code><i>&nbsp;<wbr>file</i>] [<code>-l</code>] [<code>-n</code>] [<code>-p</code>] [<code>-a</code>&nbsp;<wbr>| <code>-s</code><i>&nbsp;<wbr>subdb</i>] <code>&nbsp;<wbr>envpath</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>mdb_dump</code> utility reads a database and writes its contents to the standard output using a portable flat-text format understood by the <code><a href="/docs/linux/man/1-mdb_load/">mdb_load</a></code>(1) utility.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></p>
<dd> Write the library version number to the standard output, and exit.</p>
<dt><code>-f</code>&nbsp;<wbr>file</p>
<dd> Write to the specified file instead of to the standard output.</p>
<dt><code>-l</code></p>
<dd> List the databases stored in the environment. Just the names will be listed, no data will be output.</p>
<dt><code>-n</code></p>
<dd> Dump an LMDB database which does not use subdirectories.</p>
<dt><code>-p</code></p>
<dd> If characters in either the key or data items are printing characters (as defined by <a href="/docs/linux/man/3-isprint/">isprint</a>(3)), output them directly. This option permits users to use standard text editors and tools to modify the contents of databases. </p>
<p> Note: different systems may have different notions about what characters are considered printing characters, and databases dumped in this manner may be less portable to external systems.</p>
<dt><code>-a</code></p>
<dd> Dump all of the subdatabases in the environment.</p>
<dt><code>-s</code>&nbsp;<wbr>subdb</p>
<dd> Dump a specific subdatabase. If no database is specified, only the main database is dumped.</dl>
<h2>DIAGNOSTICS</h2>
<p> Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error. </p>
<p> Dumping and reloading databases that use user-defined comparison functions will result in new databases that use the default comparison functions. <code>In this case it is quite likely that the reloaded database will be damaged beyond repair permitting neither record storage nor retrieval.</code> </p>
<p> The only available workaround is to modify the source for the <code><a href="/docs/linux/man/1-mdb_load/">mdb_load</a></code>(1) utility to load the database using the correct comparison functions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mdb_load/">mdb_load</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Howard Chu of Symas Corporation &lt;<a rel="nofollow" href="http://www.symas.com">http://www.symas.com</a>&gt; </p>
<h2>Index</h2>
