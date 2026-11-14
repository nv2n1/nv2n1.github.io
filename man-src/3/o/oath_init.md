---
title: "oath_init(3)"
name: "oath_init"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_init/"
description: "oath_init – API function"
---

<p>oath_init &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;oath.h&gt;
int oath_init(void);</code></pre>
<h2>Arguments</h2>
<dl>
<dt> void</p>
<dd></dl>
<h2>Description</h2>
<p>This function initializes the OATH library. Every user of this library needs to call this function before using other functions. You should call <code>oath_done()</code> when use of the OATH library is no longer needed. </p>
<p> Note that this function may also initialize Libgcrypt, if the OATH library is built with libgcrypt support and libgcrypt has not been initialized before. Thus if you want to manually initialize libgcrypt you must do it before calling this function. This is useful in cases you want to disable libgcrypt&#8217;s internal lockings etc.</p>
<h2>Returns</h2>
<p>On success, <code>OATH_OK</code> (zero) is returned, otherwise an error code is returned.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
