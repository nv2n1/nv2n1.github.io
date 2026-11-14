---
title: "gnutls_x509_dn_get_rdn_ava(3)"
name: "gnutls_x509_dn_get_rdn_ava"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_dn_get_rdn_ava/"
description: "gnutls_x509_dn_get_rdn_ava – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_dn_get_rdn_ava &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_dn_get_rdn_ava(gnutls_x509_dn_t </code><i>dn</i><code>, int </code><i>irdn</i><code>, int </code><i>iava</i><code>, gnutls_x509_ava_st * </code><i>ava</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_dn_t dn</p>
<dd> a pointer to DN</p>
<dt>int irdn</p>
<dd> index of RDN</p>
<dt>int iava</p>
<dd> index of AVA.</p>
<dt>gnutls_x509_ava_st * ava</p>
<dd> Pointer to structure which will hold output information.</dl>
<h2>DESCRIPTION</h2>
<p> Get pointers to data within the DN. The format of the <i>ava</i> structure is shown below. </p>
<p> struct gnutls_x509_ava_st { gnutls_datum_t oid; gnutls_datum_t value; unsigned long value_tag; }; </p>
<p> The X.509 distinguished name is a sequence of sequences of strings and this is what the <i>irdn</i> and <i>iava</i> indexes model. </p>
<p> Note that <i>ava</i> will contain pointers into the <i>dn</i> structure which in turns points to the original certificate. Thus you should not modify any data or deallocate any of those. </p>
<p> This is a low-level function that requires the caller to do the value conversions when necessary (e.g. from UCS-2).</p>
<h2>RETURNS</h2>
<p> Returns 0 on success, or an error code.</p>
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
