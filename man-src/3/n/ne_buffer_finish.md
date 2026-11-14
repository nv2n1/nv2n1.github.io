---
title: "ne_buffer_finish(3)"
name: "ne_buffer_finish"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_buffer_finish/"
description: "ne_buffer_destroy, ne_buffer_finish – destroy a buffer object"
---

<p>ne_buffer_destroy, ne_buffer_finish &#8211; destroy a buffer object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_string.h&gt;

void ne_buffer_destroy(ne_buffer *buf);

char *ne_buffer_finish(ne_buffer *buf);</code></pre>
<h2>Description</h2>
<p><code>ne_buffer_destroy</code></p>
<dd>frees all memory associated with the buffer. <code>ne_buffer_finish</code> frees the buffer structure, but not the actual string stored in the buffer, which is returned and must be <code>free</code>()d by the caller. </p>
<p> Any use of the buffer object after calling either of these functions gives undefined behaviour.</p>
<h2>Return Value</h2>
<p><code>ne_buffer_finish</code> returns the <code>malloc</code>-allocated string stored in the buffer.</p>
<h2>Examples</h2>
<p>An example use of <code>ne_buffer_finish</code>; the <code>duplicate</code> function returns a string made up of <i>n</i> copies of <i>str</i>: </p>
<pre><code>static char *duplicate(int n, const char *str)
{
    ne_buffer *buf = ne_buffer_create();
    while (n--) {
        ne_buffer_zappend(buf, str);
    }
    return ne_buffer_finish(buf);
}</code></pre>
<h2>See Also</h2>
<p>ne_buffer, ne_buffer_create, ne_buffer_zappend</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
