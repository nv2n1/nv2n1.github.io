---
title: "rio_map_inb_region(9)"
name: "rio_map_inb_region"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_map_inb_region/"
description: "rio_map_inb_region – – Map inbound memory region."
---

<p>rio_map_inb_region &#8211; &#8211; Map inbound memory region.</p>
<h2>Synopsis</h2>
<pre><code>int rio_map_inb_region(struct rio_mport *mport, dma_addr_t local, u64 rbase, u32 size, u32 rflags);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port.</dl>
<p> <i>local</i></p>
<dl>
<dd>physical address of memory region to be mapped</dl>
<p> <i>rbase</i></p>
<dl>
<dd>RIO base address assigned to this window</dl>
<p> <i>size</i></p>
<dl>
<dd>Size of the memory region</dl>
<p> <i>rflags</i></p>
<dl>
<dd>Flags for mapping.</dl>
<h2>Return</h2>
<p>0 &#8212; Success. </p>
<p> This function will create the mapping from RIO space to local memory.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
