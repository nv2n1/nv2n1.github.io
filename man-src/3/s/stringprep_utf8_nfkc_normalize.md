---
title: "stringprep_utf8_nfkc_normalize(3)"
name: "stringprep_utf8_nfkc_normalize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_utf8_nfkc_normalize/"
description: "stringprep_utf8_nfkc_normalize – API function"
---

<p>stringprep_utf8_nfkc_normalize &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;
char *stringprep_utf8_nfkc_normalize(const char *str, ssize_t len);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * str</p>
<dd>a UTF-8 encoded string.</p>
<dt>ssize_t len</p>
<dd>length of <i>str</i>, in bytes, or -1 if <i>str</i> is nul-terminated.</dl>
<h2>Description</h2>
<p>Converts a string into canonical form, standardizing such issues as whether a character with an accent is represented as a base character and combining accent or as a single precomposed character. </p>
<p> The normalization mode is NFKC (ALL COMPOSE). It standardizes differences that do not affect the text content, such as the above-mentioned accent representation. It standardizes the &quot;compatibility&quot; characters in Unicode, such as SUPERSCRIPT THREE to the standard forms (in this case DIGIT THREE). Formatting information may be lost but for most text operations such characters should be considered the same. It returns a result with composed forms rather than a maximally decomposed form.</p>
<h2>Return Value</h2>
<p>a newly allocated string, that is the NFKC normalized form of <i>str</i>.</p>
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
