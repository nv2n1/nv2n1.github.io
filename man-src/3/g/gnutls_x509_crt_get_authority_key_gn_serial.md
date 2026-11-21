---

title: "gnutls_x509_crt_get_authority_key_gn_serial(3)"
name: "gnutls_x509_crt_get_authority_key_gn_serial"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_authority_key_gn_serial/"
description: "gnutls_x509_crt_get_authority_key_gn_serial – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_authority_key_gn_serial &#8211; API function</p>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_authority_key_gn_serial(gnutls_x509_crt_t </code><i>cert</i><code>, unsigned int </code><i>seq</i><code>, void * </code><i>alt</i><code>, size_t * </code><i>alt_size</i><code>, unsigned int * </code><i>alt_type</i><code>, void * </code><i>serial</i><code>, size_t * </code><i>serial_size</i><code>, unsigned int * </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</dt>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</dd>
<dt>unsigned int seq</dt>
<dd> specifies the sequence number of the alt name (0 for the first one, 1 for the second etc.)</dd>
<dt>void * alt</dt>
<dd> is the place where the alternative name will be copied to</dd>
<dt>size_t * alt_size</dt>
<dd> holds the size of alt.</dd>
<dt>unsigned int * alt_type</dt>
<dd> holds the type of the alternative name (one of gnutls_x509_subject_alt_name_t).</dd>
<dt>void * serial</dt>
<dd> buffer to store the serial number (may be null)</dd>
<dt>size_t * serial_size</dt>
<dd> Holds the size of the serial field (may be null)</dd>
<dt>unsigned int * critical</dt>
<dd> will be non-zero if the extension is marked as critical (may be null)</dd></dl>
<p> This function will return the X.509 authority key identifier when stored as a general name (authorityCertIssuer) and serial number. </p>
<p> Because more than one general names might be stored<br />
&nbsp;<wbr><i>seq</i>&nbsp;<wbr>can be used as a counter to request them all until&nbsp;<wbr> <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> is returned.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> if the extension is not present, otherwise a negative error value.</p>
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
