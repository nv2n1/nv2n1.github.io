---
title: "gnutls_x509_crq_get_key_usage-2(3)"
name: "gnutls_x509_crq_get_key_usage-2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_get_key_usage-2/"
description: "gnutls_x509_crq_get_key_usage – API function"
---

<p>gnutls_x509_crq_get_key_usage &#8211; API function</p>
<h2>Synopsis</h2>
<p><code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_get_key_usage(gnutls_x509_crq_t </code><i>crq</i><code>, unsigned int * </code><i>key_usage</i><code>, unsigned int * </code><i>critical</i><code>);</code></p>
<h2>Arguments</h2>
<dl COMPACT>
<dt>gnutls_x509_crq_t crq</p>
<dd>should contain a <code>gnutls_x509_crq_t</code> structure</p>
<dt>unsigned int * key_usage</p>
<dd>where the key usage bits will be stored</p>
<dt>unsigned int * critical</p>
<dd>will be non-zero if the extension is marked as critical</dl>
<h2>Description</h2>
<p>This function will return certificate&#8217;s key usage, by reading the keyUsage X.509 extension (2.5.29.15). The key usage value will ORed values of the: <code>GNUTLS_KEY_DIGITAL_SIGNATURE</code>, <code>GNUTLS_KEY_NON_REPUDIATION</code>, <code>GNUTLS_KEY_KEY_ENCIPHERMENT</code>, <code>GNUTLS_KEY_DATA_ENCIPHERMENT</code>, <code>GNUTLS_KEY_KEY_AGREEMENT</code>, <code>GNUTLS_KEY_KEY_CERT_SIGN</code>, <code>GNUTLS_KEY_CRL_SIGN</code>, <code>GNUTLS_KEY_ENCIPHER_ONLY</code>, <code>GNUTLS_KEY_DECIPHER_ONLY</code>.</p>
<h2>Returns</h2>
<p>the certificate key usage, or a negative error code in case of parsing error. If the certificate does not contain the keyUsage extension <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> will be returned.</p>
<h2>Since</h2>
<p>2.8.0</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>Copyright</h2>
<p>Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>See Also</h2>
<p>The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl COMPACT>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></p>
<dd></code></dl>
