---
title: "pskc_set_key_policy_numberoftransactions(3)"
name: "pskc_set_key_policy_numberoftransactions"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_set_key_policy_numberoftransactions/"
description: "pskc_set_key_policy_numberoftransactions – API function"
---

<p>pskc_set_key_policy_numberoftransactions &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
void pskc_set_key_policy_numberoftransactions(pskc_key_t *key, uint64_t uses);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_key_t * key</p>
<dd>a <code>pskc_key_t</code> handle, from <code>pskc_get_keypackage()</code>.</p>
<dt>uint64_t uses</p>
<dd>the number of transactions to set.</dl>
<h2>Description</h2>
<p>Set the PSKC KeyPackage Key Policy NumberOfTransactions value. The value in this element indicates the maximum number of times a key carried within the PSKC document can be used by an application after having received it. When this element is omitted, there is no restriction regarding the number of times a key can be used. </p>
<p> Note that while the PSKC specification uses the XML data type &quot;nonNegativeInteger&quot; for this variable, this implementation restricts the size of the value to 64-bit integers.</p>
<h2>Since</h2>
<p>2.2.0</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
