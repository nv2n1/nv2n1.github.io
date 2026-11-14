---
title: "pskc_add_keypackage(3)"
name: "pskc_add_keypackage"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_add_keypackage/"
description: "pskc_add_keypackage – API function"
---

<p>pskc_add_keypackage &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
int pskc_add_keypackage(pskc_t *container, pskc_key_t **key);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_t * container</p>
<dd>a <code>pskc_t</code> handle, from <code>pskc_init()</code>.</p>
<dt>pskc_key_t ** key</p>
<dd>pointer to <code>pskc_key_t</code> key package handle.</dl>
<h2>Description</h2>
<p>Add a new a PSKC keypackage to the <i>container</i> and give back a <code>pskc_key_t</code> handle.</p>
<h2>Returns</h2>
<p><code>PSKC_MALLOC_ERROR</code> on memory allocation errors, or <code>PSKC_OK</code> on success.</p>
<h2>Since</h2>
<p>2.2.0</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
