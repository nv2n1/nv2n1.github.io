---
title: "pskc_set_cryptomodule_id(3)"
name: "pskc_set_cryptomodule_id"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_set_cryptomodule_id/"
description: "pskc_set_cryptomodule_id – API function"
---

<p>pskc_set_cryptomodule_id &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
void pskc_set_cryptomodule_id(pskc_key_t *key, const char *cid);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_key_t * key</p>
<dd>a <code>pskc_key_t</code> handle, from <code>pskc_get_keypackage()</code>.</p>
<dt>const char * cid</p>
<dd>the cryptomodule id to set</dl>
<h2>Description</h2>
<p>Set the PSKC KeyPackage CryptoModule Id value. This element carries a unique identifier for the CryptoModule and is implementation specific. As such, it helps to identify a specific CryptoModule to which the key is being or was provisioned. </p>
<p> The pointer is stored in <i>container</i>, not a copy of the data, so you must not deallocate the data before another call to this function or the last call to any function using <i>container</i>.</p>
<h2>Since</h2>
<p>2.2.0</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
