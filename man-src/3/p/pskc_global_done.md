---
title: "pskc_global_done(3)"
name: "pskc_global_done"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_global_done/"
description: "pskc_global_done – API function"
---

<p>pskc_global_done &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
void pskc_global_done(void);</code></pre>
<h2>Arguments</h2>
<dl>
<dt> void</p>
<dd></dl>
<h2>Description</h2>
<p>This function deinitializes the PSKC library, which were initialized using <code>pskc_global_init()</code>. After calling this function, no other PSKC library function may be called except for to re-initialize the library using <code>pskc_global_init()</code>.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
