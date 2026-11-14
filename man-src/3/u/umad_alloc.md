---
title: "umad_alloc(3)"
name: "umad_alloc"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_alloc/"
description: "umad_alloc – allocate memory for umad buffers"
---

<p>umad_alloc &#8211; allocate memory for umad buffers</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

void *umad_alloc(int num, size_t size);</code></pre>
<h2>Description</h2>
<p><code>umad_alloc()</code> allocates memory for an array of <i>num</i> umad buffers of <i>size</i> bytes. Note that <i>size</i> should include the <code>umad_size()</code> plus the length (MAD_BLOCK_SIZE for normal MADs or the length returned from <code>umad_recv()</code> for RMPP MADs).</p>
<h2>Return Value</h2>
<p><code>umad_alloc()</code> returns NULL if out of memory.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_free/">umad_free</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
