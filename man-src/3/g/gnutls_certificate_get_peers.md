---
title: "gnutls_certificate_get_peers(3)"
name: "gnutls_certificate_get_peers"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_certificate_get_peers/"
description: "gnutls_certificate_get_peers – API function"
---

<h2>NAME</h2>
<p> gnutls_certificate_get_peers &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>const gnutls_datum_t * gnutls_certificate_get_peers(gnutls_session_t </code><i>session</i><code>, unsigned int * </code><i>list_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a gnutls session</p>
<dt>unsigned int * list_size</p>
<dd> is the length of the certificate list (may be <code>NULL</code>)</dl>
<h2>DESCRIPTION</h2>
<p> Get the peer&#8217;s raw certificate (chain) as sent by the peer. These certificates are in raw format (DER encoded for X.509). In case of a X.509 then a certificate list may be present. The first certificate in the list is the peer&#8217;s certificate, following the issuer&#8217;s certificate, then the issuer&#8217;s issuer etc. </p>
<p> In case of OpenPGP keys a single key will be returned in raw format.</p>
<h2>RETURNS</h2>
<p> a pointer to a <code>gnutls_datum_t</code> containing the peer&#8217;s certificates, or <code>NULL</code> in case of an error or if no certificate was used.</p>
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
