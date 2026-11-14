---
title: "gnutls_alert_get_name(3)"
name: "gnutls_alert_get_name"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_alert_get_name/"
description: "gnutls_alert_get_name – API function"
---

<h2>NAME</h2>
<p> gnutls_alert_get_name &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>const char * gnutls_alert_get_name(gnutls_alert_description_t </code><i>alert</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_alert_description_t alert</p>
<dd> is an alert number.</dl>
<h2>DESCRIPTION</h2>
<p> This function will return a string that describes the given alert number, or <code>NULL</code>. See <code>gnutls_alert_get()</code>.</p>
<h2>RETURNS</h2>
<p> string corresponding to <code>gnutls_alert_description_t</code> value.</p>
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
