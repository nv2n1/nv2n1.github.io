---
title: "stringprep_unichar_to_utf8(3)"
name: "stringprep_unichar_to_utf8"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stringprep_unichar_to_utf8/"
description: "stringprep_unichar_to_utf8 – API function"
---

<p>stringprep_unichar_to_utf8 &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stringprep.h&gt;
int stringprep_unichar_to_utf8(uint32_t c, char *outbuf);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>uint32_t c</p>
<dd>a ISO10646 character code</p>
<dt>char * outbuf</p>
<dd>output buffer, must have at least 6 bytes of space. If <code>NULL</code>, the length will be computed and returned and nothing will be written to <i>outbuf</i>.</dl>
<h2>Description</h2>
<p>Converts a single character to UTF-8.</p>
<h2>Return Value</h2>
<p>number of bytes written.</p>
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
