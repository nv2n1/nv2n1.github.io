---
title: "oath_strerror_name(3)"
name: "oath_strerror_name"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_strerror_name/"
description: "oath_strerror_name – API function"
---

<p>oath_strerror_name &#8211; API function</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;oath.h&gt;</code> </p>
<p> <code>const char * oath_strerror_name(int </code><i>err</i><code>);</code></p>
<h2>Arguments</h2>
<dl COMPACT>
<dt>int err</p>
<dd> liboath error code</dl>
<h2>Description</h2>
<p> Convert return code to human readable string representing the error code symbol itself. For example, oath_strerror_name(<code>OATH_OK</code>) returns the string &quot;OATH_OK&quot;. </p>
<p> This string can be used to output a diagnostic message to the user. </p>
<p> This function is one of few in the library that can be used without a successful call to <code>oath_init()</code>.</p>
<h2>Return Value</h2>
<p> Returns a pointer to a statically allocated string containing a string version of the error code <i>err</i>, or NULL if the error code is not known.</p>
<h2>Since</h2>
<p> 1.8.0</p>
<h2>Reporting Bugs</h2>
<p> Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p> Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
