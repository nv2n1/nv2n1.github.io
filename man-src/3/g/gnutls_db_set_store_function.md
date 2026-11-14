---
title: "gnutls_db_set_store_function(3)"
name: "gnutls_db_set_store_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_db_set_store_function/"
description: "gnutls_db_set_store_function – API function"
---

<h2>NAME</h2>
<p> gnutls_db_set_store_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_db_set_store_function(gnutls_session_t </code><i>session</i><code>, gnutls_db_store_func </code><i>store_func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_db_store_func store_func</p>
<dd> is the function</dl>
<h2>DESCRIPTION</h2>
<p> Sets the function that will be used to store data in the resumed sessions database. This function must return 0 on success. </p>
<p> The first argument to <i>store_func</i> will be null unless <code>gnutls_db_set_ptr()</code> has been called.</p>
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
