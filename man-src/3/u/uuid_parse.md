---
title: "uuid_parse(3)"
name: "uuid_parse"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uuid_parse/"
description: "uuid_parse – convert an input UUID string into binary representation"
---

<p>uuid_parse &#8211; convert an input UUID string into binary representation</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;uuid.h&gt;
int uuid_parse(char *in, uuid_t uu);</code></pre>
<h2>Description</h2>
<p>The <code>uuid_parse</code> function converts the UUID string given by <i>in</i> into the binary representation. The input UUID is a string of the form 1b4e28ba-2fa1-11d2-883f-b9a761bde3fb (in <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) format &quot;%08x-%04x-%04x-%04x-%012x&quot;, 36 bytes plus the trailing &#8216;\0&#8217;).  </p>
<h2>RETURN VALUE</h2>
<p> Upon successfully parsing the input string, 0 is returned, and the UUID is stored in the location pointed to by <i>uu</i>, otherwise -1 is returned.  </p>
<h2>CONFORMING TO</h2>
<p> This library parses UUIDs compatible with OSF DCE 1.1, and hash based UUIDs V3 and V5 compatible with RFC-4122.  </p>
<h2>AUTHOR</h2>
<p> Theodore Y. Ts&#8217;o  </p>
<h2>AVAILABILITY</h2>
<p> <code>libuuid</code> is part of the util-linux package since version 2.15.1 and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a>  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-uuid/">uuid</a></code>(3), <code><a href="/docs/linux/man/3-uuid_clear/">uuid_clear</a></code>(3), <code><a href="/docs/linux/man/3-uuid_compare/">uuid_compare</a></code>(3), <code><a href="/docs/linux/man/3-uuid_copy/">uuid_copy</a></code>(3), <code><a href="/docs/linux/man/3-uuid_generate/">uuid_generate</a></code>(3), <code><a href="/docs/linux/man/3-uuid_is_null/">uuid_is_null</a></code>(3), <code><a href="/docs/linux/man/3-uuid_time/">uuid_time</a></code>(3), <code><a href="/docs/linux/man/3-uuid_unparse/">uuid_unparse</a></code>(3) </p>
<h2>Index</h2>
