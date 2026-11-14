---
title: "gnutls_pkcs11_obj_set_info(3)"
name: "gnutls_pkcs11_obj_set_info"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_obj_set_info/"
description: "gnutls_pkcs11_obj_set_info – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_obj_set_info &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_obj_set_info(gnutls_pkcs11_obj_t </code><i>obj</i><code>, gnutls_pkcs11_obj_info_t </code><i>itype</i><code>, const void * </code><i>data</i><code>, size_t </code><i>data_size</i><code>, unsigned </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs11_obj_t obj</p>
<dd> should contain a <code>gnutls_pkcs11_obj_t</code> structure</p>
<dt>gnutls_pkcs11_obj_info_t itype</p>
<dd> Denotes the type of information to be set</p>
<dt>const void * data</p>
<dd> the data to set</p>
<dt>size_t data_size</p>
<dd> the size of data</p>
<dt>unsigned flags</p>
<dd> Or sequence of GNUTLS_PKCS11_OBJ_* flags</dl>
<h2>DESCRIPTION</h2>
<p> This function will set attributes on the provided object. Available options for <i>itype</i> are <code>GNUTLS_PKCS11_OBJ_LABEL</code>, <code>GNUTLS_PKCS11_OBJ_ID_HEX</code>, and <code>GNUTLS_PKCS11_OBJ_ID</code>.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> (0) on success or a negative error code on error.</p>
<h2>SINCE</h2>
<p> 3.3.26</p>
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
