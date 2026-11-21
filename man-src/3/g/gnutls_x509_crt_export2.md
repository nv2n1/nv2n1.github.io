---

title: "gnutls_x509_crt_export2(3)"
name: "gnutls_x509_crt_export2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_export2/"
description: "gnutls_x509_crt_export2 – API function"
---

<p> gnutls_x509_crt_export2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_export2(gnutls_x509_crt_t </code><i>cert</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>, gnutls_datum_t * </code><i>out</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</dt>
<dd> Holds the certificate</dd>
<dt>gnutls_x509_crt_fmt_t format</dt>
<dd> the format of output params. One of PEM or DER.</dd>
<dt>gnutls_datum_t * out</dt>
<dd> will contain a certificate PEM or DER encoded</dd></dl>
<h2>DESCRIPTION</h2>
<p> This function will export the certificate to DER or PEM format. The output buffer is allocated using <code>gnutls_malloc()</code>. </p>
<p> If the structure is PEM encoded, it will have a header of &quot;BEGIN CERTIFICATE&quot;.</p>
<h2>RETURNS</h2>
<p> In case of failure a negative error code will be returned, and 0 on success.</p>
<h2>SINCE</h2>
<p> 3.1.3</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
