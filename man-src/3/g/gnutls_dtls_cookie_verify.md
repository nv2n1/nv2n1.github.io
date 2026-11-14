---
title: "gnutls_dtls_cookie_verify(3)"
name: "gnutls_dtls_cookie_verify"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_dtls_cookie_verify/"
description: "gnutls_dtls_cookie_verify – API function"
---

<h2>NAME</h2>
<p> gnutls_dtls_cookie_verify &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/dtls.h&gt;</code> </p>
<p> <code>int gnutls_dtls_cookie_verify(gnutls_datum_t * </code><i>key</i><code>, void * </code><i>client_data</i><code>, size_t </code><i>client_data_size</i><code>, void * </code><i>_msg</i><code>, size_t </code><i>msg_size</i><code>, gnutls_dtls_prestate_st * </code><i>prestate</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_datum_t * key</p>
<dd> is a random key to be used at cookie generation</p>
<dt>void * client_data</p>
<dd> contains data identifying the client (i.e. address)</p>
<dt>size_t client_data_size</p>
<dd> The size of client&#8217;s data</p>
<dt>void * _msg</p>
<dd> An incoming message that initiates a connection.</p>
<dt>size_t msg_size</p>
<dd> The size of the message.</p>
<dt>gnutls_dtls_prestate_st * prestate</p>
<dd> The cookie of this client.</dl>
<h2>DESCRIPTION</h2>
<p> This function will verify the received message for a valid cookie. If a valid cookie is returned then it should be associated with the session using <code>gnutls_dtls_prestate_set()</code>; </p>
<p> This function must be called after <code>gnutls_dtls_cookie_send()</code>.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> (0) on success, or a negative error code.</p>
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
