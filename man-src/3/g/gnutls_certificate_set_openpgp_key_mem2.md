---

title: "gnutls_certificate_set_openpgp_key_mem2(3)"
name: "gnutls_certificate_set_openpgp_key_mem2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_set_openpgp_key_mem2/"
description: "gnutls_certificate_set_openpgp_key_mem2 – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_set_openpgp_key_mem2 &#8211; API function</p>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_certificate_set_openpgp_key_mem2(gnutls_certificate_credentials_t </code><i>res</i><code>, const gnutls_datum_t * </code><i>cert</i><code>, const gnutls_datum_t * </code><i>key</i><code>, const char * </code><i>subkey_id</i><code>, gnutls_openpgp_crt_fmt_t </code><i>format</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_certificate_credentials_t res</dt>
<dd> the destination context to save the data.</dd>
<dt>const gnutls_datum_t * cert</dt>
<dd> the datum that contains the public key.</dd>
<dt>const gnutls_datum_t * key</dt>
<dd> the datum that contains the secret key.</dd>
<dt>const char * subkey_id</dt>
<dd> a hex encoded subkey id</dd>
<dt>gnutls_openpgp_crt_fmt_t format</dt>
<dd> the format of the keys</dd></dl>
<p> This funtion is used to load OpenPGP keys into the GnuTLS credentials structure. The datum should contain at least one valid non encrypted subkey. </p>
<p> The special keyword &quot;auto&quot; is also accepted as <i>subkey_id</i> . In that case the <code>gnutls_openpgp_crt_get_auth_subkey()</code> will be used to retrieve the subkey.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 2.4.0</p>
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
