---
title: "stringprep_convert(3)"
name: "stringprep_convert"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_convert/"
description: "stringprep_convert – API function"
---

<p>stringprep_convert &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;
char *stringprep_convert(const char *str, const char *to_codeset, const char *from_codeset);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * str</p>
<dd>input zero-terminated string.</p>
<dt>const char * to_codeset</p>
<dd>name of destination character set.</p>
<dt>const char * from_codeset</p>
<dd>name of origin character set, as used by <i>str</i>.</dl>
<h2>Description</h2>
<p>Convert the string from one character set to another using the system&#8217;s <code>iconv()</code> function.</p>
<h2>Return Value</h2>
<p>Returns newly allocated zero-terminated string which is <i>str</i> transcoded into to_codeset.</p>
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
