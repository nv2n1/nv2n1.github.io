---
title: "gnutls_openpgp_privkey_export(3)"
name: "gnutls_openpgp_privkey_export"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_privkey_export/"
description: "gnutls_openpgp_privkey_export – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_privkey_export &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_privkey_export(gnutls_openpgp_privkey_t </code><i>key</i><code>, gnutls_openpgp_crt_fmt_t </code><i>format</i><code>, const char * </code><i>password</i><code>, unsigned int </code><i>flags</i><code>, void * </code><i>output_data</i><code>, size_t * </code><i>output_data_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_privkey_t key</p>
<dd> Holds the key.</p>
<dt>gnutls_openpgp_crt_fmt_t format</p>
<dd> One of gnutls_openpgp_crt_fmt_t elements.</p>
<dt>const char * password</p>
<dd> the password that will be used to encrypt the key. (unused for now)</p>
<dt>unsigned int flags</p>
<dd> (0) for future compatibility</p>
<dt>void * output_data</p>
<dd> will contain the key base64 encoded or raw</p>
<dt>size_t * output_data_size</p>
<dd> holds the size of output_data (and will be replaced by the actual size of parameters)</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the given key to RAW or Base64 format. If the buffer provided is not long enough to hold the output, then GNUTLS_E_SHORT_MEMORY_BUFFER will be returned.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an error code.</p>
<h2>SINCE</h2>
<p> 2.4.0</p>
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
