---
title: "ksize(9)"
name: "ksize"
section: "9"
letter: "k"
url: "/docs/linux/man/9-ksize/"
description: "ksize – get the actual amount of memory allocated for a given object"
---

<p>ksize &#8211; get the actual amount of memory allocated for a given object</p>
<h2>Synopsis</h2>
<pre><code>size_t ksize(const void *objp);</code></pre>
<h2>Arguments</h2>
<p><i>objp</i></p>
<dl>
<dd>
<dd>Pointer to the object</dl>
<h2>Description</h2>
<p>kmalloc may internally round up allocations and return more memory than requested. <code>ksize</code> can be used to determine the actual amount of memory allocated. The caller may use this additional memory, even though a smaller amount of memory was initially specified with the kmalloc call. The caller must guarantee that objp points to a valid object previously allocated with either <code>kmalloc</code> or <code>kmem_cache_alloc</code>. The object must not be freed during the duration of the call.</p>
<h2>Copyright</h2>
