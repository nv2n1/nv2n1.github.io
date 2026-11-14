---
title: "umad_free(3)"
name: "umad_free"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_free/"
description: "umad_free – frees memory of umad buffers"
---

<p>umad_free &#8211; frees memory of umad buffers</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

void umad_free(void *umad);</code></pre>
<h2>Description</h2>
<p><code>umad_free()</code> frees memory previously allocated with <code>umad_alloc()</code>.</p>
<h2>Return Value</h2>
<p><code>umad_free()</code> returns no value.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_alloc/">umad_alloc</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
