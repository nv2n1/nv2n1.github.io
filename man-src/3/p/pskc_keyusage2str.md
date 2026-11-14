---
title: "pskc_keyusage2str(3)"
name: "pskc_keyusage2str"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_keyusage2str/"
description: "pskc_keyusage2str – API function"
---

<p>pskc_keyusage2str &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
const char *pskc_keyusage2str(pskc_keyusage keyusage);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_keyusage keyusage</p>
<dd>an <code>pskc_keyusage</code> enumeration type</dl>
<h2>Description</h2>
<p>Convert <code>pskc_keyusage</code> to a string. For example, pskc_keyusage2str(<code>PSKC_KEYUSAGE_OTP</code>) will return &quot;OTP&quot;. The returned string must not be deallocated.</p>
<h2>Returns</h2>
<p>String corresponding to <code>pskc_keyusage</code>.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
