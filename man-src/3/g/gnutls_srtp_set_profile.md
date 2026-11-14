---
title: "gnutls_srtp_set_profile(3)"
name: "gnutls_srtp_set_profile"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_srtp_set_profile/"
description: "gnutls_srtp_set_profile – API function"
---

<h2>NAME</h2>
<p> gnutls_srtp_set_profile &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_srtp_set_profile(gnutls_session_t </code><i>session</i><code>, gnutls_srtp_profile_t </code><i>profile</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_srtp_profile_t profile</p>
<dd> is the profile id to add.</dl>
<h2>DESCRIPTION</h2>
<p> This function is to be used by both clients and servers, to declare what SRTP profiles they support, to negotiate with the peer.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned. </p>
<p> Since 3.1.4</p>
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
