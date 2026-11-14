---
title: "gnutls_x509_trust_list_remove_trust_mem(3)"
name: "gnutls_x509_trust_list_remove_trust_mem"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_trust_list_remove_trust_mem/"
description: "gnutls_x509_trust_list_remove_trust_mem – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_trust_list_remove_trust_mem &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_trust_list_remove_trust_mem(gnutls_x509_trust_list_t </code><i>list</i><code>, const gnutls_datum_t * </code><i>cas</i><code>, gnutls_x509_crt_fmt_t </code><i>type</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_trust_list_t list</p>
<dd> The structure of the list</p>
<dt>const gnutls_datum_t * cas</p>
<dd> A buffer containing a list of CAs (optional)</p>
<dt>gnutls_x509_crt_fmt_t type</p>
<dd> The format of the certificates</dl>
<h2>DESCRIPTION</h2>
<p> This function will remove the provided certificate authorities from the trusted list, and add them into a black list when needed. </p>
<p> See also <code>gnutls_x509_trust_list_remove_cas()</code>.</p>
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
