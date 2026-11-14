---
title: "pskc_get_keypackage(3)"
name: "pskc_get_keypackage"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_get_keypackage/"
description: "pskc_get_keypackage – API function"
---

<p>pskc_get_keypackage &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;</code></pre>
<p> <code>pskc_key_t * pskc_get_keypackage(pskc_t * </code><i>container</i><code>, size_t </code><i>i</i><code>);</code></p>
<h2>Arguments</h2>
<dl>
<dt>pskc_t * container</p>
<dd>a <code>pskc_t</code> handle, from <code>pskc_init()</code>.</p>
<dt>size_t i</p>
<dd>number of keypackage to get.</dl>
<h2>Description</h2>
<p>Get a PSKC keypackage <code>pskc_key_t</code> handle for the <i>i</i>&#8216;th key package in <i>container</i>. <i>i</i> is zero-based, i.e., 0 refer to the first key package, 1 refer to the second key package, and so on.</p>
<h2>Returns</h2>
<p>NULL if there is no <i>i</i>&#8216;th key package, or a valid <code>pskc_key_t</code> pointer.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
