---
title: "gnutls_x509_trust_list_add_named_crt(3)"
name: "gnutls_x509_trust_list_add_named_crt"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_trust_list_add_named_crt/"
description: "gnutls_x509_trust_list_add_named_crt – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_trust_list_add_named_crt &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_trust_list_add_named_crt(gnutls_x509_trust_list_t </code><i>list</i><code>, gnutls_x509_crt_t </code><i>cert</i><code>, const void * </code><i>name</i><code>, size_t </code><i>name_size</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_trust_list_t list</p>
<dd> The structure of the list</p>
<dt>gnutls_x509_crt_t cert</p>
<dd> A certificate</p>
<dt>const void * name</p>
<dd> An identifier for the certificate</p>
<dt>size_t name_size</p>
<dd> The size of the identifier</p>
<dt>unsigned int flags</p>
<dd> should be 0.</dl>
<h2>DESCRIPTION</h2>
<p> This function will add the given certificate to the trusted list and associate it with a name. The certificate will not be be used for verification with <code>gnutls_x509_trust_list_verify_crt()</code> but only with <code>gnutls_x509_trust_list_verify_named_crt()</code>. </p>
<p> In principle this function can be used to set individual &quot;server&quot; certificates that are trusted by the user for that specific server but for no other purposes. </p>
<p> The certificate must not be deinitialized during the lifetime of the trusted list.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.0.0</p>
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
