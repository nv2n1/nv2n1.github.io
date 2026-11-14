---
title: "wdb_keys(3)"
name: "wdb_keys"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wdb_keys/"
description: "wdb_keys"
---

<p>wdb_keys</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/wdb.h&gt;
</code></pre>
<pre>NEOERR * wdb_keys (WDB *wdb, char **primary_key, ULIST **data);</pre>
<h2>Arguments</h2>
<p>wdb &#8211; open database</p>
<h2>Description</h2>
<p>this function returns the key and column names for the current database </p>
<h2>Return Value</h2>
<p>primary_key &#8211; pointer to the primary key<br />
 data &#8211; pointer to a ULIST of the columns.<br />
 both of these are allocated structures, you can clear data<br />
 with uListDestroy (data, ULIST_FREE) </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-wdb_destroy/">wdb_destroy</a></code>(3), <a href="/docs/linux/man/3-wdbr_delete/">wdbr_delete</a><code>(3), <a href="/docs/linux/man/3-wdb_update/">wdb_update</a></code>(3), <a href="/docs/linux/man/3-wdbr_dump/">wdbr_dump</a><code>(3), <a href="/docs/linux/man/3-wdb_save/">wdb_save</a></code>(3), <a href="/docs/linux/man/3-wdbr_create/">wdbr_create</a><code>(3), <a href="/docs/linux/man/3-wdbr_destroy/">wdbr_destroy</a></code>(3), <a href="/docs/linux/man/3-wdb_attr_set/">wdb_attr_set</a><code>(3), <a href="/docs/linux/man/3-wdb_attr_next/">wdb_attr_next</a></code>(3), <a href="/docs/linux/man/3-wdb_open/">wdb_open</a><code>(3), <a href="/docs/linux/man/3-wdb_column_exchange/">wdb_column_exchange</a></code>(3), <a href="/docs/linux/man/3-wdbr_set/">wdbr_set</a><code>(3), <a href="/docs/linux/man/3-wdb_column_insert/">wdb_column_insert</a></code>(3), <a href="/docs/linux/man/3-wdbr_save/">wdbr_save</a><code>(3), <a href="/docs/linux/man/3-wdbr_next/">wdbr_next</a></code>(3), <a href="/docs/linux/man/3-wdb_keys/">wdb_keys</a><code>(3), <a href="/docs/linux/man/3-wdb_column_delete/">wdb_column_delete</a></code>(3), <a href="/docs/linux/man/3-wdbc_create/">wdbc_create</a><code>(3), <a href="/docs/linux/man/3-wdbr_get/">wdbr_get</a></code>(3), <a href="/docs/linux/man/3-wdb_attr_get/">wdb_attr_get</a><code>(3), <a href="/docs/linux/man/3-wdbr_find/">wdbr_find</a></code>(3), <a href="/docs/linux/man/3-wdbr_lookup/">wdbr_lookup</a><code>(3), <a href="/docs/linux/man/3-wdb_create/">wdb_create</a></code>(3), <a href="/docs/linux/man/3-wdbc_destroy/">wdbc_destroy</a><code>(3), wdb_column_update</code> </p>
