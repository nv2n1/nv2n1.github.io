---
title: "gnutls_srtp_set_profile_direct(3)"
name: "gnutls_srtp_set_profile_direct"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_srtp_set_profile_direct/"
description: "gnutls_srtp_set_profile_direct – API function"
---

<h2>NAME</h2>
<p> gnutls_srtp_set_profile_direct &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_srtp_set_profile_direct(gnutls_session_t </code><i>session</i><code>, const char * </code><i>profiles</i><code>, const char ** </code><i>err_pos</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const char * profiles</p>
<dd> is a string that contains the supported SRTP profiles, separated by colons.</p>
<dt>const char ** err_pos</p>
<dd> In case of an error this will have the position in the string the error occured, may be NULL.</dl>
<h2>DESCRIPTION</h2>
<p> This function is to be used by both clients and servers, to declare what SRTP profiles they support, to negotiate with the peer.</p>
<h2>RETURNS</h2>
<p> On syntax error <code>GNUTLS_E_INVALID_REQUEST</code> is returned, <code>GNUTLS_E_SUCCESS</code> on success, or an error code. </p>
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
