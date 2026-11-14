---
title: "pskc_str2valueformat(3)"
name: "pskc_str2valueformat"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_str2valueformat/"
description: "pskc_str2valueformat – API function"
---

<p>pskc_str2valueformat &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;</code></pre>
<p> <code>pskc_valueformat pskc_str2valueformat(const char * </code><i>valueformat</i><code>);</code></p>
<h2>Arguments</h2>
<dl>
<dt>const char * valueformat</p>
<dd>an string describing a key usage.</dl>
<h2>Description</h2>
<p>Convert a string to a <code>pskc_valueformat</code> type. For example, pskc_str2valueformat(&quot;DECIMAL&quot;) will return <code>PSKC_VALUEFORMAT_DECIMAL</code>.</p>
<h2>Returns</h2>
<p>The corresponding <code>pskc_valueformat</code> value.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
