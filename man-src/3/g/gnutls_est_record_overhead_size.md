---
title: "gnutls_est_record_overhead_size(3)"
name: "gnutls_est_record_overhead_size"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_est_record_overhead_size/"
description: "gnutls_est_record_overhead_size – API function"
---

<h2>NAME</h2>
<p> gnutls_est_record_overhead_size &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>size_t gnutls_est_record_overhead_size(gnutls_protocol_t </code><i>version</i><code>, gnutls_cipher_algorithm_t </code><i>cipher</i><code>, gnutls_mac_algorithm_t </code><i>mac</i><code>, gnutls_compression_method_t </code><i>comp</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_protocol_t version</p>
<dd> is a <code>gnutls_protocol_t</code> value</p>
<dt>gnutls_cipher_algorithm_t cipher</p>
<dd> is a <code>gnutls_cipher_algorithm_t</code> value</p>
<dt>gnutls_mac_algorithm_t mac</p>
<dd> is a <code>gnutls_mac_algorithm_t</code> value</p>
<dt>gnutls_compression_method_t comp</p>
<dd> is a <code>gnutls_compression_method_t</code> value</p>
<dt>unsigned int flags</p>
<dd> must be zero</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the set size in bytes of the overhead due to TLS (or DTLS) per record. </p>
<p> Note that this function may provide inacurate values when TLS extensions that modify the record format are negotiated. In these cases a more accurate value can be obtained using <code>gnutls_record_overhead_size()</code> after a completed handshake.</p>
<h2>SINCE</h2>
<p> 3.2.2</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></p>
<dd> </code></dl>
<h2>Index</h2>
