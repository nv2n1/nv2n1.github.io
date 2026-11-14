---
title: "vfree(9)"
name: "vfree"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vfree/"
description: "vfree – release memory allocated by vmalloc"
---

<p>vfree &#8211; release memory allocated by <code>vmalloc</code></p>
<h2>Synopsis</h2>
<pre><code>void vfree(const void *addr);</code></pre>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>memory base address</dl>
<h2>Description</h2>
<p>Free the virtually continuous memory area starting at <i>addr</i>, as obtained from <code>vmalloc</code>, <code>vmalloc_32</code> or <code>__vmalloc</code>. If <i>addr</i> is NULL, no operation is performed. </p>
<p> Must not be called in NMI context (strictly speaking, only if we don&#8217;t have CONFIG_ARCH_HAVE_NMI_SAFE_CMPXCHG, but making the calling conventions for <code>vfree</code> arch-depenedent would be a really bad idea)</p>
<h2>Note</h2>
<p>assumes that the object at *addr has a size &gt;= sizeof(llist_node)</p>
<h2>Copyright</h2>
