---
title: "stringprep_utf8_to_unichar(3)"
name: "stringprep_utf8_to_unichar"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_utf8_to_unichar/"
description: "stringprep_utf8_to_unichar – API function"
---

<p>stringprep_utf8_to_unichar &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;</code></pre>
<p> <code>uint32_t stringprep_utf8_to_unichar(const char * </code><i>p</i><code>);</code></p>
<h2>Arguments</h2>
<dl>
<dt>const char * p</p>
<dd>a pointer to Unicode character encoded as UTF-8</dl>
<h2>Description</h2>
<p>Converts a sequence of bytes encoded as UTF-8 to a Unicode character. If <i>p</i> does not point to a valid UTF-8 encoded character, results are undefined.</p>
<h2>Return Value</h2>
<p>the resulting character.</p>
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
