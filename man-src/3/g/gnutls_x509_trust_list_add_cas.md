---
title: "gnutls_x509_trust_list_add_cas(3)"
name: "gnutls_x509_trust_list_add_cas"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_trust_list_add_cas/"
description: "gnutls_x509_trust_list_add_cas – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_trust_list_add_cas &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_trust_list_add_cas(gnutls_x509_trust_list_t </code><i>list</i><code>, const gnutls_x509_crt_t * </code><i>clist</i><code>, unsigned </code><i>clist_size</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_trust_list_t list</p>
<dd> The structure of the list</p>
<dt>const gnutls_x509_crt_t * clist</p>
<dd> A list of CAs</p>
<dt>unsigned clist_size</p>
<dd> The length of the CA list</p>
<dt>unsigned int flags</p>
<dd> should be 0 or an or&#8217;ed sequence of <code>GNUTLS_TL</code> options.</dl>
<h2>DESCRIPTION</h2>
<p> This function will add the given certificate authorities to the trusted list. The list of CAs must not be deinitialized during this structure&#8217;s lifetime. </p>
<p> If the flag <code>GNUTLS_TL_NO_DUPLICATES</code> is specified, then the provided <i>clist</i> entries that are duplicates will not be added to the list and will be deinitialized.</p>
<h2>RETURNS</h2>
<p> The number of added elements is returned.</p>
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
