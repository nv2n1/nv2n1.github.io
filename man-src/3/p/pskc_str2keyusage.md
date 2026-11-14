---
title: "pskc_str2keyusage(3)"
name: "pskc_str2keyusage"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_str2keyusage/"
description: "pskc_str2keyusage – API function"
---

<p>pskc_str2keyusage &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;</code></pre>
<p> <code>pskc_keyusage pskc_str2keyusage(const char * </code><i>keyusage</i><code>);</code></p>
<h2>Arguments</h2>
<dl>
<dt>const char * keyusage</p>
<dd>an string describing a key usage.</dl>
<h2>Description</h2>
<p>Convert a string to a <code>pskc_keyusage</code> type. For example, pskc_str2keyusage(&quot;KeyWrap&quot;) will return <code>PSKC_KEYUSAGE_KEYWRAP</code>.</p>
<h2>Returns</h2>
<p>The corresponding <code>pskc_keyusage</code> value.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
