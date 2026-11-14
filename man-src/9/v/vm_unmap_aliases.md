---
title: "vm_unmap_aliases(9)"
name: "vm_unmap_aliases"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vm_unmap_aliases/"
---

vm_unmap_aliases - unmap outstanding lazy aliases in the vmap layer

<h2>Synopsis</h2>

<pre><code>void vm_unmap_aliases(void);</code></pre>

<h2>Arguments</h2>

<i>void</i>
<dl><dd><dd>no arguments</dl>

<h2>Description</h2>

The vmap/vmalloc layer lazily flushes kernel virtual mappings primarily to amortize TLB flushing overheads. What this means is that any page you have now, may, in a former life, have been mapped into kernel virtual address by the vmap layer and so there might be some CPUs with TLB entries still referencing that page (additional to the regular 1:1 kernel mapping). 

 vm_unmap_aliases flushes all such lazy mappings. After it returns, we can be sure that none of the pages we have control over will have any aliases from the vmap layer.

<h2>Copyright</h2>


