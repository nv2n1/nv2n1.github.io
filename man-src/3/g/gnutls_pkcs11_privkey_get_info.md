---
title: "gnutls_pkcs11_privkey_get_info(3)"
name: "gnutls_pkcs11_privkey_get_info"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_privkey_get_info/"
description: "gnutls_pkcs11_privkey_get_info – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_privkey_get_info &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_privkey_get_info(gnutls_pkcs11_privkey_t </code><i>pkey</i><code>, gnutls_pkcs11_obj_info_t </code><i>itype</i><code>, void * </code><i>output</i><code>, size_t * </code><i>output_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs11_privkey_t pkey</p>
<dd> should contain a <code>gnutls_pkcs11_privkey_t</code> structure</p>
<dt>gnutls_pkcs11_obj_info_t itype</p>
<dd> Denotes the type of information requested</p>
<dt>void * output</p>
<dd> where output will be stored</p>
<dt>size_t * output_size</p>
<dd> contains the maximum size of the output and will be overwritten with actual</dl>
<h2>DESCRIPTION</h2>
<p> This function will return information about the PKCS 11 private key such as the label, id as well as token information where the key is stored. When output is text it returns null terminated string although <code>output_size</code> contains the size of the actual data only.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> (0) on success or a negative error code on error.</p>
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
