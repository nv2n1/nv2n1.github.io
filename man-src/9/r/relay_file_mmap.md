---
title: "relay_file_mmap(9)"
name: "relay_file_mmap"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_file_mmap/"
description: "relay_file_mmap – mmap file op for relay files"
---

<p>relay_file_mmap &#8211; mmap file op for relay files</p>
<h2>Synopsis</h2>
<pre><code>int relay_file_mmap(struct file *filp, struct vm_area_struct *vma);</code></pre>
<h2>Arguments</h2>
<p><i>filp</i></p>
<dl>
<dd>
<dd>the file</dl>
<p> <i>vma</i></p>
<dl>
<dd>the vma describing what to map</dl>
<h2>Description</h2>
<p>Calls upon <code>relay_mmap_buf</code> to map the file into user space.</p>
<h2>Copyright</h2>
