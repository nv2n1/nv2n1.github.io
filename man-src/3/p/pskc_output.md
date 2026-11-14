---
title: "pskc_output(3)"
name: "pskc_output"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_output/"
description: "pskc_output – API function"
---

<p>pskc_output &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
int pskc_output(pskc_t *container, pskc_output_formats_t format, char **out, size_t *len);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_t * container</p>
<dd>a <code>pskc_t</code> handle, from <code>pskc_init()</code>.</p>
<dt>pskc_output_formats_t format</p>
<dd>an <code>pskc_output_formats_t</code> enumeration type indicating format.</p>
<dt>char ** out</p>
<dd>pointer to output variable holding newly allocated string.</p>
<dt>size_t * len</p>
<dd>pointer to output variable hold length of *<i>out</i>.</dl>
<h2>Description</h2>
<p>Convert PSKC data to a serialized string of the indicated type. This is usually used to convert the PSKC data to some human readable form.</p>
<h2>Returns</h2>
<p><code>PSKC_OK</code> on success, or an error code.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
