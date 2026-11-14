---
title: "gnutls_pubkey_export(3)"
name: "gnutls_pubkey_export"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pubkey_export/"
description: "gnutls_pubkey_export – API function"
---

<h2>NAME</h2>
<p> gnutls_pubkey_export &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_pubkey_export(gnutls_pubkey_t </code><i>key</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>, void * </code><i>output_data</i><code>, size_t * </code><i>output_data_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pubkey_t key</p>
<dd> Holds the certificate</p>
<dt>gnutls_x509_crt_fmt_t format</p>
<dd> the format of output params. One of PEM or DER.</p>
<dt>void * output_data</p>
<dd> will contain a certificate PEM or DER encoded</p>
<dt>size_t * output_data_size</p>
<dd> holds the size of output_data (and will be replaced by the actual size of parameters)</dl>
<h2>DESCRIPTION</h2>
<p> This function will export the public key to DER or PEM format. The contents of the exported data is the SubjectPublicKeyInfo X.509 structure. </p>
<p> If the buffer provided is not long enough to hold the output, then *output_data_size is updated and <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> will be returned. </p>
<p> If the structure is PEM encoded, it will have a header of &quot;BEGIN CERTIFICATE&quot;.</p>
<h2>RETURNS</h2>
<p> In case of failure a negative error code will be returned, and 0 on success.</p>
<h2>SINCE</h2>
<p> 2.12.0</p>
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
