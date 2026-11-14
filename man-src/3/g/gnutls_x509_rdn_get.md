---
title: "gnutls_x509_rdn_get(3)"
name: "gnutls_x509_rdn_get"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_rdn_get/"
description: "gnutls_x509_rdn_get – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_rdn_get &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_rdn_get(const gnutls_datum_t * </code><i>idn</i><code>, char * </code><i>buf</i><code>, size_t * </code><i>buf_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const gnutls_datum_t * idn</p>
<dd> should contain a DER encoded RDN sequence</p>
<dt>char * buf</p>
<dd> a pointer to a structure to hold the peer&#8217;s name</p>
<dt>size_t * buf_size</p>
<dd> holds the size of <i>buf</i></dl>
<h2>DESCRIPTION</h2>
<p> This function will return the name of the given RDN sequence. The name will be in the form &quot;C=xxxx,O=yyyy,CN=zzzz&quot; as described in RFC4514.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, or <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> is returned and * <i>buf_size</i> is updated if the provided buffer is not long enough, otherwise a negative error value.</p>
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
