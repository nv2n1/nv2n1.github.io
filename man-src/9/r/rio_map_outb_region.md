---
title: "rio_map_outb_region(9)"
name: "rio_map_outb_region"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_map_outb_region/"
description: "rio_map_outb_region – – Map outbound memory region."
---

<p>rio_map_outb_region &#8211; &#8211; Map outbound memory region.</p>
<h2>Synopsis</h2>
<pre><code>int rio_map_outb_region(struct rio_mport *mport, u16 destid, u64 rbase, u32 size, u32 rflags, dma_addr_t *local);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port.</dl>
<p> <i>destid</i></p>
<dl>
<dd>destination id window points to</dl>
<p> <i>rbase</i></p>
<dl>
<dd>RIO base address window translates to</dl>
<p> <i>size</i></p>
<dl>
<dd>Size of the memory region</dl>
<p> <i>rflags</i></p>
<dl>
<dd>Flags for mapping.</dl>
<p> <i>local</i></p>
<dl>
<dd>physical address of memory region mapped</dl>
<h2>Return</h2>
<p>0 &#8212; Success. </p>
<p> This function will create the mapping from RIO space to local memory.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
