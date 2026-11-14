---
title: "ne_buffer_append(3)"
name: "ne_buffer_append"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_buffer_append/"
description: "ne_buffer_append, ne_buffer_zappend, ne_buffer_concat – append data to a string buffer"
---

<p>ne_buffer_append, ne_buffer_zappend, ne_buffer_concat &#8211; append data to a string buffer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_string.h&gt;

void ne_buffer_append(ne_buffer *buf, const char *string, size_t len);

void ne_buffer_zappend(ne_buffer *buf, const char *string);

void ne_buffer_concat(ne_buffer *buf, const char *str, ...);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_buffer_append</code> and <code>ne_buffer_zappend</code> functions append a string to the end of a buffer; extending the buffer as necessary. The <i>len</i> passed to <code>ne_buffer_append</code> specifies the length of the string to append; there must be no NUL terminator in the first <i>len</i> bytes of the string. <code>ne_buffer_zappend</code> must be passed a NUL-terminated string. </p>
<p> The <code>ne_buffer_concat</code> function takes a variable-length argument list following <i>str</i>; each argument must be a <code>char *</code> pointer to a NUL-terminated string. A NULL pointer must be given as the last argument to mark the end of the list. The strings (including <i>str</i>) are appended to the buffer in the order given. None of the strings passed to <code>ne_buffer_concat</code> are modified.</p>
<h2>Examples</h2>
<p>The following code will output &quot;Hello, world. And goodbye.&quot;. </p>
<pre><code>ne_buffer *buf = ne_buffer_create();
ne_buffer_zappend(buf, &quot;Hello&quot;);
ne_buffer_concat(buf, &quot;, world. &quot;, &quot;And &quot;, &quot;goodbye.&quot;, NULL);
puts(buf-&gt;data);
ne_buffer_destroy(buf);</code></pre>
<h2>See Also</h2>
<p>ne_buffer, ne_buffer_create, ne_buffer_destroy</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
