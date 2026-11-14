---
title: "gnutls_prf(3)"
name: "gnutls_prf"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_prf/"
description: "gnutls_prf – API function"
---

<h2>NAME</h2>
<p> gnutls_prf &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_prf(gnutls_session_t </code><i>session</i><code>, size_t </code><i>label_size</i><code>, const char * </code><i>label</i><code>, int </code><i>server_random_first</i><code>, size_t </code><i>extra_size</i><code>, const char * </code><i>extra</i><code>, size_t </code><i>outsize</i><code>, char * </code><i>out</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>size_t label_size</p>
<dd> length of the <i>label</i> variable.</p>
<dt>const char * label</p>
<dd> label used in PRF computation, typically a short string.</p>
<dt>int server_random_first</p>
<dd> non-zero if server random field should be first in seed</p>
<dt>size_t extra_size</p>
<dd> length of the <i>extra</i> variable.</p>
<dt>const char * extra</p>
<dd> optional extra data to seed the PRF with.</p>
<dt>size_t outsize</p>
<dd> size of pre-allocated output buffer to hold the output.</p>
<dt>char * out</p>
<dd> pre-allocated buffer to hold the generated data.</dl>
<h2>DESCRIPTION</h2>
<p> Applies the TLS Pseudo-Random-Function (PRF) on the master secret and the provided data, seeded with the client and server random fields. </p>
<p> The output of this function is identical to RFC5705 extractor if <i>extra</i> and <i>extra_size</i> are set to zero. Otherwise, <i>extra</i> should contain the context value prefixed by a two-byte length. </p>
<p> The <i>label</i> variable usually contains a string denoting the purpose for the generated data. The <i>server_random_first</i> indicates whether the client random field or the server random field should be first in the seed. Non-zero indicates that the server random field is first, 0 that the client random field is first. </p>
<p> The <i>extra</i> variable can be used to add more data to the seed, after the random variables. It can be used to make sure the generated output is strongly connected to some additional data (e.g., a string used in user authentication). </p>
<p> The output is placed in <i>out</i> , which must be pre-allocated.</p>
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
