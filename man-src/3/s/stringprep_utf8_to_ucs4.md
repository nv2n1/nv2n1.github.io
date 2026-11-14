---
title: "stringprep_utf8_to_ucs4(3)"
name: "stringprep_utf8_to_ucs4"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_utf8_to_ucs4/"
description: "stringprep_utf8_to_ucs4 – API function"
---

<p>stringprep_utf8_to_ucs4 &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;</code></pre>
<p> <code>uint32_t * stringprep_utf8_to_ucs4(const char * </code><i>str</i><code>, ssize_t </code><i>len</i><code>, size_t * </code><i>items_written</i><code>);</code></p>
<h2>Arguments</h2>
<dl>
<dt>const char * str</p>
<dd>a UTF-8 encoded string</p>
<dt>ssize_t len</p>
<dd>the maximum length of <i>str</i> to use. If <i>len</i> &lt; 0, then the string is nul-terminated.</p>
<dt>size_t * items_written</p>
<dd>location to store the number of characters in the result, or <code>NULL</code>.</dl>
<h2>Description</h2>
<p>Convert a string from UTF-8 to a 32-bit fixed width representation as UCS-4, assuming valid UTF-8 input. This function does no error checking on the input.</p>
<h2>Return Value</h2>
<p>a pointer to a newly allocated UCS-4 string. This value must be deallocated by the caller.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-libidn [at] gnu.org&gt;. GNU Libidn home page: <a rel="nofollow" href="http://www.gnu.org/software/libidn/">http://www.gnu.org/software/libidn/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2002-2013 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>See Also</h2>
<p>The full documentation for <code>libidn</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libidn</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info libidn</code></dl>
<p> should give you access to the complete manual. </p>
