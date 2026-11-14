---
title: "stringprep_ucs4_nfkc_normalize(3)"
name: "stringprep_ucs4_nfkc_normalize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_ucs4_nfkc_normalize/"
description: "stringprep_ucs4_nfkc_normalize – API function"
---

<p>stringprep_ucs4_nfkc_normalize &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;</code></pre>
<p> <code>uint32_t * stringprep_ucs4_nfkc_normalize(const uint32_t * </code><i>str</i><code>, ssize_t </code><i>len</i><code>);</code></p>
<h2>Arguments</h2>
<dl>
<dt>const uint32_t * str</p>
<dd>a Unicode string.</p>
<dt>ssize_t len</p>
<dd>length of <i>str</i> array, or -1 if <i>str</i> is nul-terminated.</dl>
<h2>Description</h2>
<p>Converts a UCS4 string into canonical form, see <code>stringprep_utf8_nfkc_normalize()</code> for more information.</p>
<h2>Return Value</h2>
<p>a newly allocated Unicode string, that is the NFKC normalized form of <i>str</i>.</p>
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
