---
title: "pskc_sign_x509(3)"
name: "pskc_sign_x509"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pskc_sign_x509/"
description: "pskc_sign_x509 – API function"
---

<p>pskc_sign_x509 &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pskc.h&gt;
int pskc_sign_x509(pskc_t *container, const char *key_file, const char *cert_file);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>pskc_t * container</p>
<dd>a <code>pskc_t</code> handle, from <code>pskc_init()</code>.</p>
<dt>const char * key_file</p>
<dd>filename of file containing private key.</p>
<dt>const char * cert_file</p>
<dd>filename of file containing corresponding X.509 certificate.</dl>
<h2>Description</h2>
<p>Sign PSKC data using X.509 certificate and private key.</p>
<h2>Returns</h2>
<p>On success, <code>PSKC_OK</code> (zero) is returned, or an error code.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;oath-toolkit-help [at] nongnu.org&gt;. libpskc home page: <a rel="nofollow" href="http://www.gnu.org/software/libpskc/">http://www.gnu.org/software/libpskc/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
