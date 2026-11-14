---
title: "filemap_fault(9)"
name: "filemap_fault"
section: "9"
letter: "f"
url: "/docs/linux/man/9-filemap_fault/"
description: "filemap_fault – read in file data for page fault handling"
---

<p>filemap_fault &#8211; read in file data for page fault handling</p>
<h2>Synopsis</h2>
<pre><code>int filemap_fault(struct vm_area_struct *vma, struct vm_fault *vmf);</code></pre>
<h2>Arguments</h2>
<p><i>vma</i></p>
<dl>
<dd>
<dd>vma in which the fault was taken</dl>
<p> <i>vmf</i></p>
<dl>
<dd>struct vm_fault containing details of the fault</dl>
<h2>Description</h2>
<p><code>filemap_fault</code> is invoked via the vma operations vector for a mapped memory region to read in file data during a page fault. </p>
<p> The goto&#8217;s are kind of ugly, but this streamlines the normal case of having it in the page cache, and handles the special cases reasonably without having a lot of duplicated code. </p>
<p> vma-&gt;vm_mm-&gt;mmap_sem must be held on entry. </p>
<p> If our return value has VM_FAULT_RETRY set, it&#8217;s because <code>lock_page_or_retry</code> returned 0. The mmap_sem has usually been released in this case. See <code>__lock_page_or_retry</code> for the exception. </p>
<p> If our return value does not have VM_FAULT_RETRY set, the mmap_sem has not been released. </p>
<p> We never return with VM_FAULT_RETRY and a bit from VM_FAULT_ERROR set.</p>
<h2>Copyright</h2>
