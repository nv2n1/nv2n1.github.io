---
title: "ne_buffer(3)"
name: "ne_buffer"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_buffer/"
description: "ne_buffer – string buffer handling"
---

<p>ne_buffer &#8211; string buffer handling</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_string.h&gt;

typedef struct {
    char *data;
    size_t used;
    size_t length;
} ne_buffer;</code></pre>
<h2>Description</h2>
<p>The <code>ne_buffer</code> type represents an expandable memory buffer for holding NUL-terminated strings. The <i>data</i> field points to the beginnning of the string, the length of which is given by the <i>used</i> field. The current size of memory allocated is given by the <i>length</i> field. It is not recommended that the fields of a buffer are manipulated directly. The <i>data</i> pointer may change when the buffer is modified. </p>
<p> A buffer is created using ne_buffer_create or ne_buffer_ncreate, and destroyed using ne_buffer_destroy or ne_buffer_finish. The functions ne_buffer_append, ne_buffer_zappend and ne_buffer_concat are used to append data to a buffer. </p>
<p> If the string referenced by the <i>data</i> pointer is modified directly (rather than using one of the functions listed above), <code>ne_buffer_altered</code> must be called.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
