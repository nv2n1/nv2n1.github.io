---
title: "unmap_kernel_range_noflush(9)"
name: "unmap_kernel_range_noflush"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unmap_kernel_range_noflush/"
description: "unmap_kernel_range_noflush – unmap kernel VM area"
---

<p>unmap_kernel_range_noflush &#8211; unmap kernel VM area</p>
<h2>Synopsis</h2>
<pre><code>void unmap_kernel_range_noflush(unsigned long addr, unsigned long size);</code></pre>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>start of the VM area to unmap</dl>
<p> <i>size</i></p>
<dl>
<dd>size of the VM area to unmap</dl>
<h2>Description</h2>
<p>Unmap PFN_UP(<i>size</i>) pages at <i>addr</i>. The VM area <i>addr</i> and <i>size</i> specify should have been allocated using <code>get_vm_area</code> and its friends.</p>
<h2>Note</h2>
<p>This function does NOT do any cache flushing. The caller is responsible for calling <code>flush_cache_vunmap</code> on to-be-mapped areas before calling this function and <code>flush_tlb_kernel_range</code> after.</p>
<h2>Copyright</h2>
