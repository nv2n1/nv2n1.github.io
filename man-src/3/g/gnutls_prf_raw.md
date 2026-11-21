---
title: "gnutls_prf_raw(3)"
name: "gnutls_prf_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_prf_raw/"
description: "gnutls_prf_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_prf_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_prf_raw(gnutls_session_t </code><i>session</i><code>, size_t </code><i>label_size</i><code>, const char * </code><i>label</i><code>, size_t </code><i>seed_size</i><code>, const char * </code><i>seed</i><code>, size_t </code><i>outsize</i><code>, char * </code><i>out</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</dt>
<dd> is a <code>gnutls_session_t</code> structure.</dd>
<dt>size_t label_size</dt>
<dd> length of the <i>label</i> variable.</dd>
<dt>const char * label</dt>
<dd> label used in PRF computation, typically a short string.</dd>
<dt>size_t seed_size</dt>
<dd> length of the <i>seed</i> variable.</dd>
<dt>const char * seed</dt>
<dd> optional extra data to seed the PRF with.</dd>
<dt>size_t outsize</dt>
<dd> size of pre-allocated output buffer to hold the output.</dd>
<dt>char * out</dt>
<dd> pre-allocated buffer to hold the generated data.</dd></dl>
<h2>DESCRIPTION</h2>
<p> Apply the TLS Pseudo-Random-Function (PRF) on the master secret and the provided data. </p>
<p> The <i>label</i> variable usually contains a string denoting the purpose for the generated data. The <i>seed</i> usually contains data such as the client and server random, perhaps together with some additional data that is added to guarantee uniqueness of the output for a particular purpose. </p>
<p> Because the output is not guaranteed to be unique for a particular session unless <i>seed</i> includes the client random and server random fields (the PRF would output the same data on another connection resumed from the first one), it is not recommended to use this function directly. The <code>gnutls_prf()</code> function seeds the PRF with the client and server random fields directly, and is recommended if you want to generate pseudo random data unique for each session.</p>
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
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
