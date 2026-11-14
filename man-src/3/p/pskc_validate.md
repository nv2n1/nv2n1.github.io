---
title: "pskc_validate(3)"
name: "pskc_validate"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_validate/"
description: "pskc_validate – API function"
---

<p>pskc_validate &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
int pskc_validate(pskc_t *container, int *isvalid);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_t * container</p>
<dd>a <code>pskc_t</code> handle, from <code>pskc_init()</code>.</p>
<dt>int * isvalid</p>
<dd>output variable holding validation result, non-0 for valid.</dl>
<h2>Description</h2>
<p>This function validate the PSKC <i>container</i> handle the PSKC XML Schema.</p>
<h2>Returns</h2>
<p>On success, <code>PSKC_OK</code> (zero) is returned, or an error code.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
