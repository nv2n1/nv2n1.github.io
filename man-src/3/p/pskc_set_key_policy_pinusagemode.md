---
title: "pskc_set_key_policy_pinusagemode(3)"
name: "pskc_set_key_policy_pinusagemode"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_set_key_policy_pinusagemode/"
description: "pskc_set_key_policy_pinusagemode – API function"
---

<p>pskc_set_key_policy_pinusagemode &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
void pskc_set_key_policy_pinusagemode(pskc_key_t *key, pskc_pinusagemode pinusagemode);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_key_t * key</p>
<dd>a <code>pskc_key_t</code> handle, from <code>pskc_get_keypackage()</code>.</p>
<dt>pskc_pinusagemode pinusagemode</p>
<dd>the <code>pskc_pinusagemode</code> value to set</dl>
<h2>Description</h2>
<p>Set the PSKC KeyPackage Key Policy PINPolicy PINUsageMode value. This mandatory attribute indicates the way the PIN is used during the usage of the key.</p>
<h2>Since</h2>
<p>2.2.0</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
