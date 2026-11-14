---
title: "vm_unmap_ram(9)"
name: "vm_unmap_ram"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vm_unmap_ram/"
---

vm_unmap_ram - unmap linear kernel address space set up by vm_map_ram

<h2>Synopsis</h2>

<pre><code>void vm_unmap_ram(const void *mem, unsigned int count);</code></pre>

<h2>Arguments</h2>

<i>mem</i>
<dl><dd><dd>the pointer returned by vm_map_ram</dl>
 

 <i>count</i>
<dl><dd>the count passed to that vm_map_ram call (cannot unmap partial)</dl>

<h2>Copyright</h2>


