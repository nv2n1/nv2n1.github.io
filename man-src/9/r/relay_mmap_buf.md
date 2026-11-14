---
title: "relay_mmap_buf(9)"
name: "relay_mmap_buf"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_mmap_buf/"
---

relay_mmap_buf - mmap channel buffer to process address space

<h2>Synopsis</h2>

<pre><code>int relay_mmap_buf(struct rchan_buf *buf, struct vm_area_struct *vma);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>relay channel buffer</dl>
 

 <i>vma</i>
<dl><dd>vm_area_struct describing memory to be mapped</dl>

<h2>Description</h2>

Returns 0 if ok, negative on error 

 Caller should already have grabbed mmap_sem.

<h2>Copyright</h2>


