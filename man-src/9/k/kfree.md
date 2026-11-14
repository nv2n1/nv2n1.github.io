---
title: "kfree(9)"
name: "kfree"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfree/"
description: "kfree – free previously allocated memory"
---

<p>kfree &#8211; free previously allocated memory</p>
<h2>Synopsis</h2>
<pre><code>void kfree(const void *objp);</code></pre>
<h2>Arguments</h2>
<p><i>objp</i></p>
<dl>
<dd>
<dd>pointer returned by kmalloc.</dl>
<h2>Description</h2>
<p>If <i>objp</i> is NULL, no operation is performed. </p>
<p> Don&#8217;t free memory not originally allocated by <code>kmalloc</code> or you will run into trouble.</p>
<h2>Copyright</h2>
