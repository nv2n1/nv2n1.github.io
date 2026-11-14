---
title: "ldb(3)"
name: "ldb"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb/"
description: "ldb – A light-weight database library"
---

<h2 class="name">NAME</h2>
<p> ldb &#8211; A light-weight database library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldb.h&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> ldb is a light weight embedded database library and API. With a programming interface that is very similar to LDAP, ldb can store its data either in a <a href="/docs/linux/man/3-tdb/">tdb</a>(3) database or in a real LDAP database. </p>
<p> When used with the tdb backend ldb does not require any database daemon. Instead, ldb function calls are processed immediately by the ldb library, which does IO directly on the database, while allowing multiple readers/writers using operating system byte range locks. This leads to an API with very low overheads, often resulting in speeds of more than 10x what can be achieved with a more traditional LDAP architecture. </p>
<p> In a taxonomy of databases ldb would sit half way between key/value pair databases (such as berkley db or tdb) and a full LDAP database. With a structured attribute oriented API like LDAP and good indexing capabilities, ldb can be used for quite sophisticated applications that need a light weight database, without the administrative overhead of a full LDAP installation. </p>
<p> Included with ldb are a number of useful command line tools for manipulating a ldb database. These tools are similar in style to the equivalent ldap command line tools. </p>
<p> In its default mode of operation with a tdb backend, ldb can also be seen as a &quot;schema-less LDAP&quot;. By default ldb does not require a schema, which greatly reduces the complexity of getting started with ldb databases. As the complexity of you application grows you can take advantage of some of the optional schema-like attributes that ldb offers, or you can migrate to using the full LDAP api while keeping your exiting ldb code. </p>
<p> If you are new to ldb, then I suggest starting with the manual pages for <a href="/docs/linux/man/1-ldbsearch/">ldbsearch</a>(1) and <a href="/docs/linux/man/1-ldbedit/">ldbedit</a>(1), and experimenting with a local database. Then I suggest you look at the <a href="/docs/linux/man/3-ldb_connect/">ldb_connect</a>(3) and <a href="/docs/linux/man/3-ldb_search/">ldb_search</a>(3) manual pages.</p>
<h2>TOOLS</h2>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-ldbsearch/">ldbsearch</a>(1) &#8211; command line ldb search utility</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-ldbedit/">ldbedit</a>(1) &#8211; edit all or part of a ldb database using your favourite editor</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-ldbadd/">ldbadd</a>(1) &#8211; add records to a ldb database using LDIF formatted input</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-ldbdel/">ldbdel</a>(1) &#8211; delete records from a ldb database</dl>
<dl>
<dt>
<dd> &bull; <a href="/docs/linux/man/1-ldbmodify/">ldbmodify</a>(1) &#8211; modify records in a ldb database using LDIF formatted input</dl>
<h2>FUNCTIONS</h2>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_connect/">ldb_connect</a>(3)</code> &#8211; connect to a ldb backend</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_search/">ldb_search</a>(3)</code> &#8211; perform a database search</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_add/">ldb_add</a>(3)</code> &#8211; add a record to the database</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_delete/">ldb_delete</a>(3)</code> &#8211; delete a record from the database</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_modify/">ldb_modify</a>(3)</code> &#8211; modify a record in the database</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_errstring/">ldb_errstring</a>(3)</code> &#8211; retrieve extended error information from the last operation</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_ldif_write/">ldb_ldif_write</a>(3)</code> &#8211; write a LDIF formatted message</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_ldif_write_file/">ldb_ldif_write_file</a>(3)</code> &#8211; write a LDIF formatted message to a file</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_ldif_read/">ldb_ldif_read</a>(3)</code> &#8211; read a LDIF formatted message</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_ldif_read_free/">ldb_ldif_read_free</a>(3)</code> &#8211; free the result of a ldb_ldif_read()</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_ldif_read_file/">ldb_ldif_read_file</a>(3)</code> &#8211; read a LDIF message from a file</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_ldif_read_string/">ldb_ldif_read_string</a>(3)</code> &#8211; read a LDIF message from a string</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_msg_find_element/">ldb_msg_find_element</a>(3)</code> &#8211; find an element in a ldb_message</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_val_equal_exact/">ldb_val_equal_exact</a>(3)</code> &#8211; compare two ldb_val structures</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_msg_find_val/">ldb_msg_find_val</a>(3)</code> &#8211; find an element by value</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_msg_add_empty/">ldb_msg_add_empty</a>(3)</code> &#8211; add an empty message element to a ldb_message</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_msg_add/">ldb_msg_add</a>(3)</code> &#8211; add a non-empty message element to a ldb_message</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_msg_element_compare/">ldb_msg_element_compare</a>(3)</code> &#8211; compare two ldb_message_element structures</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_msg_find_int/">ldb_msg_find_int</a>(3)</code> &#8211; return an integer value from a ldb_message</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_msg_find_uint/">ldb_msg_find_uint</a>(3)</code> &#8211; return an unsigned integer value from a ldb_message</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_msg_find_double/">ldb_msg_find_double</a>(3)</code> &#8211; return a double value from a ldb_message</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_msg_find_string/">ldb_msg_find_string</a>(3)</code> &#8211; return a string value from a ldb_message</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_set_alloc/">ldb_set_alloc</a>(3)</code> &#8211; set the memory allocation function to be used by ldb</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_set_debug/">ldb_set_debug</a>(3)</code> &#8211; set a debug handler to be used by ldb</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-ldb_set_debug_stderr/">ldb_set_debug_stderr</a>(3)</code> &#8211; set a debug handler for stderr output</dl>
<h2>AUTHOR</h2>
<p> ldb was written by m[blue]<code>Andrew Tridgell</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> If you wish to report a problem or make a suggestion then please see the m[blue]<code><a rel="nofollow" href="http://ldb.samba.org/">http://ldb.samba.org/</a></code>m[] web site for current contact and maintainer information. </p>
<p> ldb is released under the GNU Lesser General Public License version 2 or later. Please see the file COPYING for license details.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Andrew Tridgell</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://samba.org/~tridge/">http://samba.org/~tridge/</a></dl>
</dl>
<h2>Index</h2>
