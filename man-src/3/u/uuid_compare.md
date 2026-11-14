---
title: "uuid_compare(3)"
name: "uuid_compare"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uuid_compare/"
description: "uuid_compare – compare whether two UUIDs are the same"
---

<p>uuid_compare &#8211; compare whether two UUIDs are the same</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;uuid.h&gt;

int uuid_compare(uuid_t uu1, uuid_t uu2)</code></pre>
<h2>Description</h2>
<p>The <code>uuid_compare</code> function compares the two supplied uuid variables <i>uu1</i> and <i>uu2</i> to each other.</p>
<h2>Return Value</h2>
<p>Returns an integer less than, equal to, or greater than zero if <i>uu1</i> is found, respectively, to be lexicographically less than, equal, or greater than <i>uu2</i>.</p>
<h2>Author</h2>
<p>Theodore Y. Ts&#8217;o</p>
<h2>Availability</h2>
<p><code>libuuid</code> is part of the util-linux package since version 2.15.1 and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uuid/">uuid</a></code>(3), <code><a href="/docs/linux/man/3-uuid_clear/">uuid_clear</a></code>(3), <code><a href="/docs/linux/man/3-uuid_copy/">uuid_copy</a></code>(3), <code><a href="/docs/linux/man/3-uuid_generate/">uuid_generate</a></code>(3), <code><a href="/docs/linux/man/3-uuid_is_null/">uuid_is_null</a></code>(3), <code><a href="/docs/linux/man/3-uuid_parse/">uuid_parse</a></code>(3), <code><a href="/docs/linux/man/3-uuid_unparse/">uuid_unparse</a></code>(3) </p>
