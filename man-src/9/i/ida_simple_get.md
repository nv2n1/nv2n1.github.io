---
title: "ida_simple_get(9)"
name: "ida_simple_get"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ida_simple_get/"
description: "ida_simple_get – get a new id."
---

<p>ida_simple_get &#8211; get a new id.</p>
<h2>Synopsis</h2>
<pre><code>int ida_simple_get(struct ida *ida, unsigned int start, unsigned int end, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>ida</i></p>
<dl>
<dd>
<dd>the (initialized) ida.</dl>
<p> <i>start</i></p>
<dl>
<dd>the minimum id (inclusive, &lt; 0x8000000)</dl>
<p> <i>end</i></p>
<dl>
<dd>the maximum id (exclusive, &lt; 0x8000000 or 0)</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>memory allocation flags</dl>
<h2>Description</h2>
<p>Allocates an id in the range start &lt;= id &lt; end, or returns -ENOSPC. On memory allocation failure, returns -ENOMEM. </p>
<p> Use <code>ida_simple_remove</code> to get rid of an id.</p>
<h2>Copyright</h2>
