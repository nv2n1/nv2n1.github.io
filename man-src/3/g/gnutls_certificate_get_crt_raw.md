---

title: "gnutls_certificate_get_crt_raw(3)"
name: "gnutls_certificate_get_crt_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_get_crt_raw/"
description: "gnutls_certificate_get_crt_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_get_crt_raw &#8211; API function</p>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_certificate_get_crt_raw(gnutls_certificate_credentials_t </code><i>sc</i><code>, unsigned </code><i>idx1</i><code>, unsigned </code><i>idx2</i><code>, gnutls_datum_t * </code><i>cert</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t sc</dt>
<dd> is a <code>gnutls_certificate_credentials_t</code> structure.</dd>
<dt>unsigned idx1</dt>
<dd> the index of the certificate if multiple are present</dd>
<dt>unsigned idx2</dt>
<dd> the index in the certificate list. Zero gives the server&#8217;s certificate.</dd>
<dt>gnutls_datum_t * cert</dt>
<dd> Will hold the DER encoded certificate.</dd></dl>
<p> This function will return the DER encoded certificate of the server or any other certificate on its certificate chain (based on <i>idx2</i> ). The returned data should be treated as constant and only accessible during the lifetime of <i>sc</i> .</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value. In case the indexes are out of bounds <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> is returned.</p>
<h2>SINCE</h2>
<p> 3.2.5</p>
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
