---
title: "ntdbtool(8)"
name: "ntdbtool"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntdbtool/"
description: "ntdbtool – manipulate the contents NTDB files"
---

<p>ntdbtool &#8211; manipulate the contents NTDB files</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ntdbtool</code> <i>NTDBFILE</i> [<i>COMMANDS</i>&#8230;]</dt></dl>
<h2>Description</h2>
<dd>This tool is part of the <code>samba</code>(1) suite. </dd>
<p> <code>ntdbtool</code> a tool for displaying and altering the contents of Samba NTDB (New Trivial DataBase) files. Each of the commands listed below can be entered interactively or provided on the command line.</p>
<h2>Commands</h2>
<p><code>create</code> <i>NTDBFILE</i></p>
<dl>
<dd>Create a new database named <i>NTDBFILE</i>.</dd></dl>
<p> <code>open</code> <i>NTDBFILE</i></p>
<dl>
<dd>Open an existing database named <i>NTDBFILE</i>.</dd></dl>
<p> <code>erase</code></p>
<dl>
<dd>Erase the current database.</dd></dl>
<p> <code>dump</code></p>
<dl>
<dd>Dump the current database as strings.</dd></dl>
<p> <code>cdump</code></p>
<dl>
<dd>Dump the current database as connection records.</dd></dl>
<p> <code>keys</code></p>
<dl>
<dd>Dump the current database keys as strings.</dd></dl>
<p> <code>hexkeys</code></p>
<dl>
<dd>Dump the current database keys as hex values.</dd></dl>
<p> <code>info</code></p>
<dl>
<dd>Print summary information about the current database.</dd></dl>
<p> <code>insert</code> <i>KEY</i> <i>DATA</i></p>
<dl>
<dd>Insert a record into the current database.</dd></dl>
<p> <code>move</code> <i>KEY</i> <i>NTDBFILE</i></p>
<dl>
<dd>Move a record from the current database into <i>NTDBFILE</i>.</dd></dl>
<p> <code>store</code> <i>KEY</i> <i>DATA</i></p>
<dl>
<dd>Store (replace) a record in the current database.</dd></dl>
<p> <code>show</code> <i>KEY</i></p>
<dl>
<dd>Show a record by key.</dd></dl>
<p> <code>delete</code> <i>KEY</i></p>
<dl>
<dd>Delete a record by key.</dd></dl>
<p> <code>list</code></p>
<dl>
<dd>Print the current database hash table and free list.</dd></dl>
<p> <code>free</code></p>
<dl>
<dd>Print the current database and free list.</dd></dl>
<p> <code>!</code> <i>COMMAND</i></p>
<dl>
<dd>Execute the given system command.</dd></dl>
<p> <code>first</code></p>
<dl>
<dd>Print the first record in the current database.</dd></dl>
<p> <code>next</code></p>
<dl>
<dd>Print the next record in the current database.</dd></dl>
<p> <code>check</code></p>
<dl>
<dd>Check the integrity of the current database.</dd></dl>
<p> <code>repack</code></p>
<dl>
<dd>Repack a database using a temporary file to remove fragmentation.</dd></dl>
<p> <code>quit</code></p>
<dl>
<dd>Exit <code>ntdbtool</code>.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tdbtool/">tdbtool</a>(8)</p>
<h2>Caveats</h2>
<p>The contents of the Samba NTDB files are private to the implementation and should not be altered with <code>ntdbtool</code>.</p>
<h2>Version</h2>
<p>This man page is correct for version 4.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
