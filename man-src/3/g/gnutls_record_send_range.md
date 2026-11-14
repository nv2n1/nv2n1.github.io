---
title: "gnutls_record_send_range(3)"
name: "gnutls_record_send_range"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_record_send_range/"
description: "gnutls_record_send_range – API function"
---

<h2>NAME</h2>
<p> gnutls_record_send_range &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>ssize_t gnutls_record_send_range(gnutls_session_t </code><i>session</i><code>, const void * </code><i>data</i><code>, size_t </code><i>data_size</i><code>, const gnutls_range_st * </code><i>range</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const void * data</p>
<dd> contains the data to send.</p>
<dt>size_t data_size</p>
<dd> is the length of the data.</p>
<dt>const gnutls_range_st * range</p>
<dd> is the range of lengths in which the real data length must be hidden.</dl>
<h2>DESCRIPTION</h2>
<p> This function operates like <code>gnutls_record_send()</code> but, while <code>gnutls_record_send()</code> adds minimal padding to each TLS record, this function uses the TLS extra-padding feature to conceal the real data size within the range of lengths provided. Some TLS sessions do not support extra padding (e.g. stream ciphers in standard TLS or SSL3 sessions). To know whether the current session supports extra padding, and hence length hiding, use the <code>gnutls_record_can_use_length_hiding()</code> function.</p>
<h2>NOTE</h2>
<p> This function currently is only limited to blocking sockets.</p>
<h2>RETURNS</h2>
<p> The number of bytes sent (that is data_size in a successful invocation), or a negative error code.</p>
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
