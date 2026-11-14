---
title: "gnutls_srtp_get_keys(3)"
name: "gnutls_srtp_get_keys"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_srtp_get_keys/"
description: "gnutls_srtp_get_keys – API function"
---

<h2>NAME</h2>
<p> gnutls_srtp_get_keys &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_srtp_get_keys(gnutls_session_t </code><i>session</i><code>, void * </code><i>key_material</i><code>, unsigned int </code><i>key_material_size</i><code>, gnutls_datum_t * </code><i>client_key</i><code>, gnutls_datum_t * </code><i>client_salt</i><code>, gnutls_datum_t * </code><i>server_key</i><code>, gnutls_datum_t * </code><i>server_salt</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>void * key_material</p>
<dd> Space to hold the generated key material</p>
<dt>unsigned int key_material_size</p>
<dd> The maximum size of the key material</p>
<dt>gnutls_datum_t * client_key</p>
<dd> The master client write key, pointing inside the key material</p>
<dt>gnutls_datum_t * client_salt</p>
<dd> The master client write salt, pointing inside the key material</p>
<dt>gnutls_datum_t * server_key</p>
<dd> The master server write key, pointing inside the key material</p>
<dt>gnutls_datum_t * server_salt</p>
<dd> The master server write salt, pointing inside the key material</dl>
<h2>DESCRIPTION</h2>
<p> This is a helper function to generate the keying material for SRTP. It requires the space of the key material to be pre-allocated (should be at least 2x the maximum key size and salt size). The <i>client_key</i> , <i>client_salt</i> , <i>server_key</i> and <i>server_salt</i> are convenience datums that point inside the key material. They may be <code>NULL</code>.</p>
<h2>RETURNS</h2>
<p> On success the size of the key material is returned, otherwise, <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> if the buffer given is not sufficient, or a negative error code. </p>
<p> Since 3.1.4</p>
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
