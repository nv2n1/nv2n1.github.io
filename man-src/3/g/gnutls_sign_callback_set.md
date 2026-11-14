---
title: "gnutls_sign_callback_set(3)"
name: "gnutls_sign_callback_set"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_sign_callback_set/"
description: "gnutls_sign_callback_set – API function"
---

<h2>NAME</h2>
<p> gnutls_sign_callback_set &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>void gnutls_sign_callback_set(gnutls_session_t </code><i>session</i><code>, gnutls_sign_func </code><i>sign_func</i><code>, void * </code><i>userdata</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a gnutls session</p>
<dt>gnutls_sign_func sign_func</p>
<dd> function pointer to application&#8217;s sign callback.</p>
<dt>void * userdata</p>
<dd> void pointer that will be passed to sign callback.</dl>
<h2>DESCRIPTION</h2>
<p> Set the callback function. The function must have this prototype: </p>
<p> typedef int (*gnutls_sign_func) (gnutls_session_t session, void *userdata, gnutls_certificate_type_t cert_type, const gnutls_datum_t * cert, const gnutls_datum_t * hash, gnutls_datum_t * signature); </p>
<p> The <i>userdata</i> parameter is passed to the <i>sign_func</i> verbatim, and can be used to store application-specific data needed in the callback function. See also <code>gnutls_sign_callback_get()</code>.</p>
<h2>DEPRECATED</h2>
<p> Use the PKCS 11 or <code>gnutls_privkey_t</code> interfacess like <code>gnutls_privkey_import_ext()</code> instead.</p>
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
