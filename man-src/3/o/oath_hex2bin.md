---
title: "oath_hex2bin(3)"
name: "oath_hex2bin"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_hex2bin/"
description: "oath_hex2bin – API function"
---

<p>oath_hex2bin &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;oath.h&gt;
int oath_hex2bin(const char *hexstr, char *binstr, size_t *binlen);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * hexstr</p>
<dd>input string with hex data</p>
<dt>char * binstr</p>
<dd>output string that holds binary data, or NULL</p>
<dt>size_t * binlen</p>
<dd>output variable holding needed length of <i>binstr</i></dl>
<h2>Description</h2>
<p>Convert string with hex data to binary data. </p>
<p> Non-hexadecimal data are not ignored but instead will lead to an <code>OATH_INVALID_HEX</code> error. </p>
<p> If <i>binstr</i> is NULL, then <i>binlen</i> will be populated with the necessary length. If the <i>binstr</i> buffer is too small, <code>OATH_TOO_SMALL_BUFFER</code> is returned and <i>binlen</i> will contain the necessary length.</p>
<h2>Returns</h2>
<p>On success, <code>OATH_OK</code> (zero) is returned, otherwise an error code is returned.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
