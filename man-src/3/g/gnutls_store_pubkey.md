---
title: "gnutls_store_pubkey(3)"
name: "gnutls_store_pubkey"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_store_pubkey/"
description: "gnutls_store_pubkey – API function"
---

<h2>NAME</h2>
<p> gnutls_store_pubkey &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_store_pubkey(const char * </code><i>db_name</i><code>, gnutls_tdb_t </code><i>tdb</i><code>, const char * </code><i>host</i><code>, const char * </code><i>service</i><code>, gnutls_certificate_type_t </code><i>cert_type</i><code>, const gnutls_datum_t * </code><i>cert</i><code>, time_t </code><i>expiration</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
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
<dd> The data of the certificate</p>
<dt>time_t expiration</p>
<dd> The expiration time (use 0 to disable expiration)</p>
<dt>unsigned int flags</p>
<dd> should be 0.</dl>
<h2>DESCRIPTION</h2>
<p> This function will store the provided (raw or DER-encoded) certificate to the list of stored public keys. The key will be considered valid until the provided expiration time. </p>
<p> The <i>store</i> variable if non-null specifies a custom backend for the storage of entries. If it is NULL then the default file backend will be used.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
