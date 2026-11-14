---
title: "gnutls_x509_name_constraints_add_permitted(3)"
name: "gnutls_x509_name_constraints_add_permitted"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_name_constraints_add_permitted/"
description: "gnutls_x509_name_constraints_add_permitted – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_name_constraints_add_permitted &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_name_constraints_add_permitted(gnutls_x509_name_constraints_t </code><i>nc</i><code>, gnutls_x509_subject_alt_name_t </code><i>type</i><code>, const gnutls_datum_t * </code><i>name</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_name_constraints_t nc</p>
<dd> The nameconstraints structure</p>
<dt>gnutls_x509_subject_alt_name_t type</p>
<dd> The type of the constraints</p>
<dt>const gnutls_datum_t * name</p>
<dd> The data of the constraints</dl>
<h2>DESCRIPTION</h2>
<p> This function will add a name constraint to the list of permitted constraints. The constraints <i>type</i> can be any of the following types: <code>GNUTLS_SAN_DNSNAME</code>, <code>GNUTLS_SAN_RFC822NAME</code>, <code>GNUTLS_SAN_DN</code>, <code>GNUTLS_SAN_URI</code>, <code>GNUTLS_SAN_IPADDRESS</code>. For the latter, an IP address in network byte order is expected, followed by its network mask.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.3.0</p>
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
