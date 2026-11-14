---
title: "gnutls_mac_set_priority(3)"
name: "gnutls_mac_set_priority"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_mac_set_priority/"
description: "gnutls_mac_set_priority – API function"
---

<h2>NAME</h2>
<p> gnutls_mac_set_priority &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_mac_set_priority(gnutls_session_t </code><i>session</i><code>, const int * </code><i>list</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const int * list</p>
<dd> is a 0 terminated list of gnutls_mac_algorithm_t elements.</dl>
<h2>DESCRIPTION</h2>
<p> Sets the priority on the mac algorithms supported by gnutls. Priority is higher for elements specified before others. After specifying the algorithms you want, you must append a 0. Note that the priority is set on the client. The server does not use the algorithm&#8217;s priority except for disabling algorithms that were not specified.</p>
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
