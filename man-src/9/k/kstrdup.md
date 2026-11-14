---
title: "kstrdup(9)"
name: "kstrdup"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kstrdup/"
description: "kstrdup – allocate space for and copy an existing string"
---

<p>kstrdup &#8211; allocate space for and copy an existing string</p>
<h2>Synopsis</h2>
<pre><code>char *kstrdup(const char *s, gfp_t gfp);</code></pre>
<h2>Arguments</h2>
<p><i>s</i></p>
<dl>
<dd>
<dd>the string to duplicate</dl>
<p> <i>gfp</i></p>
<dl>
<dd>the GFP mask used in the <code>kmalloc</code> call when allocating memory</dl>
<h2>Copyright</h2>
