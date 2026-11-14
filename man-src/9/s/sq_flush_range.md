---
title: "sq_flush_range(9)"
name: "sq_flush_range"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sq_flush_range/"
description: "sq_flush_range – Flush (prefetch) a specific SQ range"
---

<p>sq_flush_range &#8211; Flush (prefetch) a specific SQ range</p>
<h2>Synopsis</h2>
<pre><code>void sq_flush_range(unsigned long start, unsigned int len);</code></pre>
<h2>Arguments</h2>
<p><i>start</i></p>
<dl>
<dd>
<dd>the store queue address to start flushing from</dl>
<p> <i>len</i></p>
<dl>
<dd>the length to flush</dl>
<h2>Description</h2>
<p>Flushes the store queue cache from <i>start</i> to <i>start</i> + <i>len</i> in a linear fashion.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
