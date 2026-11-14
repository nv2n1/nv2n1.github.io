---
title: "ne_buffer_clear(3)"
name: "ne_buffer_clear"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_buffer_clear/"
description: "ne_buffer_clear, ne_buffer_grow, ne_buffer_altered – clear, grow, or mark as altered a string buffer"
---

<p>ne_buffer_clear, ne_buffer_grow, ne_buffer_altered &#8211; clear, grow, or mark as altered a string buffer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_string.h&gt;

void ne_buffer_clear(ne_buffer *buf);

void ne_buffer_altered(ne_buffer *buf);

void ne_buffer_grow(ne_buffer *buf, size_t size);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_buffer_clear</code> function sets the string stored in <i>buf</i> to be the empty string (&quot;&quot;). </p>
<p> The <code>ne_buffer_altered</code> function must be used after the string stored in the buffer <i>buf</i> is modified by directly rather than using ne_buffer_append, ne_buffer_zappend or ne_buffer_concat. </p>
<p> The <code>ne_buffer_grow</code> function ensures that at least <i>size</i> bytes are allocated for the string; this can be used if a large amount of data is going to be appended to the buffer and may result in more efficient memory allocation.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
