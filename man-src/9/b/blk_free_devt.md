---
title: "blk_free_devt(9)"
name: "blk_free_devt"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_free_devt/"
description: "blk_free_devt – free a dev_t"
---

<p>blk_free_devt &#8211; free a dev_t</p>
<h2>Synopsis</h2>
<pre><code>void blk_free_devt(dev_t devt);</code></pre>
<h2>Arguments</h2>
<p><i>devt</i></p>
<dl>
<dd>
<dd>dev_t to free</dl>
<h2>Description</h2>
<p>Free <i>devt</i> which was allocated using <code>blk_alloc_devt</code>.</p>
<h2>Context</h2>
<p>Might sleep.</p>
<h2>Copyright</h2>
