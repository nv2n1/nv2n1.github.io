---
title: "ne_buffer_create(3)"
name: "ne_buffer_create"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_buffer_create/"
description: "ne_buffer_create, ne_buffer_ncreate – create a string buffer"
---

<p>ne_buffer_create, ne_buffer_ncreate &#8211; create a string buffer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_alloc.h&gt;

ne_buffer *ne_buffer_create(void);

ne_buffer *ne_buffer_ncreate(size_t size);</code></pre>
<h2>Description</h2>
<p><code>ne_buffer_create</code></p>
<dd>creates a new buffer object, with an implementation-defined initial size. <code>ne_buffer_ncreate</code> creates an <code>ne_buffer</code> where the minimum initial size is given in the <i>size</i> parameter. The buffer created will contain the empty string (&quot;&quot;).</p>
<h2>Return Value</h2>
<p>Both functions return a pointer to a new buffer object, and never NULL.</p>
<h2>See Also</h2>
<p>ne_buffer</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
