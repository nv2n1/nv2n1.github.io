---
title: "pskc_build_xml(3)"
name: "pskc_build_xml"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_build_xml/"
description: "pskc_build_xml – API function"
---

<p>pskc_build_xml &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
int pskc_build_xml(pskc_t *container, char **out, size_t *len);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_t * container</p>
<dd>a <code>pskc_t</code> handle, from <code>pskc_init()</code>.</p>
<dt>char ** out</p>
<dd>pointer to output variable to hold newly allocated string.</p>
<dt>size_t * len</p>
<dd>output variable holding length of *<i>out</i>.</dl>
<h2>Description</h2>
<p>This function builds a XML file from the data in <i>container</i>. As a convenience, it also converts the XML into a string placed in the newly allocated *<i>out</i> of length <i>len</i> using <code>pskc_output()</code> with <code>PSKC_OUTPUT_XML</code>.</p>
<h2>Returns</h2>
<p>On success, <code>PSKC_OK</code> (zero) is returned, on memory allocation errors <code>PSKC_MALLOC_ERROR</code> is returned.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
