---
title: "relay_alloc_buf(9)"
name: "relay_alloc_buf"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_alloc_buf/"
description: "relay_alloc_buf – allocate a channel buffer"
---

<p>relay_alloc_buf &#8211; allocate a channel buffer</p>
<h2>Synopsis</h2>
<pre><code>void *relay_alloc_buf(struct rchan_buf *buf, size_t *size);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>the buffer struct</dl>
<p> <i>size</i></p>
<dl>
<dd>total size of the buffer</dl>
<h2>Description</h2>
<p>Returns a pointer to the resulting buffer, <code>NULL</code> if unsuccessful. The passed in size will get page aligned, if it isn&#8217;t already.</p>
<h2>Copyright</h2>
