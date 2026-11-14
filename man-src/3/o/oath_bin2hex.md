---
title: "oath_bin2hex(3)"
name: "oath_bin2hex"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_bin2hex/"
---

oath_bin2hex - API function

<h2>Synopsis</h2>

<pre><code>#include &lt;oath.h&gt;
void oath_bin2hex(const char *binstr, size_t binlen, char *hexstr);</code></pre>

<h2>Arguments</h2>

<dl><dt>const char * binstr
<dd>input binary data
<dt>size_t binlen
<dd>length of input binary data <i>binstr</i>
<dt>char * hexstr
<dd>output string with hex data, must have room for 2*<i>binlen</i>+1.</dl>

<h2>Description</h2>

Convert binary data to NUL-terminated string with hex data. The output <i>hexstr</i> is allocated by the caller and must have room for at least 2*<i>binlen</i>+1, to make room for the encoded data and the terminating NUL byte.

<h2>Since</h2>

1.12.0

<h2>Reporting Bugs</h2>

Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" HREF="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" HREF="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>

<h2>Copyright</h2>

Copyright &#169; 2009-2012 Simon Josefsson. 
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.
