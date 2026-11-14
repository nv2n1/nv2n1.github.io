---
title: "gnutls_record_send(3)"
name: "gnutls_record_send"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_record_send/"
description: "gnutls_record_send – API function"
---

<h2>NAME</h2>
<p> gnutls_record_send &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>ssize_t gnutls_record_send(gnutls_session_t </code><i>session</i><code>, const void * </code><i>data</i><code>, size_t </code><i>data_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const void * data</p>
<dd> contains the data to send</p>
<dt>size_t data_size</p>
<dd> is the length of the data</dl>
<h2>DESCRIPTION</h2>
<p> This function has the similar semantics with <code>send()</code>. The only difference is that it accepts a GnuTLS session, and uses different error codes. Note that if the send buffer is full, <code>send()</code> will block this function. See the <code>send()</code> documentation for more information. </p>
<p> You can replace the default push function which is <code>send()</code>, by using <code>gnutls_transport_set_push_function()</code>. </p>
<p> If the EINTR is returned by the internal push function then <code>GNUTLS_E_INTERRUPTED</code> will be returned. If <code>GNUTLS_E_INTERRUPTED</code> or <code>GNUTLS_E_AGAIN</code> is returned, you must call this function again, with the exact same parameters; alternatively you could provide a <code>NULL</code> pointer for data, and 0 for size. cf. <code>gnutls_record_get_direction()</code>. </p>
<p> Note that in DTLS this function will return the <code>GNUTLS_E_LARGE_PACKET</code> error code if the send data exceed the data MTU value &#8211; as returned by <code>gnutls_dtls_get_data_mtu()</code>. The errno value EMSGSIZE also maps to <code>GNUTLS_E_LARGE_PACKET</code>. Note that since 3.2.13 this function can be called under cork in DTLS mode, and will refuse to send data over the MTU size by returning <code>GNUTLS_E_LARGE_PACKET</code>.</p>
<h2>RETURNS</h2>
<p> The number of bytes sent, or a negative error code. The number of bytes sent might be less than <i>data_size</i> . The maximum number of bytes this function can send in a single call depends on the negotiated maximum record size.</p>
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
