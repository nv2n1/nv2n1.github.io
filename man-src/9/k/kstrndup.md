---
title: "kstrndup(9)"
name: "kstrndup"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kstrndup/"
description: "kstrndup – allocate space for and copy an existing string"
---

<p>kstrndup &#8211; allocate space for and copy an existing string</p>
<h2>Synopsis</h2>
<pre><code>char *kstrndup(const char *s, size_t max, gfp_t gfp);</code></pre>
<h2>Arguments</h2>
<p><i>s</i></p>
<dl>
<dd>
<dd>the string to duplicate</dl>
<p> <i>max</i></p>
<dl>
<dd>read at most <i>max</i> chars from <i>s</i></dl>
<p> <i>gfp</i></p>
<dl>
<dd>the GFP mask used in the <code>kmalloc</code> call when allocating memory</dl>
<h2>Copyright</h2>
