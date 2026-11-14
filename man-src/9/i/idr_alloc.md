---
title: "idr_alloc(9)"
name: "idr_alloc"
section: "9"
letter: "i"
url: "/docs/linux/man/9-idr_alloc/"
description: "idr_alloc – allocate new idr entry"
---

<p>idr_alloc &#8211; allocate new idr entry</p>
<h2>Synopsis</h2>
<pre><code>int idr_alloc(struct idr *idr, void *ptr, int start, int end, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>idr</i></p>
<dl>
<dd>
<dd>the (initialized) idr</dl>
<p> <i>ptr</i></p>
<dl>
<dd>pointer to be associated with the new id</dl>
<p> <i>start</i></p>
<dl>
<dd>the minimum id (inclusive)</dl>
<p> <i>end</i></p>
<dl>
<dd>the maximum id (exclusive, &lt;= 0 for max)</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>memory allocation flags</dl>
<h2>Description</h2>
<p>Allocate an id in [start, end) and associate it with <i>ptr</i>. If no ID is available in the specified range, returns -ENOSPC. On memory allocation failure, returns -ENOMEM. </p>
<p> Note that <i>end</i> is treated as max when &lt;= 0. This is to always allow using <i>start</i> + N as <i>end</i> as long as N is inside integer range. </p>
<p> The user is responsible for exclusively synchronizing all operations which may modify <i>idr</i>. However, read-only accesses such as <code>idr_find</code> or iteration can be performed under RCU read lock provided the user destroys <i>ptr</i> in RCU-safe way after removal from idr.</p>
<h2>Copyright</h2>
