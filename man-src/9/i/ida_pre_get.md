---
title: "ida_pre_get(9)"
name: "ida_pre_get"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ida_pre_get/"
description: "ida_pre_get – reserve resources for ida allocation"
---

<p>ida_pre_get &#8211; reserve resources for ida allocation</p>
<h2>Synopsis</h2>
<pre><code>int ida_pre_get(struct ida *ida, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>ida</i></p>
<dl>
<dd>
<dd>ida handle</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>memory allocation flag</dl>
<h2>Description</h2>
<p>This function should be called prior to locking and calling the following function. It preallocates enough memory to satisfy the worst possible allocation. </p>
<p> If the system is REALLY out of memory this function returns <code>0</code>, otherwise <code>1</code>.</p>
<h2>Copyright</h2>
