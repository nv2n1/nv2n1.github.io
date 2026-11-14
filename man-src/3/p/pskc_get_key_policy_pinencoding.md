---
title: "pskc_get_key_policy_pinencoding(3)"
name: "pskc_get_key_policy_pinencoding"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_get_key_policy_pinencoding/"
description: "pskc_get_key_policy_pinencoding – API function"
---

<p>pskc_get_key_policy_pinencoding &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;</code></pre>
<p> <code>pskc_valueformat pskc_get_key_policy_pinencoding(pskc_key_t * </code><i>key</i><code>, int * </code><i>present</i><code>);</code></p>
<h2>Arguments</h2>
<dl>
<dt>pskc_key_t * key</p>
<dd>a <code>pskc_key_t</code> handle, from <code>pskc_get_keypackage()</code>.</p>
<dt>int * present</p>
<dd>output variable indicating whether data was provided or not.</dl>
<h2>Description</h2>
<p>Get the PSKC KeyPackage Key Policy PINPolicy PINEncoding value. This attribute indicates the encoding of the PIN and MUST be one of the <code>pskc_valueformat</code> values. </p>
<p> If <i>present</i> is non-NULL, it will be 0 if the field is not present or 1 if it was present.</p>
<h2>Returns</h2>
<p>an <code>pskc_valueformat</code> value</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
