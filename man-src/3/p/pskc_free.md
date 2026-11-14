---
title: "pskc_free(3)"
name: "pskc_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_free/"
description: "pskc_free – API function"
---

<p>pskc_free &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
void pskc_free(void *ptr);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>void * ptr</p>
<dd>memory region to deallocate, or NULL.</dl>
<h2>Description</h2>
<p>Deallocates memory region by calling <code>free()</code>. If <i>ptr</i> is NULL no operation is performed. </p>
<p> This function is necessary on Windows, where different parts of the same application may use different memory heaps.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
