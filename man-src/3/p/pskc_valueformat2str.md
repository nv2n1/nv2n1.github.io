---
title: "pskc_valueformat2str(3)"
name: "pskc_valueformat2str"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_valueformat2str/"
description: "pskc_valueformat2str – API function"
---

<p>pskc_valueformat2str &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
const char *pskc_valueformat2str(pskc_valueformat valueformat);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_valueformat valueformat</p>
<dd>an <code>pskc_valueformat</code> enumeration type</dl>
<h2>Description</h2>
<p>Convert <code>pskc_valueformat</code> to a string. For example, pskc_valueformat2str(<code>PSKC_VALUEFORMAT_DECIMAL</code>) will return &quot;DECIMAL&quot;. The returned string must not be deallocated.</p>
<h2>Returns</h2>
<p>String corresponding to <code>pskc_valueformat</code>.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
