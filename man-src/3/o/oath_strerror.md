---
title: "oath_strerror(3)"
name: "oath_strerror"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_strerror/"
description: "oath_strerror – API function"
---

<p>oath_strerror &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;oath.h&gt;
const char *oath_strerror(int err);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>int err</p>
<dd>liboath error code</dl>
<h2>Description</h2>
<p>Convert return code to human readable string explanation of the reason for the particular error code. </p>
<p> This string can be used to output a diagnostic message to the user. </p>
<p> This function is one of few in the library that can be used without a successful call to <code>oath_init()</code>.</p>
<h2>Return Value</h2>
<p>Returns a pointer to a statically allocated string containing an explanation of the error code <i>err</i>.</p>
<h2>Since</h2>
<p>1.8.0</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
