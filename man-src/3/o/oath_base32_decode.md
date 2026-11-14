---
title: "oath_base32_decode(3)"
name: "oath_base32_decode"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oath_base32_decode/"
description: "oath_base32_decode – API function"
---

<p>oath_base32_decode &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;oath.h&gt;
int oath_base32_decode(const char *in, size_t inlen, char **out, size_t *outlen);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * in</p>
<dd>input string with base32 encoded data of length <i>inlen</i></p>
<dt>size_t inlen</p>
<dd>length of input base32 string <i>in</i></p>
<dt>char ** out</p>
<dd>pointer to output variable for binary data of length <i>outlen</i>, or NULL</p>
<dt>size_t * outlen</p>
<dd>pointer to output variable holding length of <i>out</i>, or NULL</dl>
<h2>Description</h2>
<p>Decode a base32 encoded string into binary data. </p>
<p> Space characters are ignored and pad characters are added if needed. Non-base32 data are not ignored but instead will lead to an <code>OATH_INVALID_BASE32</code> error. </p>
<p> The <i>in</i> parameter should contain <i>inlen</i> bytes of base32 encoded data. The function allocates a new string in *<i>out</i> to hold the decoded data, and sets *<i>outlen</i> to the length of the data. </p>
<p> If <i>out</i> is NULL, then *<i>outlen</i> will be set to what would have been the length of *<i>out</i> on successful encoding. </p>
<p> If the caller is not interested in knowing the length of the output data <i>out</i>, then <i>outlen</i> may be set to NULL. </p>
<p> It is permitted but useless to have both <i>out</i> and <i>outlen</i> NULL.</p>
<h2>Returns</h2>
<p>On success <code>OATH_OK</code> (zero) is returned, <code>OATH_INVALID_BASE32</code> is returned if the input contains non-base32 characters, and <code>OATH_MALLOC_ERROR</code> is returned on memory allocation errors.</p>
<h2>Since</h2>
<p>1.12.0</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. liboath home page: <a rel="nofollow" href="http://www.gnu.org/software/liboath/">http://www.gnu.org/software/liboath/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
