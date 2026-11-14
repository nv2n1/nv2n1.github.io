---
title: "gnutls_psk_set_client_credentials(3)"
name: "gnutls_psk_set_client_credentials"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_psk_set_client_credentials/"
description: "gnutls_psk_set_client_credentials – API function"
---

<h2>NAME</h2>
<p> gnutls_psk_set_client_credentials &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_psk_set_client_credentials(gnutls_psk_client_credentials_t </code><i>res</i><code>, const char * </code><i>username</i><code>, const gnutls_datum_t * </code><i>key</i><code>, gnutls_psk_key_flags </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_psk_client_credentials_t res</p>
<dd> is a <code>gnutls_psk_client_credentials_t</code> structure.</p>
<dt>const char * username</p>
<dd> is the user&#8217;s zero-terminated userid</p>
<dt>const gnutls_datum_t * key</p>
<dd> is the user&#8217;s key</p>
<dt>gnutls_psk_key_flags flags</p>
<dd> indicate the format of the key, either <code>GNUTLS_PSK_KEY_RAW</code> or <code>GNUTLS_PSK_KEY_HEX</code>.</dl>
<h2>DESCRIPTION</h2>
<p> This function sets the username and password, in a gnutls_psk_client_credentials_t structure. Those will be used in PSK authentication. <i>username</i> should be an ASCII string or UTF-8 strings prepared using the &quot;SASLprep&quot; profile of &quot;stringprep&quot;. The key can be either in raw byte format or in Hex format (without the 0x prefix).</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise an error code is returned.</p>
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
