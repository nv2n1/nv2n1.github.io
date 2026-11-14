---
title: "vm_insert_page(9)"
name: "vm_insert_page"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vm_insert_page/"
description: "vm_insert_page – insert single page into user vma"
---

<p>vm_insert_page &#8211; insert single page into user vma</p>
<h2>Synopsis</h2>
<pre><code>int vm_insert_page(struct vm_area_struct *vma, unsigned long addr, struct page *page);</code></pre>
<h2>Arguments</h2>
<p><i>vma</i></p>
<dl>
<dd>
<dd>user vma to map to</dl>
<p> <i>addr</i></p>
<dl>
<dd>target user address of this page</dl>
<p> <i>page</i></p>
<dl>
<dd>source kernel page</dl>
<h2>Description</h2>
<p>This allows drivers to insert individual pages they&#8217;ve allocated into a user vma. </p>
<p> The page has to be a nice clean _individual_ kernel allocation. If you allocate a compound page, you need to have marked it as such (__GFP_COMP), or manually just split the page up yourself (see <code>split_page</code>). </p>
<p> NOTE! Traditionally this was done with &#8220;<code>remap_pfn_range</code>&#8221; which took an arbitrary page protection parameter. This doesn&#8217;t allow that. Your vma protection will have to be set up correctly, which means that if you want a shared writable mapping, you&#8217;d better ask for a shared writable mapping! </p>
<p> The page does not need to be reserved. </p>
<p> Usually this function is called from f_op-&gt;<code>mmap</code> handler under mm-&gt;mmap_sem write-lock, so it can change vma-&gt;vm_flags. Caller must set VM_MIXEDMAP on vma if it wants to call this function from other places, for example from page-fault handler.</p>
<h2>Copyright</h2>
