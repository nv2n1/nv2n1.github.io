---

title: "gnutls_x509_crl_list_import(3)"
name: "gnutls_x509_crl_list_import"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crl_list_import/"
description: "gnutls_x509_crl_list_import – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crl_list_import &#8211; API function</p>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crl_list_import(gnutls_x509_crl_t * </code><i>crls</i><code>, unsigned int * </code><i>crl_max</i><code>, const gnutls_datum_t * </code><i>data</i><code>, gnutls_x509_crt_fmt_t </code><i>format</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crl_t * crls</dt>
<dd> The structures to store the parsed CRLs. Must not be initialized.</dd>
<dt>unsigned int * crl_max</dt>
<dd> Initially must hold the maximum number of crls. It will be updated with the number of crls available.</dd>
<dt>const gnutls_datum_t * data</dt>
<dd> The PEM encoded CRLs</dd>
<dt>gnutls_x509_crt_fmt_t format</dt>
<dd> One of DER or PEM.</dd>
<dt>unsigned int flags</dt>
<dd> must be (0) or an OR&#8217;d sequence of gnutls_certificate_import_flags.</dd></dl>
<p> This function will convert the given PEM encoded CRL list to the native gnutls_x509_crl_t format. The output will be stored in <i>crls</i> . They will be automatically initialized. </p>
<p> If the Certificate is PEM encoded it should have a header of &quot;X509 CRL&quot;.</p>
<h2>RETURNS</h2>
<p> the number of certificates read or a negative error value.</p>
<h2>SINCE</h2>
<p> 3.0</p>
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
