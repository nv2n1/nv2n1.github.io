---
title: "vunmap(9)"
name: "vunmap"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vunmap/"
description: "vunmap – release virtual mapping obtained by vmap"
---

<p>vunmap &#8211; release virtual mapping obtained by <code>vmap</code></p>
<h2>Synopsis</h2>
<pre><code>void vunmap(const void *addr);</code></pre>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>memory base address</dl>
<h2>Description</h2>
<p>Free the virtually contiguous memory area starting at <i>addr</i>, which was created from the page array passed to <code>vmap</code>. </p>
<p> Must not be called in interrupt context.</p>
<h2>Copyright</h2>
