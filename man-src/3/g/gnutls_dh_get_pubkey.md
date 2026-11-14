---
title: "gnutls_dh_get_pubkey(3)"
name: "gnutls_dh_get_pubkey"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_dh_get_pubkey/"
description: "gnutls_dh_get_pubkey – API function"
---

<h2>NAME</h2>
<p> gnutls_dh_get_pubkey &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_dh_get_pubkey(gnutls_session_t </code><i>session</i><code>, gnutls_datum_t * </code><i>raw_key</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a gnutls session</p>
<dt>gnutls_datum_t * raw_key</p>
<dd> will hold the public key.</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the peer&#8217;s public key used in the last Diffie-Hellman key exchange. This function should be used for both anonymous and ephemeral Diffie-Hellman. The output parameters must be freed with <code>gnutls_free()</code>. </p>
<p> Note, that public key is exported as non-negative integer and may include a leading zero byte.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise an error code is returned.</p>
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
