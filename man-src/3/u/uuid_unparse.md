---
title: "uuid_unparse(3)"
name: "uuid_unparse"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uuid_unparse/"
description: "uuid_unparse – convert a UUID from binary representation to a string"
---

<p>uuid_unparse &#8211; convert a UUID from binary representation to a string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;uuid.h&gt;
void uuid_unparse(uuid_t uu, char *out);
void uuid_unparse_upper(uuid_t uu, char *out);
void uuid_unparse_lower(uuid_t uu, char *out);</code></pre>
<h2>Description</h2>
<p>The <code>uuid_unparse</code> function converts the supplied UUID <i>uu</i> from the binary representation into a 36-byte string (plus trailing &#8216;\0&#8217;) of the form 1b4e28ba-2fa1-11d2-883f-0016d3cca427 and stores this value in the character string pointed to by <i>out</i>. The case of the hex digits returned by <code>uuid_unparse</code> may be upper or lower case, and is dependent on the system-dependent local default. </p>
<p> If the case of the hex digits is important then the functions <code>uuid_unparse_upper</code> and <code>uuid_unparse_lower</code> may be used.  </p>
<h2>CONFORMING TO</h2>
<p> This library unparses UUIDs compatible with OSF DCE 1.1.  </p>
<h2>AUTHOR</h2>
<p> Theodore Y. Ts&#8217;o  </p>
<h2>AVAILABILITY</h2>
<p> <code>libuuid</code> is part of the util-linux package since version 2.15.1 and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a>  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-uuid/">uuid</a></code>(3), <code><a href="/docs/linux/man/3-uuid_clear/">uuid_clear</a></code>(3), <code><a href="/docs/linux/man/3-uuid_compare/">uuid_compare</a></code>(3), <code><a href="/docs/linux/man/3-uuid_copy/">uuid_copy</a></code>(3), <code><a href="/docs/linux/man/3-uuid_generate/">uuid_generate</a></code>(3), <code><a href="/docs/linux/man/3-uuid_time/">uuid_time</a></code>(3), <code><a href="/docs/linux/man/3-uuid_is_null/">uuid_is_null</a></code>(3), <code><a href="/docs/linux/man/3-uuid_parse/">uuid_parse</a></code>(3) </p>
<h2>Index</h2>
