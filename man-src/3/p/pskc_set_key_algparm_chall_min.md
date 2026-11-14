---
title: "pskc_set_key_algparm_chall_min(3)"
name: "pskc_set_key_algparm_chall_min"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_set_key_algparm_chall_min/"
description: "pskc_set_key_algparm_chall_min – API function"
---

<p>pskc_set_key_algparm_chall_min &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
void pskc_set_key_algparm_chall_min(pskc_key_t *key, uint32_t challmin);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_key_t * key</p>
<dd>a <code>pskc_key_t</code> handle, from <code>pskc_get_keypackage()</code>.</p>
<dt>uint32_t challmin</p>
<dd>the minimum challenge length to set.</dl>
<h2>Description</h2>
<p>Set the PSKC KeyPackage Key AlgorithmParameters ChallengeFormat Min value. This attribute defines the minimum size of the challenge accepted by the device for CR mode and MUST be included. If the digits/characters. If the &#8216;Encoding&#8217; attribute is set to &#8216;BASE64&#8217; or &#8216;BINARY&#8217;, this value indicates the minimum number of bytes of the unencoded value.</p>
<h2>Since</h2>
<p>2.2.0</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
