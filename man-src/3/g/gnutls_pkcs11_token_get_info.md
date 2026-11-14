---
title: "gnutls_pkcs11_token_get_info(3)"
name: "gnutls_pkcs11_token_get_info"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_token_get_info/"
description: "gnutls_pkcs11_token_get_info – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_token_get_info &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_token_get_info(const char * </code><i>url</i><code>, gnutls_pkcs11_token_info_t </code><i>ttype</i><code>, void * </code><i>output</i><code>, size_t * </code><i>output_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * url</p>
<dd> should contain a PKCS 11 URL</p>
<dt>gnutls_pkcs11_token_info_t ttype</p>
<dd> Denotes the type of information requested</p>
<dt>void * output</p>
<dd> where output will be stored</p>
<dt>size_t * output_size</p>
<dd> contains the maximum size of the output and will be overwritten with actual</dl>
<h2>DESCRIPTION</h2>
<p> This function will return information about the PKCS 11 token such as the label, id, etc.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> (0) on success or a negative error code on error.</p>
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
