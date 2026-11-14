---
title: "gnutls_pkcs12_get_bag(3)"
name: "gnutls_pkcs12_get_bag"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs12_get_bag/"
description: "gnutls_pkcs12_get_bag – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs12_get_bag &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs12.h&gt;</code> </p>
<p> <code>int gnutls_pkcs12_get_bag(gnutls_pkcs12_t </code><i>pkcs12</i><code>, int </code><i>indx</i><code>, gnutls_pkcs12_bag_t </code><i>bag</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs12_t pkcs12</p>
<dd> should contain a gnutls_pkcs12_t structure</p>
<dt>int indx</p>
<dd> contains the index of the bag to extract</p>
<dt>gnutls_pkcs12_bag_t bag</p>
<dd> An initialized bag, where the contents of the bag will be copied</dl>
<h2>DESCRIPTION</h2>
<p> This function will return a Bag from the PKCS12 structure. </p>
<p> After the last Bag has been read <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> will be returned.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
