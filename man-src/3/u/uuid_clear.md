---
title: "uuid_clear(3)"
name: "uuid_clear"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uuid_clear/"
description: "uuid_clear – reset value of UUID variable to the NULL value"
---

<p>uuid_clear &#8211; reset value of UUID variable to the NULL value</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;uuid.h&gt;

void uuid_clear(uuid_t uu);</code></pre>
<h2>Description</h2>
<p>The <code>uuid_clear</code> function sets the value of the supplied uuid variable <i>uu</i> to the NULL value.</p>
<h2>Author</h2>
<p>Theodore Y. Ts&#8217;o</p>
<h2>Availability</h2>
<p><code>libuuid</code> is part of the util-linux package since version 2.15.1 and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uuid/">uuid</a></code>(3), <code><a href="/docs/linux/man/3-uuid_compare/">uuid_compare</a></code>(3), <code><a href="/docs/linux/man/3-uuid_copy/">uuid_copy</a></code>(3), <code><a href="/docs/linux/man/3-uuid_generate/">uuid_generate</a></code>(3), <code><a href="/docs/linux/man/3-uuid_is_null/">uuid_is_null</a></code>(3), <code><a href="/docs/linux/man/3-uuid_parse/">uuid_parse</a></code>(3), <code><a href="/docs/linux/man/3-uuid_unparse/">uuid_unparse</a></code>(3) </p>
