---
title: "unmap_kernel_range(9)"
name: "unmap_kernel_range"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unmap_kernel_range/"
description: "unmap_kernel_range – unmap kernel VM area and flush cache and TLB"
---

<p>unmap_kernel_range &#8211; unmap kernel VM area and flush cache and TLB</p>
<h2>Synopsis</h2>
<pre><code>void unmap_kernel_range(unsigned long addr, unsigned long size);</code></pre>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>start of the VM area to unmap</dl>
<p> <i>size</i></p>
<dl>
<dd>size of the VM area to unmap</dl>
<h2>Description</h2>
<p>Similar to <code>unmap_kernel_range_noflush</code> but flushes vcache before the unmapping and tlb after.</p>
<h2>Copyright</h2>
