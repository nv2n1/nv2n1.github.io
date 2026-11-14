---
title: "ntdb(3)"
name: "ntdb"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ntdb/"
description: "ntdb – A not-so trivial keyword/data database system"
---

<p>ntdb &#8211; A not-so trivial keyword/data database system</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ntdb.h&gt;</code></pre>
<h2>Description</h2>
<p>If you have previously used the tdb library from Samba, much of this will seem familiar, but there are some API changes which a compiler will warn you about if you simply replace &#8216;tdb&#8217; with &#8216;ntdb&#8217; in your code! The on-disk format for ntdb is incompatible with tdb. </p>
<p> tdb&#8217;s API was based on gdbm, and ntdb continues this tradition, with enhancements. A differences guide is available in the text file lib/ntdb/doc/TDB_porting.txt in the SAMBA source tree.</p>
<h2>Ntdb Api Overview</h2>
<p>The complete API is documented in the ntdb.h header, which is kept up-to-date and recommended reading. </p>
<p> Normal usage is to call ntdb_open() to create or open an ntdb file. ntdb_store() is used to add records, ntdb_fetch() is used to fetch them. Traversals are supported via callback (ntdb_traverse()) or iteration (ntdb_firstkey() and ntdb_nextkey()). Transactions are supported for batching updates or reads atomically, using ntdb_transaction_start() and ntdb_transaction_commit().</p>
<h3>Use With Talloc</h3>
<p>ntdb_open() takes an optional linked list of attributes: in particular you can specify an alternate allocator (such as talloc): </p>
<dl>
<dd>
<pre>#include &lt;talloc.h&gt;
#include &lt;ntdb.h&gt;
static void *my_alloc(const void *owner, size_t len, void *priv)
{
 return talloc_size(owner, len);
}
static void *my_expand(void *old, size_t newlen, void *priv)
{
 return talloc_realloc_size(NULL, old, newlen);
}
static void my_free(void *old, void *priv)
{
 talloc_free(old);
}
/* This opens an ntdb file as a talloc object with given parent. */
struct ntdb_context *ntdb_open_talloc(const void *parent,
 const char *filename)
{
 struct ntdb_context *ntdb;
 union ntdb_attribute alloc;
 alloc.base.attr = NTDB_ATTRIBUTE_ALLOCATOR;
 alloc.base.next = NULL;
 alloc.alloc.alloc = my_alloc;
 alloc.alloc.expand = my_expand;
 alloc.alloc.free = my_free;
 ntdb = ntdb_open(filename, NTDB_DEFAULT, O_RDWR|O_CREAT, 0600,
 &amp;alloc);
 if (ntdb) {
 talloc_steal(parent, ntdb);
 talloc_set_name(ntdb, &quot;%s&quot;, filename);
 }
 return ntdb;
}</pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://tdb.samba.org/">http://tdb.samba.org/</a></code>m[]</p>
<h2>Author</h2>
<p>The original tdb software was created by Andrew Tridgell, and is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. ntdb was derived from tdb, but mostly rewritten by Rusty Russell.</p>
<h2>Copyright/License</h2>
<p>Copyright (C) Rusty Russell 2013, IBM Corporation </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a></p>
