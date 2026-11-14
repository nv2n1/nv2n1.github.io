---
title: "gnutls_session_channel_binding(3)"
name: "gnutls_session_channel_binding"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_session_channel_binding/"
description: "gnutls_session_channel_binding – API function"
---

<h2>NAME</h2>
<p> gnutls_session_channel_binding &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_session_channel_binding(gnutls_session_t </code><i>session</i><code>, gnutls_channel_binding_t </code><i>cbtype</i><code>, gnutls_datum_t * </code><i>cb</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_channel_binding_t cbtype</p>
<dd> an <code>gnutls_channel_binding_t</code> enumeration type</p>
<dt>gnutls_datum_t * cb</p>
<dd> output buffer array with data</dl>
<h2>DESCRIPTION</h2>
<p> Extract given channel binding data of the <i>cbtype</i> (e.g., <code>GNUTLS_CB_TLS_UNIQUE</code>) type.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, <code>GNUTLS_E_UNIMPLEMENTED_FEATURE</code> if the <i>cbtype</i> is unsupported, <code>GNUTLS_E_CHANNEL_BINDING_NOT_AVAILABLE</code> if the data is not currently available, or an error code.</p>
<h2>SINCE</h2>
<p> 2.12.0</p>
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
