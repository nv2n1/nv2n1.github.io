---
title: "gnutls_pk_get_id(3)"
name: "gnutls_pk_get_id"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pk_get_id/"
description: "gnutls_pk_get_id – API function"
---

<h2>NAME</h2>
<p> gnutls_pk_get_id &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>gnutls_pk_algorithm_t gnutls_pk_get_id(const char * </code><i>name</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * name</p>
<dd> is a string containing a public key algorithm name.</dl>
<h2>DESCRIPTION</h2>
<p> Convert a string to a <code>gnutls_pk_algorithm_t</code> value. The names are compared in a case insensitive way. For example, gnutls_pk_get_id(&quot;RSA&quot;) will return <code>GNUTLS_PK_RSA</code>.</p>
<h2>RETURNS</h2>
<p> a <code>gnutls_pk_algorithm_t</code> id of the specified public key algorithm string, or <code>GNUTLS_PK_UNKNOWN</code> on failures.</p>
<h2>SINCE</h2>
<p> 2.6.0</p>
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
