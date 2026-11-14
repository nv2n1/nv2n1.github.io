---
title: "tld_check_4z(3)"
name: "tld_check_4z"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tld_check_4z/"
description: "tld_check_4z – API function"
---

<p>tld_check_4z &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tld.h&gt;
int tld_check_4z(const uint32_t *in, size_t *errpos, const Tld_table **overrides);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const uint32_t * in</p>
<dd>Zero-terminated array of unicode code points to process.</p>
<dt>size_t * errpos</p>
<dd>Position of offending character is returned here.</p>
<dt>const Tld_table ** overrides</p>
<dd>A <code>Tld_table</code> array of additional domain restriction structures that complement and supersede the built-in information.</dl>
<h2>Description</h2>
<p>Test each of the code points in <i>in</i> for whether or not they are allowed by the information in <i>overrides</i> or by the built-in TLD restriction data. When data for the same TLD is available both internally and in <i>overrides</i>, the information in <i>overrides</i> takes precedence. If several entries for a specific TLD are found, the first one is used. If <i>overrides</i> is <code>NULL</code>, only the built-in information is used. The position of the first offending character is returned in <i>errpos</i>.</p>
<h2>Return Value</h2>
<p>Returns the <code>Tld_rc</code> value <code>TLD_SUCCESS</code> if all code points are valid or when <i>tld</i> is null, <code>TLD_INVALID</code> if a character is not allowed, or additional error codes on general failure conditions.</p>
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
