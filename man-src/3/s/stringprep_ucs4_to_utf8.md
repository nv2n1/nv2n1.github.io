---
title: "stringprep_ucs4_to_utf8(3)"
name: "stringprep_ucs4_to_utf8"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_ucs4_to_utf8/"
description: "stringprep_ucs4_to_utf8 – API function"
---

<p>stringprep_ucs4_to_utf8 &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;
char *stringprep_ucs4_to_utf8(const uint32_t *str, ssize_t len, size_t *items_read, size_t *items_written);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const uint32_t * str</p>
<dd>a UCS-4 encoded string</p>
<dt>ssize_t len</p>
<dd>the maximum length of <i>str</i> to use. If <i>len</i> &lt; 0, then the string is terminated with a 0 character.</p>
<dt>size_t * items_read</p>
<dd>location to store number of characters read read, or <code>NULL</code>.</p>
<dt>size_t * items_written</p>
<dd>location to store number of bytes written or <code>NULL</code>. The value here stored does not include the trailing 0 byte.</dl>
<h2>Description</h2>
<p>Convert a string from a 32-bit fixed width representation as UCS-4. to UTF-8. The result will be terminated with a 0 byte.</p>
<h2>Return Value</h2>
<p>a pointer to a newly allocated UTF-8 string. This value must be deallocated by the caller. If an error occurs, <code>NULL</code> will be returned.</p>
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
