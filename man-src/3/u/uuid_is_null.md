---
title: "uuid_is_null(3)"
name: "uuid_is_null"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uuid_is_null/"
description: "uuid_is_null – compare the value of the UUID to the NULL value"
---

<p>uuid_is_null &#8211; compare the value of the UUID to the NULL value</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;uuid.h&gt;

int uuid_is_null(uuid_t uu);</code></pre>
<h2>Description</h2>
<p>The <code>uuid_is_null</code> function compares the value of the supplied UUID variable <i>uu</i> to the NULL value. If the value is equal to the NULL UUID, 1 is returned, otherwise 0 is returned.</p>
<h2>Author</h2>
<p>Theodore Y. Ts&#8217;o</p>
<h2>Availability</h2>
<p><code>libuuid</code> is part of the util-linux package since version 2.15.1 and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uuid/">uuid</a></code>(3), <code><a href="/docs/linux/man/3-uuid_clear/">uuid_clear</a></code>(3), <code><a href="/docs/linux/man/3-uuid_compare/">uuid_compare</a></code>(3), <code><a href="/docs/linux/man/3-uuid_copy/">uuid_copy</a></code>(3), <code><a href="/docs/linux/man/3-uuid_generate/">uuid_generate</a></code>(3), <code><a href="/docs/linux/man/3-uuid_time/">uuid_time</a></code>(3), <code><a href="/docs/linux/man/3-uuid_parse/">uuid_parse</a></code>(3), <code><a href="/docs/linux/man/3-uuid_unparse/">uuid_unparse</a></code>(3) </p>
