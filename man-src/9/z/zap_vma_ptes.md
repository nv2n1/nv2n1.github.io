---
title: "zap_vma_ptes(9)"
name: "zap_vma_ptes"
section: "9"
letter: "z"
url: "/docs/linux/man/9-zap_vma_ptes/"
description: "zap_vma_ptes – remove ptes mapping the vma"
---

<p>zap_vma_ptes &#8211; remove ptes mapping the vma</p>
<h2>Synopsis</h2>
<pre><code>int zap_vma_ptes(struct vm_area_struct *vma, unsigned long address, unsigned long size);</code></pre>
<h2>Arguments</h2>
<p><i>vma</i></p>
<dl>
<dd>
<dd>vm_area_struct holding ptes to be zapped</dl>
<p> <i>address</i></p>
<dl>
<dd>starting address of pages to zap</dl>
<p> <i>size</i></p>
<dl>
<dd>number of bytes to zap</dl>
<h2>Description</h2>
<p>This function only unmaps ptes assigned to VM_PFNMAP vmas. </p>
<p> The entire address range must be fully contained within the vma. </p>
<p> Returns 0 if successful.</p>
<h2>Copyright</h2>


