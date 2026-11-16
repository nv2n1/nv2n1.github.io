---
title: "rio_unmap_outb_region(9)"
name: "rio_unmap_outb_region"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_unmap_outb_region/"
description: "rio_unmap_outb_region – – Unmap the inbound memory region"
---

<p>rio_unmap_outb_region &#8211; &#8211; Unmap the inbound memory region</p>
<h2>Synopsis</h2>
<pre><code>void rio_unmap_outb_region(struct rio_mport *mport, u16 destid, u64 rstart);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
</dd><dd>Master port</dd></dl>
<p> <i>destid</i></p>
<dl>
<dd>destination id mapping points to</dd></dl>
<p> <i>rstart</i></p>
<dl>
<dd>RIO base address window translates to</dd></dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
