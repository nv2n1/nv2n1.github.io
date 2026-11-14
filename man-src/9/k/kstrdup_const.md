---
title: "kstrdup_const(9)"
name: "kstrdup_const"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kstrdup_const/"
description: "kstrdup_const – conditionally duplicate an existing const string"
---

<p>kstrdup_const &#8211; conditionally duplicate an existing const string</p>
<h2>Synopsis</h2>
<pre><code>const char *kstrdup_const(const char *s, gfp_t gfp);</code></pre>
<h2>Arguments</h2>
<p><i>s</i></p>
<dl>
<dd>
<dd>the string to duplicate</dl>
<p> <i>gfp</i></p>
<dl>
<dd>the GFP mask used in the <code>kmalloc</code> call when allocating memory</dl>
<h2>Description</h2>
<p>Function returns source string if it is in .rodata section otherwise it fallbacks to kstrdup. Strings allocated by kstrdup_const should be freed by kfree_const.</p>
<h2>Copyright</h2>
