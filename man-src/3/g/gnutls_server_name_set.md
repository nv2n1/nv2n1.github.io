---
title: "gnutls_server_name_set(3)"
name: "gnutls_server_name_set"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_server_name_set/"
description: "gnutls_server_name_set – API function"
---

<h2>NAME</h2>
<p> gnutls_server_name_set &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_server_name_set(gnutls_session_t </code><i>session</i><code>, gnutls_server_name_type_t </code><i>type</i><code>, const void * </code><i>name</i><code>, size_t </code><i>name_length</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_server_name_type_t type</p>
<dd> specifies the indicator type</p>
<dt>const void * name</p>
<dd> is a string that contains the server name.</p>
<dt>size_t name_length</p>
<dd> holds the length of name</dl>
<h2>DESCRIPTION</h2>
<p> This function is to be used by clients that want to inform (via a TLS extension mechanism) the server of the name they connected to. This should be used by clients that connect to servers that do virtual hosting. </p>
<p> The value of <i>name</i> depends on the <i>type</i> type. In case of <code>GNUTLS_NAME_DNS</code>, an ASCII (0)-terminated domain name string, without the trailing dot, is expected. IPv4 or IPv6 addresses are not permitted.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
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
