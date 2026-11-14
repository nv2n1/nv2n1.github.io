---
title: "gnutls_priority_mac_list(3)"
name: "gnutls_priority_mac_list"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_priority_mac_list/"
description: "gnutls_priority_mac_list – API function"
---

<h2>NAME</h2>
<p> gnutls_priority_mac_list &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_priority_mac_list(gnutls_priority_t </code><i>pcache</i><code>, const unsigned int ** </code><i>list</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_priority_t pcache</p>
<dd> is a <code>gnutls_prioritity_t</code> structure.</p>
<dt>const unsigned int ** list</p>
<dd> will point to an integer list</dl>
<h2>DESCRIPTION</h2>
<p> Get a list of available MAC algorithms in the priority structure.</p>
<h2>RETURNS</h2>
<p> the number of curves, or an error code.</p>
<h2>SINCE</h2>
<p> 3.2.3</p>
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
