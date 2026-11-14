---
title: "gnutls_pkcs11_obj_get_exts(3)"
name: "gnutls_pkcs11_obj_get_exts"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_obj_get_exts/"
description: "gnutls_pkcs11_obj_get_exts – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_obj_get_exts &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_obj_get_exts(gnutls_pkcs11_obj_t </code><i>obj</i><code>, gnutls_x509_ext_st ** </code><i>exts</i><code>, unsigned int * </code><i>exts_size</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs11_obj_t obj</p>
<dd> should contain a <code>gnutls_pkcs11_obj_t</code> type</p>
<dt>gnutls_x509_ext_st ** exts</p>
<dd> a pointer to a <code>gnutls_x509_ext_st</code> pointer</p>
<dt>unsigned int * exts_size</p>
<dd> will be updated with the number of <i>exts</i></p>
<dt>unsigned int flags</p>
<dd> Or sequence of <code>GNUTLS_PKCS11_OBJ_</code>* flags</dl>
<h2>DESCRIPTION</h2>
<p> This function will return information about attached extensions that associate to the provided object (which should be a certificate). The extensions are the attached p11-kit trust module extensions. </p>
<p> Each element of <i>exts</i> must be deinitialized using <code>gnutls_x509_ext_deinit()</code> while <i>exts</i> should be deallocated using <code>gnutls_free()</code>.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> (0) on success or a negative error code on error.</p>
<h2>SINCE</h2>
<p> 3.3.8</p>
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
