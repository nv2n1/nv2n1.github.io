---
title: "gnutls_range_split(3)"
name: "gnutls_range_split"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_range_split/"
description: "gnutls_range_split – API function"
---

<h2>NAME</h2>
<p> gnutls_range_split &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_range_split(gnutls_session_t </code><i>session</i><code>, const gnutls_range_st * </code><i>orig</i><code>, gnutls_range_st * </code><i>next</i><code>, gnutls_range_st * </code><i>remainder</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure</p>
<dt>const gnutls_range_st * orig</p>
<dd> is the original range provided by the user</p>
<dt>gnutls_range_st * next</p>
<dd> is the returned range that can be conveyed in a TLS record</p>
<dt>gnutls_range_st * remainder</p>
<dd> is the returned remaining range</dl>
<h2>DESCRIPTION</h2>
<p> This function should be used when it is required to hide the length of very long data that cannot be directly provided to <code>gnutls_record_send_range()</code>. In that case this function should be called with the desired length hiding range in <i>orig</i> . The returned <i>next</i> value should then be used in the next call to <code>gnutls_record_send_range()</code> with the partial data. That process should be repeated until <i>remainder</i> is (0,0).</p>
<h2>RETURNS</h2>
<p> 0 in case splitting succeeds, non zero in case of error. Note that <i>orig</i> is not changed, while the values of <i>next</i> and <i>remainder</i> are modified to store the resulting values.</p>
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
