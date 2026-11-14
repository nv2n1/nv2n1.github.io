---
title: "punycode_strerror(3)"
name: "punycode_strerror"
section: "3"
letter: "p"
url: "/docs/linux/man/3-punycode_strerror/"
description: "punycode_strerror – API function"
---

<p>punycode_strerror &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;punycode.h&gt;
const char *punycode_strerror(Punycode_status rc);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>Punycode_status rc</p>
<dd>an <code>Punycode_status</code> return code.</dl>
<h2>Description</h2>
<p>Convert a return code integer to a text string. This string can be used to output a diagnostic message to the user.</p>
<h2>Punycode_Success</h2>
<p>Successful operation. This value is guaranteed to always be zero, the remaining ones are only guaranteed to hold non-zero values, for logical comparison purposes.</p>
<h2>Punycode_Bad_Input</h2>
<p>Input is invalid.</p>
<h2>Punycode_Big_Output</h2>
<p>Output would exceed the space provided.</p>
<h2>Punycode_Overflow</h2>
<p>Input needs wider integers to process.</p>
<h2>Return Value</h2>
<p>Returns a pointer to a statically allocated string containing a description of the error with the return code <i>rc</i>.</p>
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
