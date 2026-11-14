---
title: "uuid_copy(3)"
name: "uuid_copy"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uuid_copy/"
description: "uuid_copy – copy a UUID value"
---

<p>uuid_copy &#8211; copy a UUID value</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;uuid.h&gt;

void uuid_copy(uuid_t dst, uuid_t src);</code></pre>
<h2>Description</h2>
<p>The <code>uuid_copy</code> function copies the UUID variable <i>src</i> to <i>dst</i>.</p>
<h2>Return Value</h2>
<p>The copied UUID is returned in the location pointed to by <i>dst</i>.</p>
<h2>Author</h2>
<p>Theodore Y. Ts&#8217;o</p>
<h2>Availability</h2>
<p><code>libuuid</code> is part of the util-linux package since version 2.15.1 and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uuid/">uuid</a></code>(3), <code><a href="/docs/linux/man/3-uuid_clear/">uuid_clear</a></code>(3), <code><a href="/docs/linux/man/3-uuid_compare/">uuid_compare</a></code>(3), <code><a href="/docs/linux/man/3-uuid_generate/">uuid_generate</a></code>(3), <code><a href="/docs/linux/man/3-uuid_is_null/">uuid_is_null</a></code>(3), <code><a href="/docs/linux/man/3-uuid_parse/">uuid_parse</a></code>(3), <code><a href="/docs/linux/man/3-uuid_unparse/">uuid_unparse</a></code>(3) </p>
