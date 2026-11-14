---
title: "gnutls_verify_stored_pubkey(3)"
name: "gnutls_verify_stored_pubkey"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_verify_stored_pubkey/"
description: "gnutls_verify_stored_pubkey – API function"
---

<h2>NAME</h2>
<p> gnutls_verify_stored_pubkey &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_verify_stored_pubkey(const char * </code><i>db_name</i><code>, gnutls_tdb_t </code><i>tdb</i><code>, const char * </code><i>host</i><code>, const char * </code><i>service</i><code>, gnutls_certificate_type_t </code><i>cert_type</i><code>, const gnutls_datum_t * </code><i>cert</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * db_name</p>
<dd> A file specifying the stored keys (use NULL for the default)</p>
<dt>gnutls_tdb_t tdb</p>
<dd> A storage structure or NULL to use the default</p>
<dt>const char * host</p>
<dd> The peer&#8217;s name</p>
<dt>const char * service</p>
<dd> non-NULL if this key is specific to a service (e.g. http)</p>
<dt>gnutls_certificate_type_t cert_type</p>
<dd> The type of the certificate</p>
<dt>const gnutls_datum_t * cert</p>
<dd> The raw (der) data of the certificate</p>
<dt>unsigned int flags</p>
<dd> should be 0.</dl>
<h2>DESCRIPTION</h2>
<p> This function will try to verify the provided (raw or DER-encoded) certificate using a list of stored public keys. The <i>service</i> field if non-NULL should be a port number. </p>
<p> The <i>retrieve</i> variable if non-null specifies a custom backend for the retrieval of entries. If it is NULL then the default file backend will be used. In POSIX-like systems the file backend uses the $HOME/.gnutls/known_hosts file. </p>
<p> Note that if the custom storage backend is provided the retrieval function should return <code>GNUTLS_E_CERTIFICATE_KEY_MISMATCH</code> if the host/service pair is found but key doesn&#8217;t match, <code>GNUTLS_E_NO_CERTIFICATE_FOUND</code> if no such host/service with the given key is found, and 0 if it was found. The storage function should return 0 on success.</p>
<h2>RETURNS</h2>
<p> If no associated public key is found then <code>GNUTLS_E_NO_CERTIFICATE_FOUND</code> will be returned. If a key is found but does not match <code>GNUTLS_E_CERTIFICATE_KEY_MISMATCH</code> is returned. On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, or a negative error value on other errors.</p>
<h2>SINCE</h2>
<p> 3.0.13</p>
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
