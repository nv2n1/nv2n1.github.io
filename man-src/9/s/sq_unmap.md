---
title: "sq_unmap(9)"
name: "sq_unmap"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sq_unmap/"
description: "sq_unmap – Unmap a Store Queue allocation"
---

<p>sq_unmap &#8211; Unmap a Store Queue allocation</p>
<h2>Synopsis</h2>
<pre><code>void sq_unmap(unsigned long vaddr);</code></pre>
<h2>Arguments</h2>
<p><i>vaddr</i></p>
<dl>
<dd>
<dd>Pre-allocated Store Queue mapping.</dl>
<h2>Description</h2>
<p>Unmaps the store queue allocation <i>map</i> that was previously created by <code>sq_remap</code>. Also frees up the pte that was previously inserted into the kernel page table and discards the UTLB translation.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
