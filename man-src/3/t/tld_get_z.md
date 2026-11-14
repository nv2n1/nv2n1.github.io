---
title: "tld_get_z(3)"
name: "tld_get_z"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tld_get_z/"
description: "tld_get_z – API function"
---

<p>tld_get_z &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tld.h&gt;
int tld_get_z(const char *in, char **out);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>const char * in</p>
<dd>Zero terminated character array to process.</p>
<dt>char ** out</p>
<dd>Zero terminated ascii result string pointer.</dl>
<h2>Description</h2>
<p>Isolate the top-level domain of <i>in</i> and return it as an ASCII string in <i>out</i>. The input string <i>in</i> may be UTF-8, ISO-8859-1 or any ASCII compatible character encoding.</p>
<h2>Return Value</h2>
<p>Return <code>TLD_SUCCESS</code> on success, or the corresponding <code>Tld_rc</code> error code otherwise.</p>
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
