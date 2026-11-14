---
title: "gnutls_pkcs11_obj_list_import_url(3)"
name: "gnutls_pkcs11_obj_list_import_url"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_obj_list_import_url/"
description: "gnutls_pkcs11_obj_list_import_url – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_obj_list_import_url &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_obj_list_import_url(gnutls_pkcs11_obj_t * </code><i>p_list</i><code>, unsigned int * </code><i>n_list</i><code>, const char * </code><i>url</i><code>, gnutls_pkcs11_obj_attr_t </code><i>attrs</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs11_obj_t * p_list</p>
<dd> An uninitialized object list (may be NULL)</p>
<dt>unsigned int * n_list</p>
<dd> initially should hold the maximum size of the list. Will contain the actual size.</p>
<dt>const char * url</p>
<dd> A PKCS 11 url identifying a set of objects</p>
<dt>gnutls_pkcs11_obj_attr_t attrs</p>
<dd> Attributes of type <code>gnutls_pkcs11_obj_attr_t</code> that can be used to limit output</p>
<dt>unsigned int flags</p>
<dd> Or sequence of GNUTLS_PKCS11_OBJ_* flags</dl>
<h2>DESCRIPTION</h2>
<p> This function will initialize and set values to an object list by using all objects identified by a PKCS 11 URL.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 2.12.0</p>
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
