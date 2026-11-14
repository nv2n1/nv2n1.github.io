---
title: "gnutls_pem_base64_encode(3)"
name: "gnutls_pem_base64_encode"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pem_base64_encode/"
description: "gnutls_pem_base64_encode – API function"
---

<h2>NAME</h2>
<p> gnutls_pem_base64_encode &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_pem_base64_encode(const char * </code><i>msg</i><code>, const gnutls_datum_t * </code><i>data</i><code>, char * </code><i>result</i><code>, size_t * </code><i>result_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * msg</p>
<dd> is a message to be put in the header</p>
<dt>const gnutls_datum_t * data</p>
<dd> contain the raw data</p>
<dt>char * result</p>
<dd> the place where base64 data will be copied</p>
<dt>size_t * result_size</p>
<dd> holds the size of the result</dl>
<h2>DESCRIPTION</h2>
<p> This function will convert the given data to printable data, using the base64 encoding. This is the encoding used in PEM messages. </p>
<p> The output string will be null terminated, although the size will not include the terminating null.</p>
<h2>RETURNS</h2>
<p> On success <code>GNUTLS_E_SUCCESS</code> (0) is returned, <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> is returned if the buffer given is not long enough, or 0 on success.</p>
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
