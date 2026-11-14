---
title: "gnutls_x509_trust_list_remove_cas(3)"
name: "gnutls_x509_trust_list_remove_cas"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_trust_list_remove_cas/"
description: "gnutls_x509_trust_list_remove_cas – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_trust_list_remove_cas &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_trust_list_remove_cas(gnutls_x509_trust_list_t </code><i>list</i><code>, const gnutls_x509_crt_t * </code><i>clist</i><code>, int </code><i>clist_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_trust_list_t list</p>
<dd> The structure of the list</p>
<dt>const gnutls_x509_crt_t * clist</p>
<dd> A list of CAs</p>
<dt>int clist_size</p>
<dd> The length of the CA list</dl>
<h2>DESCRIPTION</h2>
<p> This function will remove the given certificate authorities from the trusted list. </p>
<p> Note that this function can accept certificates and authorities not yet known. In that case they will be kept in a separate black list that will be used during certificate verification. Unlike <code>gnutls_x509_trust_list_add_cas()</code> there is no deinitialization restriction for certificate list provided in this function.</p>
<h2>RETURNS</h2>
<p> The number of removed elements is returned.</p>
<h2>SINCE</h2>
<p> 3.1.10</p>
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
