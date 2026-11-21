---

title: "gnutls_hmac_fast(3)"
name: "gnutls_hmac_fast"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_hmac_fast/"
description: "gnutls_hmac_fast – API function"
---

<h2>NAME</h2>
<p> gnutls_hmac_fast &#8211; API function</p>
<p> <code>#include &lt;gnutls/crypto.h&gt;</code> </p>
<p> <code>int gnutls_hmac_fast(gnutls_mac_algorithm_t </code><i>algorithm</i><code>, const void * </code><i>key</i><code>, size_t </code><i>keylen</i><code>, const void * </code><i>text</i><code>, size_t </code><i>textlen</i><code>, void * </code><i>digest</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_mac_algorithm_t algorithm</dt>
<dd> the hash algorithm to use</dd>
<dt>const void * key</dt>
<dd> the key to use</dd>
<dt>size_t keylen</dt>
<dd> The length of the key</dd>
<dt>const void * text</dt>
<dd> the data to hash</dd>
<dt>size_t textlen</dt>
<dd> The length of data to hash</dd>
<dt>void * digest</dt>
<dd> is the output value of the hash</dd></dl>
<p> This convenience function will hash the given data and return output on a single call.</p>
<h2>RETURNS</h2>
<p> Zero or a negative error code on error.</p>
<h2>SINCE</h2>
<p> 2.10.0</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
