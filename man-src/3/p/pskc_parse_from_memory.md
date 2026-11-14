---
title: "pskc_parse_from_memory(3)"
name: "pskc_parse_from_memory"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_parse_from_memory/"
description: "pskc_parse_from_memory – API function"
---

<p>pskc_parse_from_memory &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
int pskc_parse_from_memory(pskc_t *container, size_t len, const char *buffer);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_t * container</p>
<dd>a <code>pskc_t</code> handle, from <code>pskc_init()</code>.</p>
<dt>size_t len</p>
<dd>length of <i>buffer</i>.</p>
<dt>const char * buffer</p>
<dd>XML data to parse.</dl>
<h2>Description</h2>
<p>This function will parse the XML data in <i>buffer</i> of <i>len</i> size into <i>container</i>. If <code>PSKC_PARSE_ERROR</code> is returned, parsing of some elements have failed but the <i>container</i> is still valid and contain partially parsed information. In this situation, you may continue but raise a warning.</p>
<h2>Returns</h2>
<p>On success, <code>PSKC_OK</code> (zero) is returned, on memory allocation errors <code>PSKC_MALLOC_ERROR</code> is returned, on XML library errors <code>PSKC_XML_ERROR</code> is returned, on PSKC parse errors <code>PSKC_PARSE_ERROR</code> is returned.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
