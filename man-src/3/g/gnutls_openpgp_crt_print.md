---
title: "gnutls_openpgp_crt_print(3)"
name: "gnutls_openpgp_crt_print"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_crt_print/"
description: "gnutls_openpgp_crt_print – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_crt_print &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_crt_print(gnutls_openpgp_crt_t </code><i>cert</i><code>, gnutls_certificate_print_formats_t </code><i>format</i><code>, gnutls_datum_t * </code><i>out</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_crt_t cert</p>
<dd> The structure to be printed</p>
<dt>gnutls_certificate_print_formats_t format</p>
<dd> Indicate the format to use</p>
<dt>gnutls_datum_t * out</p>
<dd> Newly allocated datum with (0) terminated string.</dl>
<h2>DESCRIPTION</h2>
<p> This function will pretty print an OpenPGP certificate, suitable for display to a human. </p>
<p> The format should be (0) for future compatibility. </p>
<p> The output <i>out</i> needs to be deallocate using <code>gnutls_free()</code>.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an error code.</p>
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
