---
title: "pskc_global_init(3)"
name: "pskc_global_init"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_global_init/"
description: "pskc_global_init – API function"
---

<p>pskc_global_init &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
int pskc_global_init(void);</code></pre>
<h2>Arguments</h2>
<dl>
<dt> void</p>
<dd></dl>
<h2>Description</h2>
<p>This function initializes the PSKC library. Every user of this library needs to call this function before using other functions. You should call <code>pskc_global_done()</code> when use of the PSKC library is no longer needed.</p>
<h2>Returns</h2>
<p>On success, <code>PSKC_OK</code> (zero) is returned, otherwise an error code is returned.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
