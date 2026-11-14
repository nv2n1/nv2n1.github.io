---
title: "pskc_done(3)"
name: "pskc_done"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_done/"
description: "pskc_done – API function"
---

<p>pskc_done &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
void pskc_done(pskc_t *container);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_t * container</p>
<dd>a <code>pskc_t</code> handle, from <code>pskc_init()</code>.</dl>
<h2>Description</h2>
<p>This function releases the resources associated with the PSKC <i>container</i> handle.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
