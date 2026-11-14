---
title: "find_get_entry(9)"
name: "find_get_entry"
section: "9"
letter: "f"
url: "/docs/linux/man/9-find_get_entry/"
description: "find_get_entry – find and get a page cache entry"
---

<p>find_get_entry &#8211; find and get a page cache entry</p>
<h2>Synopsis</h2>
<pre><code>struct page *find_get_entry(struct address_space *mapping, pgoff_t offset);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>the address_space to search</dl>
<p> <i>offset</i></p>
<dl>
<dd>the page cache index</dl>
<h2>Description</h2>
<p>Looks up the page cache slot at <i>mapping</i> &amp; <i>offset</i>. If there is a page cache page, it is returned with an increased refcount. </p>
<p> If the slot holds a shadow entry of a previously evicted page, or a swap entry from shmem/tmpfs, it is returned. </p>
<p> Otherwise, <code>NULL</code> is returned.</p>
<h2>Copyright</h2>
