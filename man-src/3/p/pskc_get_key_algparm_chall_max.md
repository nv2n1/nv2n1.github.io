---
title: "pskc_get_key_algparm_chall_max(3)"
name: "pskc_get_key_algparm_chall_max"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_get_key_algparm_chall_max/"
description: "pskc_get_key_algparm_chall_max – API function"
---

<p>pskc_get_key_algparm_chall_max &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;</code></pre>
<p> <code>uint32_t pskc_get_key_algparm_chall_max(pskc_key_t * </code><i>key</i><code>, int * </code><i>present</i><code>);</code></p>
<h2>Arguments</h2>
<dl>
<dt>pskc_key_t * key</p>
<dd>a <code>pskc_key_t</code> handle, from <code>pskc_get_keypackage()</code>.</p>
<dt>int * present</p>
<dd>output variable indicating whether data was provided or not.</dl>
<h2>Description</h2>
<p>Get the PSKC KeyPackage Key AlgorithmParameters ChallengeFormat Max value. This attribute defines the maximum size of the challenge accepted by the device for CR mode and MUST be included. If the &#8216;Encoding&#8217; attribute is set to &#8216;DECIMAL&#8217;, &#8216;HEXADECIMAL&#8217;, or &#8216;ALPHANUMERIC&#8217;, this value indicates the maximum number of digits/characters. If the &#8216;Encoding&#8217; attribute is set to &#8216;BASE64&#8217; or &#8216;BINARY&#8217;, this value indicates the maximum number of bytes of the unencoded value. </p>
<p> If <i>present</i> is non-NULL, it will be 0 if the field is not present or 1 if it was present.</p>
<h2>Returns</h2>
<p>an integer holding the content.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
