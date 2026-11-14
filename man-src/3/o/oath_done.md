---
title: "oath_done(3)"
name: "oath_done"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_done/"
description: "oath_done – API function"
---

<p>oath_done &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;oath.h&gt;
int oath_done(void);</code></pre>
<h2>Arguments</h2>
<dl>
<dt> void</p>
<dd></dl>
<h2>Description</h2>
<p>This function deinitializes the OATH library, which were initialized using <code>oath_init()</code>. After calling this function, no other OATH library function may be called except for to re-initialize the library using <code>oath_init()</code>.</p>
<h2>Returns</h2>
<p>On success, <code>OATH_OK</code> (zero) is returned, otherwise an error code is returned.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
