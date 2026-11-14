---
title: "gnutls_dtls_cookie_send(3)"
name: "gnutls_dtls_cookie_send"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_dtls_cookie_send/"
description: "gnutls_dtls_cookie_send – API function"
---

<h2>NAME</h2>
<p> gnutls_dtls_cookie_send &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/dtls.h&gt;</code> </p>
<p> <code>int gnutls_dtls_cookie_send(gnutls_datum_t * </code><i>key</i><code>, void * </code><i>client_data</i><code>, size_t </code><i>client_data_size</i><code>, gnutls_dtls_prestate_st * </code><i>prestate</i><code>, gnutls_transport_ptr_t </code><i>ptr</i><code>, gnutls_push_func </code><i>push_func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_datum_t * key</p>
<dd> is a random key to be used at cookie generation</p>
<dt>void * client_data</p>
<dd> contains data identifying the client (i.e. address)</p>
<dt>size_t client_data_size</p>
<dd> The size of client&#8217;s data</p>
<dt>gnutls_dtls_prestate_st * prestate</p>
<dd> The previous cookie returned by <code>gnutls_dtls_cookie_verify()</code></p>
<dt>gnutls_transport_ptr_t ptr</p>
<dd> A transport pointer to be used by <i>push_func</i></p>
<dt>gnutls_push_func push_func</p>
<dd> A function that will be used to reply</dl>
<h2>DESCRIPTION</h2>
<p> This function can be used to prevent denial of service attacks to a DTLS server by requiring the client to reply using a cookie sent by this function. That way it can be ensured that a client we allocated resources for (i.e. <code>gnutls_session_t</code>) is the one that the original incoming packet was originated from. </p>
<p> This function must be called at the first incoming packet, prior to allocating any resources and must be succeeded by <code>gnutls_dtls_cookie_verify()</code>.</p>
<h2>RETURNS</h2>
<p> the number of bytes sent, or a negative error code.</p>
<h2>SINCE</h2>
<p> 3.0</p>
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
