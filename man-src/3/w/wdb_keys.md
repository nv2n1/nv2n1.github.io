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
<p>primary_key &#8211; pointer to the primary key<br/>
 data &#8211; pointer to a ULIST of the columns.<br/>
 both of these are allocated structures, you can clear data<br/>
 with uListDestroy (data, ULIST_FREE) </p>
<h2>See Also</h2>
<p><code>wdb_destroy</code>(3), wdbr_delete<code>(3), wdb_update</code>(3), wdbr_dump<code>(3), wdb_save</code>(3), wdbr_create<code>(3), wdbr_destroy</code>(3), wdb_attr_set<code>(3), wdb_attr_next</code>(3), wdb_open<code>(3), wdb_column_exchange</code>(3), wdbr_set<code>(3), wdb_column_insert</code>(3), wdbr_save<code>(3), wdbr_next</code>(3), <a href="/docs/linux/man/3-wdb_keys/">wdb_keys</a><code>(3), wdb_column_delete</code>(3), wdbc_create<code>(3), wdbr_get</code>(3), wdb_attr_get<code>(3), wdbr_find</code>(3), wdbr_lookup<code>(3), wdb_create</code>(3), wdbc_destroy<code>(3), wdb_column_update</code> </p>
