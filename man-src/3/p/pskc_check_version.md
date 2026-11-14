---
title: "pskc_check_version(3)"
name: "pskc_check_version"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_check_version/"
description: "pskc_check_version – API function"
---

<p>pskc_check_version &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
const char *pskc_check_version(const char *req_version);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * req_version</p>
<dd>version string to compare with, or NULL.</dl>
<h2>Description</h2>
<p>Check PSKC library version. </p>
<p> See <code>PSKC_VERSION</code> for a suitable <i>req_version</i> string. </p>
<p> This function is one of few in the library that can be used without a successful call to <code>pskc_global_init()</code>.</p>
<h2>Return Value</h2>
<p>Check that the version of the library is at minimum the one given as a string in <i>req_version</i> and return the actual version string of the library; return NULL if the condition is not met. If NULL is passed to this function no check is done and only the version string is returned.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
