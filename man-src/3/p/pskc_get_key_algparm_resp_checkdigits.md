---
title: "pskc_get_key_algparm_resp_checkdigits(3)"
name: "pskc_get_key_algparm_resp_checkdigits"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_get_key_algparm_resp_checkdigits/"
description: "pskc_get_key_algparm_resp_checkdigits – API function"
---

<p>pskc_get_key_algparm_resp_checkdigits &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
int pskc_get_key_algparm_resp_checkdigits(pskc_key_t *key, int *present);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_key_t * key</p>
<dd>a <code>pskc_key_t</code> handle, from <code>pskc_get_keypackage()</code>.</p>
<dt>int * present</p>
<dd>output variable indicating whether data was provided or not.</dl>
<h2>Description</h2>
<p>Get the PSKC KeyPackage Key AlgorithmParameters ResponseFormat CheckDigits value. This attribute indicates whether the device needs to append a Luhn check digit, as defined in [ISOIEC7812], to the response. This is only valid if the &#8216;Encoding&#8217; attribute is set to &#8216;DECIMAL&#8217;. If the value is TRUE, then the device will append a Luhn check digit to the response. If the value is FALSE, then the device will not append a Luhn check digit to the response. </p>
<p> If <i>present</i> is non-NULL, it will be 0 if the field is not present or 1 if it was present.</p>
<h2>Returns</h2>
<p>1 to indicate a CheckDigits value of true, or 0 to indicate false.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
