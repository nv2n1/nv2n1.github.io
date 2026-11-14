---
title: "pskc_global_log(3)"
name: "pskc_global_log"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_global_log/"
description: "pskc_global_log – API function"
---

<p>pskc_global_log &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
void pskc_global_log(pskc_log_func log_func);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_log_func log_func</p>
<dd>new global <code>pskc_log_func</code> log function to use.</dl>
<h2>Description</h2>
<p>Enable global debug logging function. The function will be invoked to print various debugging information. </p>
<p> <i>pskc_log_func</i> is of the form, void (*pskc_log_func) (const char *msg); </p>
<p> The container and keypackage variables may be NULL if they are not relevant for the debug information printed.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
