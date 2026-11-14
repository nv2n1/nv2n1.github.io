---
title: "hdb_entry_ex(3)"
name: "hdb_entry_ex"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hdb_entry_ex/"
description: "hdb_entry_ex –"
---

<h2 class="name">NAME</h2>
<p> hdb_entry_ex &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hdb.h&gt;</p>
<h2>Detailed Description</h2>
<p> <code>hdb_entry_ex</code> is a wrapper structure around the hdb_entry structure that allows backends to keep a pointer to the backing store, ie in -&gt;hdb_fetch_kvno(), so that we the kadmin/kpasswd backend gets around to -&gt;hdb_store(), the backend doesn&#8217;t need to lookup the entry again. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalhdblibrary from the source code. </p>
<h2>Index</h2>
