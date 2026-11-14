---
title: "gnutls_db_check_entry(3)"
name: "gnutls_db_check_entry"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_db_check_entry/"
description: "gnutls_db_check_entry – API function"
---

<h2>NAME</h2>
<p> gnutls_db_check_entry &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_db_check_entry(gnutls_session_t </code><i>session</i><code>, gnutls_datum_t </code><i>session_entry</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_datum_t session_entry</p>
<dd> is the session data (not key)</dl>
<h2>DESCRIPTION</h2>
<p> This function has no effect.</p>
<h2>RETURNS</h2>
<p> Returns <code>GNUTLS_E_EXPIRED</code>, if the database entry has expired or 0 otherwise.</p>
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
