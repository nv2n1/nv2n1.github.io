---
title: "gnutls_tdb_set_verify_func(3)"
name: "gnutls_tdb_set_verify_func"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_tdb_set_verify_func/"
description: "gnutls_tdb_set_verify_func – API function"
---

<h2>NAME</h2>
<p> gnutls_tdb_set_verify_func &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_tdb_set_verify_func(gnutls_tdb_t </code><i>tdb</i><code>, gnutls_tdb_verify_func </code><i>verify</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_tdb_t tdb</p>
<dd> The trust storage</p>
<dt>gnutls_tdb_verify_func verify</p>
<dd> The verification function</dl>
<h2>DESCRIPTION</h2>
<p> This function will associate a retrieval function with the trust storage structure. The function is of the following form. </p>
<p> int gnutls_tdb_verify_func(const char* db_name, const char* host, const char* service, const gnutls_datum_t* pubkey); </p>
<p> The verify function should return zero on a match, <code>GNUTLS_E_CERTIFICATE_KEY_MISMATCH</code> if there is a mismatch and any other negative error code otherwise. </p>
<p> The <i>db_name</i> should be used to pass any private data to this function.</p>
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
